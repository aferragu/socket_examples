# Ejemplos de Sockets para el curso de Redes
## Universidad ORT Uruguay

Los archivos de Python incluyen diferentes clientes y servidores con sockets con y sin conexión.
Los servidores hacen un simple eco de los mensajes recibidos. Los clientes muestran un prompt
para introducir el mensaje y esperan la respuesta.

* `udp_socket_server.py`: servidor sin conexión escuchando en un puerto UDP.
* `udp_socket_client.py`: cliente por UDP.
* `simple_tcp_socket_server.py`: servidor básico en puerto TCP.
* `threaded_tcp_socket_server.py`: servidor usando threads en puerto TCP.
* `simple_tcp_socket_client.py`: clienta básico TCP.

Modo de uso:

> `python udp_socket_server.py <puerto>`

> `python udp_socket_client.py <IPdestino> <puerto>`

y análogo para los TCP.

Si lo quieren probar local necesitan un intérprete Python 3 y pueden hacer lo siguiente:

 * En una consola llaman al servidor con `python udp_socket_server.py 5000`
 * En otra consola llaman al cliente con `python udp_socket_client.py localhost 5000`
   La dirección `localhost` es una dirección particular que hace referencia a la propia máquina.
------

Creado por Andrés Ferragut
Curso Redes, Universidad ORT Uruguay
