import os, time
import socket
import logging

# NetScan
def netscan():
    logging.basicConfig(filename='app.log', level= 'DEBUG')
    ip = input(str("Ingresa la red que deseas escanear (192.168.0.), solo clase C: "))
    nombre = input("Archivo donde se guardara el output: ")
    try:
        os.makedirs("Netscan")
        logging.info("Se creo la Carpeta Netscan")
    except:
        logging.info("La carpeta Netscan ya existia")
        pass 
    folder = ("Netscan")
    os.chdir(os.path.join(os.getcwd(), folder))
    file = open(nombre + ".txt", "a")
    file.write("IPs Habilitadas\n")
    for x in range(82, 88):
        time.sleep(5)
        ipre = (ip + str(x))
        result = os.popen("ping -n 1 " + ip + str(x))
        for linija in result.readlines():
            if "TTL" in linija:
                file.write(ipre + '\n')       
        else:
            pass


#PortScan
def portscan():
    ip = input(str("Ingresa la ip que deseas escanear (192.168.0.0): "))
    #port_ini = int(input("Puerto inicial: "))
    #port_fin = int(input("Puerto final: "))
    nombre = input("Archivo donde se guardara el output: ")
    puertos = [21, 22, 80, 443, 445, 8080]
    try:
        os.makedirs("Portscan")
    except:
        pass 
    folder = ("Portscan")
    os.chdir(os.path.join(os.getcwd(), folder))
    file = open(nombre + ".txt", "a")
    file.write(ip + '\n')
    for port in puertos:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((ip, port))
        if result == 0:
            file.write("Port: " + str(port) + " Open\n")
        else:
            pass
    print("Terminado")


# PortNetScan
def portnetscan():
    ips = []
    ip = input(str("Ingresa la red que deseas escanear (192.168.0.), solo clase C: "))
    #port_ini = int(input("Puerto inicial: "))
    #port_fin = int(input("Puerto final: "))
    nombre = input("Archivo donde se guardara el output: ")
    puertos = [21, 22, 80, 443, 445, 8080]
    try:
        os.makedirs("PortNetScan")
    except:
        pass 
    folder = ("PortNetScan")
    os.chdir(os.path.join(os.getcwd(), folder))
    for x in range(82, 88):
        time.sleep(5)
        ipre = (ip + str(x))
        result = os.popen("ping -n 1 " + ip + str(x))
        for linija in result.readlines():
            if "TTL" in linija:
                ips.append(ipre)      
        else:
            pass
    print(ips)
    for ips1 in ips:
        file = open(nombre+".txt", "a")
        file.write(ips1 + '\n')
        for port in puertos:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = s.connect_ex((ips1, port))
            if result == 0:
                file.write("Port: " + str(port) + " Open\n")
            else:
                pass
        file.write('\n')
    print("Terminado")
