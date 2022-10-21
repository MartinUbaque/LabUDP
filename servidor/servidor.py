import socket
import time
import os
import time


UDP_IP = "127.0.0.1"
UDP_PORT = 5005
buf = 1024
file_name = r"C:\Users\marti\OneDrive\Documentos\Sexto semestre\Infracom\Lab3\data\archivoEnvio.txt"


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
nombreLog = str(time.ctime(time.time())).replace(" ","-").replace(":","-")+"-log.txt"

temp= nombreLog.split("-")


nombreLog= temp[6]+"-"+temp[1]+"-"+temp[2]+"-"+temp[3]+"-"+temp[4]+"-"+temp[5]+"-"+temp[7]



f = open(file_name, "rb")
file_stats = os.stat(file_name)
data = f.read(buf)
inicio = time.time()
while(data):
    if(sock.sendto(data, (UDP_IP, UDP_PORT))):
        data = f.read(buf)
        time.sleep(0.02) # Give receiver a bit time to save

sock.close()
f.close()
fin = time.time()


nombreArchivo = "archivoEnvio.txt"
tamañoArchivo = str(file_stats.st_size / (1024 * 1024))+"MB"

tiempoEjecucion=round(fin-inicio,2)

f= open(r"C:\Users\marti\OneDrive\Documentos\Sexto semestre\Infracom\Lab3\data\%s" % nombreLog,"w+")
f.write("Nombre archivo: "+nombreArchivo)
f.write("Tamaño archivo: "+tamañoArchivo)
f.write("Tiempo ejecución: "+str(tiempoEjecucion)+"s")