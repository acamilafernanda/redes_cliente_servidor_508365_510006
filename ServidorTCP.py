import socket

HOST = 'localhost'
PORT = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()

i = 0
while i < 10:
    print ('Aguardando conexão de um cliente')
    conn, ender = s.accept()
    print ('Conectado em ', ender)
    data = int(conn.recv(1024))

    if ((data / 1000000000) >= 1):
        conn.sendall(str.encode(str(data)))
    else:
        if data % 2 == 0:
            conn.sendall(str.encode("PAR"))
        conn.sendall(str.encode("ÍMPAR"))
    i += 1
conn.close()