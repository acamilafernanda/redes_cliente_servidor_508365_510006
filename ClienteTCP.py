import socket
import random
import time

HOST = '127.0.0.1'
PORT = 5000

i = 0
while i < 10:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    num = str(random.randint(0, 999999999999999999999999999999))
    s.sendall(str.encode(num))
    data = s.recv(1024)
    print('Mensagem ecoada:', data.decode(), "\nFIM")
    s.close()
    time.sleep(10)
    i += 1