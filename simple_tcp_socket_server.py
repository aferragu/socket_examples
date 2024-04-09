# Carga la biblioteca socket
from socket import *
# Carga sys para manejar argumentos
import sys
# Cargo datetime biblioteca de tiempo para el log
from datetime import datetime

# Chequeo de argumentos: puerto para escuchar.
if (len(sys.argv) != 2):
    print("Uso: simple_tcp_socket_server.py <server_port>")
    sys.exit()

#El primer argumento es el puerto...
port=int(sys.argv[1])

# Creo el socket TCP (SOCK_STREAM)
serverSocket = socket(AF_INET, SOCK_STREAM)
# Asigno el puerto para escuchar y cualquier IP ''
serverSocket.bind(('', port))

#Envolvemos el loop en un try para capturar el Ctrl+C de corte
print("Iniciando servidor, en el puerto "+str(port)+", presione Ctrl+C para salir...")
serverSocket.listen()

try:
    while True:
        #Esperamos una conexión
        connection,address = serverSocket.accept()
        print("Incoming connection from: "+str(address[0])+":"+str(address[1]))
        #una vez conectado, iniciamos recepción y transmisión de datos
        while True:
            # Leemos el mensaje recibido y la dirección de donde viene
            message = connection.recv(1024)

            if not message:  #si el mensaje está vacío es que se desconectó
                print("Cliente desconectado")
                connection.close()
                break

		    #decodificamos los bytes a string
            decoded = message.decode()
            #Logging a pantalla
            print("["+datetime.now().strftime("%H:%M:%S")+"] - Received: "+decoded)
            # Pasamos el mensaje a mayúscula
            outgoing = decoded.upper()
            # Volvemos a enviarlo hacia la misma dirección y puerto del que vino.
            connection.sendall(outgoing.encode())
		
except KeyboardInterrupt:
	print("Closing socket...")
	serverSocket.close()
	print("Exiting...")
	sys.exit()