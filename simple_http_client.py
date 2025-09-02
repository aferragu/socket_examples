# Carga la biblioteca socket
from socket import *
from urllib.parse import urlparse

# Carga sys para manejar argumentos
import sys

# Chequeo de argumentos: host y puerto a conectarse
if (len(sys.argv) != 2):
    print("Uso: simple_http_client.py <URL>")
    sys.exit()

url = urlparse(sys.argv[1])

serverHost = url.hostname
if url.port:
    serverPort = url.port
else:
    serverPort = 80

print("Iniciando conexión desde el cliente...")

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.settimeout(10.0)

clientSocket.connect((serverHost,serverPort))
address = clientSocket.getsockname()
print("Conexión establecida usando el puerto "+str(address[1]))        

pedidoHTTP = f"GET {url.path} HTTP/1.1\r\nHost: {url.hostname}\r\n\r\n"
print(pedidoHTTP)
clientSocket.sendall(pedidoHTTP.encode())

data_buffer = b''
receivedBytes= clientSocket.recv(65536)
data_buffer+=receivedBytes

print(data_buffer.decode())

clientSocket.close()
sys.exit()
