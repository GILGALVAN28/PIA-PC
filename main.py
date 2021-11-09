# GILBERTO EDUARDO GALVAN GARCIA, MARCO ARTURO CANTU VIVANCO , KEILA SOFIA CABALLERO RAMOS

from traceback import print_tb
from typing import MutableMapping
import Metadata
import NetworkScan
import VirusTotal
import Codificacion
import Report
import argparse
import pyfiglet

descripcion = """Opciones disponibles:
                + Metadata (Obtener metadata de Imagenes o PDFs de manera Local o Web)
                -opc Metadata
                + NetworkScan (Obtener Ips activas y escaneo de puertos)
                -opc NetworkScan
                + Virustotal (Obtener nivel de riesgo de links en txt (url_sospechosas.txt))
                -opc Virustotal
                + Codificacion (Codificacion y Decodificacion de Mensajes y Archivos / Envio de archivos Codificados por correo)
                -opc Codificacion
                + Reporte (Generar Reporte de Procesos o EventLog)
                -opc Reporte
                      """
ascii_banner = pyfiglet.figlet_format("Tareas de Ciberseguridad")

#parámetros
parser = argparse.ArgumentParser(description= ascii_banner , epilog= descripcion, formatter_class=argparse.RawTextHelpFormatter)  
parser.add_argument("-opc", dest="opc", help="Opcion: (Metadata/NetworkScan/VirusTotal/Codificacion/Reporte)")
params = parser.parse_args()  
parametro = str(params.opc)

def clear():     
	import os
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')

if __name__ == '__main__':
    if parametro=="NetworkScan":
        clear()
        print("MENU DE OPCIONES")
        print("1. Scaneo de Red.")
        print("2. Scaneo de Puertos")
        print("3. Scaneo de Red y Puertos")
        print("4. Salir")
        op1 = (input("Seleccione una opción a buscar: "))
        while(op1 == str() or op1.isalpha() or op1.isspace() or int(op1) < 1 or int(op1) > 4):
            op1 = input("Seleccione una opción a buscar: ")
        if(int(op1) == 1):
            NetworkScan.netscan()
        if(int(op1) == 2):
            NetworkScan.portscan()
        if(int(op1) == 3):
            NetworkScan.portnetscan()
        if(int(op1) == 4):
            exit()
        input("Presione enter para continuar")

    elif (parametro=="Metadata"):
        clear()
        print("MENU DE OPCIONES")
        print("1. Obtener Metadata Local.")
        print("2. Obtener Metadata Web")
        print("3. Salir")
        op2 = (input("Seleccione una opción a buscar: "))
        while(op2 == str() or op2.isalpha() or op2.isspace() or int(op2) < 1 or int(op2) > 3):
            op2 = input("Seleccione una opción a buscar: ")
        if (int(op2) == 1):
            Metadata.local()
        if (int(op2) == 2):
            Metadata.web()
        if (int(op2) == 3):
            exit()

    elif (parametro=="VirusTotal"):
        VirusTotal.VirusTotalUrl()

    elif (parametro=="Codificacion"):
        clear()
        print("MENU DE OPCIONES")
        print("1. Cifrado Cesar")
        print("2. Descifrado Cesar")
        print("3. Codificacion Mensajes Base 64")
        print("4. Decodificacion Mensajes Base 64")
        print("5. Codificacion Archivos Base 64")
        print("6. Decodificacion Archivos Base 64")
        print("7. Envio de Archivos Codificados")
        print("8. Salir")
        op2 = (input("Seleccione una opción a buscar: "))
        while (op2 == str() or op2.isalpha() or op2.isspace() or int(op2) < 1 or int(op2) > 8):
            op2 = input("Seleccione una opción a buscar: ")
        if int(op2) == 1:
            Codificacion.cifrarcesar()
        if int(op2) == 2:
            Codificacion.descifrarcesar()
        if int(op2) == 3:
            Codificacion.base_enc()
        if int(op2) == 4:
            Codificacion.base_dec()
        if int(op2) == 5:
            Codificacion.encode()
        if int(op2) == 6:
            Codificacion.decode()
        if int(op2) == 7:
            Codificacion.correo_codb64()
        if int(op2) == 8:
            exit()
        exit()

    elif (parametro=="Reporte"):
        clear()
        print("MENU DE OPCIONES")
        print("1. Reporte EventLog")
        print("2. Reporte Procesos")
        print("3. Salir")
        op2 = (input("Seleccione una opción a buscar: "))
        while (op2 == str() or op2.isalpha() or op2.isspace() or int(op2) < 1 or int(op2) > 3):
            op2 = input("Seleccione una opción a buscar: ")
        if int(op2) == 1:
            Report.eventLog()
        if int(op2) == 2:
            Report.process()
        if int(op2) == 3:
            exit()
        exit()
    else:
        print("syntax error")