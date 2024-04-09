# Carga la biblioteca socket
from socket import *
# Carga sys para manejar argumentos
import sys

# Chequeo de argumentos: host y puerto a conectarse
if (len(sys.argv) != 3):
    print("Uso: tcp_socket_client.py <server_host> <server_port>")
    sys.exit()

#recuperamos los argumentos
serverHost = sys.argv[1]
serverPort = int(sys.argv[2])

#Envolvemos el loop en un try para capturar el Ctrl+C de corte
print("Iniciando conexión desde el cliente, presione Ctrl+C para salir...")

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverHost,serverPort))
address = clientSocket.getsockname()
print("Conexión establecida usando el puerto "+str(address[1]))        

try:
    while True:

        #Pedimos un mensaje al usuario.
        message = input("Mensaje: ")

        #Enviamos el mensaje por el cliente. encode() pasa el string a bytes.
        clientSocket.sendall(message.encode())

        #Luego leemos un buffer de 1024 bytes a ver si hay respuesta. Esta llamada bloquea hasta recibir algo o timeout.
        receivedBytes= clientSocket.recv(1024)
        #Pasamos el recibido a string nuevamente
        receivedMessage = receivedBytes.decode()
        print(receivedMessage)

except KeyboardInterrupt:
    print("")
    print("Cerrando el socket...")
    clientSocket.close()
    print("Saliendo...")
    sys.exit()
