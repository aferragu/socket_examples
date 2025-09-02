# Carga la biblioteca socket
from socket import *
from urllib.parse import urlparse

# Carga sys para manejar argumentos
import sys

# Chequeo de argumentos: host y puerto a conectarse
if (len(sys.argv) != 2):
    print("Uso: simple_pop3_client.py <server>")
    sys.exit()

serverHost = sys.argv[1]
serverPort = 110

print("Iniciando conexión desde el cliente...")

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.settimeout(10.0)
clientSocket.connect((serverHost,serverPort))
address = clientSocket.getsockname()
print("Conexión establecida usando el puerto "+str(address[1]))        

message = clientSocket.recv(1024)
print(">>"+message.decode())

user = input("Usuario: ")
password = input("Password: ")

clientSocket.sendall((f"user {user}\r\n").encode())
message = clientSocket.recv(1024)
print(">>"+message.decode())

clientSocket.sendall((f"pass {password}\r\n").encode())
message = clientSocket.recv(1024)
print(">>"+message.decode())

clientSocket.sendall(("list\r\n").encode())
message = clientSocket.recv(1024)
print("Esta es su lista de mensajes:")
print(">>"+message.decode())

while True:
    index = input("Indique el mensaje a descargar (o Enter para salir):")

    if index=="":
        print("Saliendo...")
        clientSocket.sendall(("quit\r\n").encode())
        clientSocket.close()
        sys.exit()
    else:
        clientSocket.sendall(("retr "+index+"\r\n").encode())
        message = clientSocket.recv(1024)
        print(">>"+message.decode())

