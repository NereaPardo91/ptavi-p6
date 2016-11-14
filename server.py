#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys

P = int(sys.argv[1])

class EchoHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """

    def handle(self):
        # Escribe dirección y puerto del cliente (de tupla client_address)
        self.wfile.write(b"Hemos recibido tu peticion")
        while 1:
            # Leyendo línea a línea lo que nos envía el cliente
            line = self.rfile.read()
            print("El cliente nos manda " + line.decode('utf-8'))

            # Si no hay más líneas salimos del bucle infinito
            if not line:
                break

if __name__ == "__main__":
    # Creamos servidor de eco y escuchamos
    serv = socketserver.UDPServer(('', P), EchoHandler)
    print("Lanzando servidor UDP de eco...")
    serv.serve_forever()

    #Debemos transformalo para llamarle de esta manera:
            # python.py metodo (INVITE O BYE) receptor@IPreceptor:puertoSIP
            # client.py BYE robin@193.147.73.20:5555
            # sino que nos salga el usage error
            #al servidor debemos darle un puerto distinto al 5060