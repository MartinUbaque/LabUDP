import socketserver
import os
from datetime import datetime
import time

ServerAddress = ("127.0.0.1", 8888)

class MyUDPRequestHandler(socketserver.DatagramRequestHandler):
    archivo = input('Ingrese el archivo: ')
    def log(self, archivo, cliente, tiempo, confirmacion):
        nombreLog = datetime.today().strftime('%Y-%m-%d-%H-%M-%S')+'-log.txt'
        size = os.path.getsize(archivo)
        with open('Logs/'+nombreLog, 'a+') as f:
            f.write(f'Archivo: {archivo} size: {size} cliente {cliente} tiempo: {str(tiempo)} ms tuvo resultado {confirmacion}.\n')

    def handle(self):
        archivo = self.archivo
        datagram = self.rfile.readline().strip()
        file = open(archivo, 'rb')
        buf=1024
        start = time.time()
        data = file.read(buf)
        while(data):
            self.wfile.write(data)
            data = file.read(buf)
        end = time.time()
        confirmacion = 'OK'
        self.log(archivo, self.client_address, end-start, confirmacion)  
        print(f'Se envió el archivo al cliente {self.client_address}')         

 
UDPServerObject = socketserver.ThreadingUDPServer(ServerAddress, MyUDPRequestHandler)
UDPServerObject.serve_forever()
