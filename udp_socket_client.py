# Carga la biblioteca socket
from socket import *
# Carga sys para manejar argumentos
import sys

# Chequeo de argumentos: host y puerto a conectarse
if (len(sys.argv) != 3):
    print("Uso: udp_socket_client.py <server_host> <server_port>")
    sys.exit()

#Envolvemos el loop en un try para capturar el Ctrl+C de corte
print("Iniciando cliente, presione Ctrl+C para salir...")
try:
    while True:
        # Creo el socket
        serverHost, serverPort = sys.argv[1:]
        clientSocket = socket(AF_INET, SOCK_DGRAM)
        clientSocket.settimeout(3) #timeout en segundos para el read.

        #Pedimos un mensaje al usuario.
        message = input("Mensaje: ")

        #Enviamos el mensaje por el cliente. encode() pasa el string a bytes.
        clientSocket.sendto(message.encode(),(serverHost, int(serverPort)))
        print("Mensaje enviado, usando el puerto "+str(clientSocket.getsockname()[1]))

        #Luego leemos un buffer de 1024 bytes a ver si hay respuesta. 
        #Esta llamada bloquea hasta recibir algo o timeout, por eso el try block
        try:
            receivedBytes, serverAddress = clientSocket.recvfrom(1024)
            #Pasamos el recibido a string nuevamente
            receivedMessage = receivedBytes.decode()
            print(receivedMessage)

        except TimeoutError:
            print("Timeout!")
                    
except KeyboardInterrupt:
    print("")
    print("Cerrando el socket...")
    clientSocket.close()
    print("Saliendo...")
    sys.exit()
