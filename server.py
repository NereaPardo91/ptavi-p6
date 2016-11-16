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
            self.wfile.write(b'SIP/2.0 100 Trying' + b' ' + b'SIP/2.0 180 Ring' + b' ' + b'SIP/2.0 200 OK')
        elif line[0] == 'BYE':
            self.wfile.write(b'adios')
        elif line[0] == 'ACK':
            self.wfile.write(b'SIP/2.0 200 OK')
        else:
            self.wfile.write(b'SIP/2.0 405 Method Not Allowed')

if __name__ == "__main__":
    # Creamos servidor de eco y escuchamos
    serv = socketserver.UDPServer(('', P), EchoHandler)
    print("Lanzando servidor UDP de eco...")
    serv.serve_forever()
