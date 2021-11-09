# CIFRADO / CODIFICACION / ENVIO DE CORREOS

from typing import Callable
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import smtplib
import getpass


# FUNCION CIFRAR MENSAJE
def cifrarcesar():
    print("--CIFRADO CESAR--")
    message = input('Ingresa el mensaje: ')
    espacios = 1
    while espacios > 0:
        clave = input('Ingresa tu palabra clave para cifrar: ')
        espacios = clave.count(' ')
        if clave.isalpha() == False:
            espacios += 1
    key = len(clave)
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
    translated = ''
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex + key
            # print(translatedIndex)
            if translatedIndex >= len(SYMBOLS):
                translatedIndex = translatedIndex - len(SYMBOLS)
            elif translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)
            translated = translated + SYMBOLS[translatedIndex]
        else:
            # Append the symbol without encrypting/decrypting:
            translated = translated + symbol
    print(translated)
# cifrarcesar()


# FUNCION DESCIFRAR MENSAJE
def descifrarcesar():
    print("--DESCIFRADO CESAR--")
    message = input('Ingresa el mensaje: ')
    espacios = 1
    while espacios > 0:
        clave = input('Ingresa tu palabra clave para cifrar: ')
        espacios = clave.count(' ')
        if clave.isalpha() == False:
            espacios += 1
    key = len(clave)

    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

    translated = ''

    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex - key
            # print(translatedIndex)
            if translatedIndex >= len(SYMBOLS):
                translatedIndex = translatedIndex - len(SYMBOLS)
            elif translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            translated = translated + SYMBOLS[translatedIndex]
        else:
            translated = translated + symbol

    print(translated)
# descifrarcesar()


# FUNCION CODIFICAR MENSAJE
def base_enc():
    print("--CODIFICACION DE TEXTO BASE64--")
    message = input("Ingresa tu mensaje a codificar: ")
    message_bytes = message.encode("ascii")
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode("ascii")
    print(base64_message)
# base_enc()


# FUNCION DECODIFICAR MENSAJE
def base_dec():
    print("--DECODIFICACION DE TEXTO BASE64--")
    message = input("Ingresa tu mensaje a decodificar: ")
    message_bytes = message.encode("ascii")
    base64_bytes = base64.b64decode(message_bytes)
    base64_message = base64_bytes.decode("ascii")
    print(base64_message)
# base_dec()


def encode_decode_bytes(byte_message: bytes, encode_fn: Callable[[bytes], bytes]) -> bytes:
    return encode_fn(byte_message)


def save_file(path: str, content: bytes) -> None:
    with open(path, "wb") as file_to_save:
        file_to_save.write(content)


# FUNCION CODIFICAR ARCHIVO
def encode():
    print("--CODIFICACION DE ARCHIVOS BASE64--")
    def encode_file(path: str) -> bytes:
        with open(path, "rb") as file_to_encode:
            return encode_decode_bytes(file_to_encode.read(), base64.b64encode)
    path = input("Nombre del archivo a codificar: ")
    nombre = input("Guardar archivo en: ")
    save_file(nombre, encode_file(path))
# encode()


# FUNCION DECODIFICAR ARCHIVO
def decode():
    print("--DECODIFICACION DE ARCHIVOS BASE64--")
    def decode_file(path: str) -> bytes:
        file_to_encode = open(path, "rb")
        return encode_decode_bytes(file_to_encode.read(), base64.b64decode)
    path = input("Nombre del archivo a decodificar: ")
    nombre = input("Guardar archivo en: ")
    save_file(nombre, decode_file(path))
# decode()


# FUNCIÓN ENVIAR CORREO CON ARCHIVO CODIFICADO
def correo_codb64():
    print("--ENVIO DE ARCHIVOS CODIFICADOS POR CORREO--")
    data = {
        "user": "",
        "pass": ""
    }
    user = input("Correo Emisor: ")
    pasw = getpass.getpass("Contraseña: ")
    data["user"] = user
    data["pass"] = pasw

    email_msg = MIMEMultipart()

    # datos correo
    email_msg["From"] = data["user"]
    correo = input("Correo Receptor: ")
    receipents = [correo]
    email_msg["To"] = ", ".join(receipents)
    email_msg["Subject"] = input("Asunto del Correo: ")


    message = input("Mensaje del Correo: ")
    email_msg.attach(MIMEText(message, "plain"))

    def encode(path: str) -> bytes:
        with open(path, "rb") as file_to_encode:
            return encode_decode_bytes(file_to_encode.read(), base64.b64encode)
    path = input("Archivo a enviar: ")
    nombre = path + ".txt"

    save_file(nombre, encode(path))

    with open(nombre, "rb") as arch:
        attach = MIMEApplication(arch.read(), _subtype="txt",)
    attach.add_header("Content-Disposition", "attachment", filename=nombre)
    email_msg.attach(attach)
    # create server
    server = smtplib.SMTP("smtp.office365.com:587")
    server.starttls()

    # Login Credentials for sending the mail
    server.login(data["user"], data["pass"])

    # send the message via the server.
    server.sendmail(email_msg["From"], receipents, email_msg.as_string())
    server.quit()
    print("successfully sent email to %s:" % (email_msg["To"]))
#correo_codb64()
