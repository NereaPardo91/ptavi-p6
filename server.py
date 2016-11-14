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
        line = self.rfile.read()
        print("El cliente nos manda " + line.decode('utf-8'))
        line = line.decode('utf-8').split()

        if line[0] == 'INVITE':
            self.wfile.write(b'SIP/2.0 100 Trying' + ' ' + b'SIP/2.0 180 Ring')
        if line[0] == 'BYE':
            self.wfile.write(b'adios')

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