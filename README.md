# PIA-PC
PIA de Programacion para Ciberseguridad UANL

## Suite de Seguridad

- Metadata (Obtener metadata de Imagenes o PDFs de manera Local o Web)
- Codificacion (Codificacion y Decodificacion de Mensajes y Archivos / Envio de archivos Codificados por correo)
- Escaneo de Red (Obtener Ips activas y escaneo de puertos)
- Reportes (Generar Reporte de Procesos o EventLog)
- API Virus Total (Obtener nivel de riesgo de links en txt (url_sospechosas.txt))

## Instalacion
Para la instalacion de este repositorio en Linux

```bash
sudo apt install git
git clone https://github.com/GILGALVAN28/PIA-PC
cd PIA-PC
```
Para la instalacion de este repositorio en Termux

```bash
pkg install git
pkg install python
git clone https://github.com/GILGALVAN28/PIA-PC
cd PIA-PC
```
Para la instalacion de los modulos
```bash
pip install -r requirements.txt
```
## Usage
- main.py   
Funcion -h: Nos ayuda para desplegar el modo de uso
```bash
python main.py -h 
```
Funcion Metadata: Nos ayuda para hacer uso del modulo de Metadata, al inicio nos mostrara un menu y tendremos que seleccionar si queremos obtener metadata de manera local o web, una vez hecho esto nos aparecera otro menu y tendremos que seleccionar si queremos obtener la metadata de imagenes o de pdfs. 
Para el uso de Metadata en Local es necesario tener una carpeta con el nombre de 'Img a Analizar' y otra con 'Pdfs a Analizar'.
```bash
python main.py -opc Metadata
```

Funcion Codificacion: Nos ayuda para hacer uso del modulo de Codificacion, nos mostrara un menu para hacer el uso de las siguientes herramientas de codificacion: Cifrado y Descifrado Cesar. Codificacion y Decodificacion de Mensajes y archivos en Base 64,Envio de Archivos Codificados.
```bash
python main.py -opc Codificacion
```

Funcion Escaneo de Red: Nos ayuda para hacer uso del modulo de NetworkScan, nos mostrara un menu para hacer uso de un escaneo de red, escaneo de puertos o escaneo de red con sus respectivos puertos abiertos, haciendo uso del modulo SOCKET.
```bash
python main.py -opc NetworkScan
```

Funcion Reportes: Nos ayuda para hacer uso del modulo de Reportes, nos muestra un menu para generar Reporte de Procesos en base a su tamaño o EventLog en los eventos mas recientes.
```bash
python main.py -opc Reportes
```

Funcion VirusTotal: Nos ayuda para hacer uso del modulo de VirusTotal, hace uso de la API de [VirusTotal](https://www.virustotal.com/gui/home/url) para analizar URLs desde la terminal.
```bash
python main.py -opc VirusTotal
```
## CONTRIBUTORS
- Gilberto Eduardo Galvan Garcia [GILGALVAN28](https://github.com/GILGALVAN28)
- Keila Sofia Caballero Ramos [Aliekaifos](https://github.com/Aliekaifos)
- Marco Arturo Cantu Vivanco [Mark-1805](https://github.com/Mark-1805)
