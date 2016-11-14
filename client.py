#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente que abre un socket a un servidor
"""

import socket
import sys

try:
	METODO = sys.argv[1]
	DATOS = sys.argv[2]
	PORT = int(DATOS.split(":")[-1])
except:
	sys.exit("Usage: python client.py receptor@IPreceptor:puertoSIP")

#AQUI VAN TODOS LOS METODOS INVITE, ACK, BYE
if METODO == 'INVITE':
	LINE = METODO

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
my_socket.connect(('127.0.0.1', PORT))


print("Enviando: " + LINE)
my_socket.send(bytes(LINE, 'utf-8') + b'\r\n')
data = my_socket.recv(1024)

print('Recibido -- ', data.decode('utf-8'))
print("Terminando socket...")

# Cerramos todo
my_socket.close()
print("Fin.")