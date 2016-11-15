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
except:
	sys.exit("Usage: python client.py receptor@IPreceptor:puertoSIP")

PORT = int(DATOS.split(":")[-1])
DIR_SIP = DATOS.split(":")[0]
#ACK = DATOS.split(":")[0] + 'SIP/2.0'

if METODO == 'INVITE':
	LINE = METODO + ' ' + 'sip:' + DIR_SIP + ' ' + 'SIP/2.0'
if METODO == 'BYE':
	LINE = DIR_SIP + ' ' + 'SIP/2.0'

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
my_socket.connect(('127.0.0.1', PORT))

print("Enviando: " + LINE)
my_socket.send(bytes(LINE, 'utf-8') + b'\r\n')
data = my_socket.recv(1024)

ACK = data.decode('utf-8')
#print(ACK)
ACK_MSG = 'OK SIP/2.0'
#print(ACK)

if ACK == ('SIP/2.0 100 Trying SIP/2.0 180 Ring SIP/2.0 200 OK'):
	my_socket.send(bytes(ACK_MSG, 'utf-8') + b'\r\n')
	
print('Recibido... ', data.decode('utf-8'))
print("Terminando socket...")

# Cerramos todo
my_socket.close()
print("Fin.")