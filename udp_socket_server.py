# Carga la biblioteca socket
from socket import *
# Carga sys para manejar argumentos
import sys
# Cargo datetime biblioteca de tiempo para el log
from datetime import datetime

# Chequeo de argumentos: puerto para escuchar.
if (len(sys.argv) != 2):
    print("Uso: udp_socket_server.py <server_port>")
    sys.exit()

#El primer argumento es el puerto...
port=int(sys.argv[1])

# Creo el socket UDP (SOCK_DGRAM)
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Asigno el puerto para escuchar y cualquier IP ''
serverSocket.bind(('', port))

#Envolvemos el loop en un try para capturar el Ctrl+C de corte
print("Iniciando servidor, en el puerto "+str(port)+", presione Ctrl+C para salir...")
try:
	while True:
		# Leemos el mensaje recibido y la dirección de donde viene
		message, address = serverSocket.recvfrom(1024)
		#decodificamos los bytes a string
		decoded = message.decode()
		#Logging a pantalla
		print("["+datetime.now().strftime("%H:%M:%S")+"] - Received '"+decoded+"' from: "+str(address[0])+":"+str(address[1]))
		# Pasamos el mensaje a mayúscula
		outgoing = decoded.upper()
		# Volvemos a enviarlo hacia la misma dirección y puerto del que vino.
		serverSocket.sendto(outgoing.encode(), address)

except KeyboardInterrupt:
	print("Closing socket...")
	serverSocket.close()
	print("Exiting...")
	sys.exit()