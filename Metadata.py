import PyPDF2
import os
import glob
from PyPDF2 import PdfFileReader
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from PIL.ExifTags import TAGS, GPSTAGS
from PIL import Image
import time
import folium
from folium import plugins
from geopy.geocoders import Nominatim



# Es necesario tener 2 carpetas con las imagenes y pdfs llamadas Img a Analizar y Pdfs a Analizar

def descargaimg():
    try:
        os.makedirs("Imgs Descargadas")
    except:
        pass  
    url = input("Ingresa la url de donde quieres obtener las imagenes: ")
    folder = ("Imgs Descargadas")
    os.chdir(os.path.join(os.getcwd(), folder))
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    images = soup.find_all('img')
    for image in images:
        name = image['alt']
        link = image['src']
        with open(name.replace(' ', '-').replace('/', '') + '.jpg', 'wb') as f:
            im = requests.get(link)
            f.write(im.content)
    print("Imagenes Descargadas")



def decode_gps_info(exif):
    gpsinfo = {}
    if 'GPSInfo' in exif:
        #Parse geo references.
        #print(exif['GPSInfo'])
        
        Nsec = exif['GPSInfo'][2][2] 
        Nmin = exif['GPSInfo'][2][1]
        Ndeg = exif['GPSInfo'][2][0]
        Wsec = exif['GPSInfo'][4][2]
        Wmin = exif['GPSInfo'][4][1]
        Wdeg = exif['GPSInfo'][4][0]
        if exif['GPSInfo'][1] == 'N':
            Nmult = 1
        else:
            Nmult = -1
        if exif['GPSInfo'][3] == 'E':
            Wmult = 1
        else:
            Wmult = -1
        Lat = Nmult * (Ndeg + (Nmin + Nsec/60.0)/60.0)
        Lng = Wmult * (Wdeg + (Wmin + Wsec/60.0)/60.0)
        exif['GPSInfo'] = {"Lat" : Lat, "Lng" : Lng}
        

 
def get_exif_metadata(image_path):
    ret = {}
    image = Image.open(image_path)
    if hasattr(image, '_getexif'):
        exifinfo = image._getexif()
        if exifinfo is not None:
            for tag, value in exifinfo.items():
                decoded = TAGS.get(tag, tag)
                ret[decoded] = value
    decode_gps_info(ret)
    return ret
    
def printMetalocal():
    IMGs = []
    lista =[]
    ruta = "Img a Analizar" 
    os.chdir(ruta)
    for img in glob.glob("*.jpg"):
        IMGs.append(img)
    for img in glob.glob(".jpg"):
        IMGs.append(img)
    for root, dirs, files in os.walk(".", topdown=False):
        for name in IMGs:
            fileimg = open(name+".txt", "a") 
            fileimg.write("[+] Metadata for file: " + (name) + '\n')
            try:
                exifData = {}
                exif = get_exif_metadata(name)
                for metadata in exif:
                    fileimg.write("Metadata: " +str(metadata) + " - Value:  " + str(exif[metadata]) + "\n")
                lista.append(exif["GPSInfo"])
            except:
                import sys, traceback
                traceback.print_exc(file=sys.stdout)
    #print(lista)
    listadat = []
    listanom = []
    for i in lista:
        listadat.append(list(i.values()))
    # print(listadat)
    for i in lista:
        uno = str(i['Lat'])
        dos = str(i['Lng'])
        listanom.append(uno + "," + dos)
    # print(listanom)
    mapa = folium.Map(location=listadat[0], zoom_start=12)
    count = 0
    for i in listadat:
        geolocalizador = Nominatim(user_agent="Prueba")
        ubicacion = geolocalizador.reverse(listanom[count])
        ubi = ubicacion.raw['display_name']
        mapa.add_child(plugins.HeatMap([i]))
        mapa.add_child(folium.Marker(location=i, icon=folium.Icon(color="red"), popup=ubi))
        time.sleep(3)
        count += 1
    path = os.getcwd()
    mapa.save(path + "\Mapa.html")
    print("Metadata Guardada")


def printMetaweb():
    IMGs = []
    for img in glob.glob("*.jpg"):
        IMGs.append(img)
    for img in glob.glob(".jpg"):
        IMGs.append(img)
    for root, dirs, files in os.walk(".", topdown=False):
        for name in IMGs:
            fileimg = open(name+".txt", "a") 
            file1 = open("imgdescargadas.txt", "a")
            file1.write(name+"\n")
            fileimg.write("[+] Metadata for file: " + (name) + '\n')
            try:
                exifData = {}
                exif = get_exif_metadata(name)
                for metadata in exif:
                    fileimg.write("Metadata: " +str(metadata) + " - Value:  " + str(exif[metadata]) + "\n")
            except:
                import sys, traceback
                traceback.print_exc(file=sys.stdout)
    print("Metadata Guardada")


PDFs = []
IMGss = []
IMGs =[]
pdfsdescargados = []


#LOCAL
def local():
    #menu
    print("Obtener metadata en ruta local de:")
    print("1) PDFs")
    print("2) Imágenes")
    print("3) salir")
    op = input("Seleccione una opción: ")
    while(op == str() or op.isalpha() or op.isspace() or int(op) < 0 or int(op) > 3):
        op = input("Seleccione una opción: ")
    #PDFs
    if(int(op) == 1): 
        for pdf in glob.glob("Pdfs a Analizar\*.pdf"):
            PDFs.append(pdf)
        for pdf in PDFs:
            pdf_toread = PdfFileReader(open(pdf, "rb"))
            pdf_info = pdf_toread.getDocumentInfo()
            file = open(pdf+".txt", "w")
            file.write(str(pdf_info))
        print("Metadata de PDFs Guardada")

    #IMG
    if(int(op) == 2): 
        printMetalocal()      
    
    #Salir
    if(int(op) == 3): 
        exit()
   

# WEB
def web():
    #menu
    print("Descargar y obtener metadata de:")
    print("1) PDFs")
    print("2) Imágenes")
    print("3) salir")
    op = input("Seleccione una opción: ")
    while(op == str() or op.isalpha() or op.isspace() or int(op) < 0 or int(op) > 4):
        op = input("Seleccione una opción: ")
    #PDFs
    if(int(op) == 1): 
        if os.path.exists("Pdf Descargados\pdfdescargados.txt"):
            os.remove("Pdf Descargados\pdfdescargados.txt")
        url = input("Ingresa la url de donde quieres obtener los pdf: ")
        folder_location = ("Pdf Descargados")
        if not os.path.exists(folder_location):os.mkdir(folder_location)
        response = requests.get(url)
        soup= BeautifulSoup(response.text, "html.parser")     
        for link in soup.select("a[href$='.pdf']"):
            filename = os.path.join(folder_location,link['href'].split('/')[-1])
            with open(filename, 'wb') as f:
                f.write(requests.get(urljoin(url,link['href'])).content)
        for pdf in glob.glob("Pdf Descargados\*.pdf"):
            PDFs.append(pdf)
        for pdf in PDFs:
            pdf_toread = PdfFileReader(open(pdf, "rb"))
            pdf_info = pdf_toread.getDocumentInfo()
            file = open(pdf+".txt", "w")
            file.write(str(pdf_info))
            pdfsdescargados.append(pdf)
            file1 = open("Pdf Descargados\pdfdescargados.txt", "a")
            file1.write(pdf+"\n")
        print("Metadata de PDFs Guardada")

    #IMGs
    if(int(op) == 2):
        descargaimg()
        printMetaweb()
    
    #Salir
    if(int(op) == 3): 
        exit()

