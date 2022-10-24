import socket
import threading
import select
import os
import time
from datetime import datetime

msgFromClient       = "Hello UDP Server"
bytesToSend         = str.encode(msgFromClient)
bufferSize          = 1024
serverAddressPort   = ("127.0.0.1", 8888)

def log(archivo, cliente, tiempo, confirmacion):
        nombreLog = datetime.today().strftime('%Y-%m-%d-%H-%M-%S')+'-log.txt'
        size = os.path.getsize(archivo)
        with open(nombreLog, 'a+') as f:
            f.write(f'Archivo: {archivo} size: {size} cliente {cliente} tiempo: {str(tiempo)} ms tuvo resultado {confirmacion}.\n')

def Connect2Server(nClient, nConexiones):
    nombreArchivo = f'Cliente{nClient}-Prueba-{nConexiones}.txt'
    timeout = 3
    UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)
    start = time.time()
    f = open(nombreArchivo, 'wb+')
    while True:
        ready = select.select([UDPClientSocket], [], [], timeout)
        if ready[0]:
            data, addr = UDPClientSocket.recvfrom(bufferSize)
            f.write(data)
            confirmacion = 'NO OK'
        else:
            f.close()
            confirmacion = 'OK'
            break
    end = time.time()
    log(nombreArchivo, nClient, end-start, confirmacion)

ThreadList  = []
ThreadCount = int(input('Ingrese el número de clientes: '))

for index in range(ThreadCount):
    ThreadInstance = threading.Thread(target=Connect2Server, args=(index, ThreadCount))
    ThreadList.append(ThreadInstance)
    ThreadInstance.start()

for index in range(ThreadCount):
    ThreadList[index].join()