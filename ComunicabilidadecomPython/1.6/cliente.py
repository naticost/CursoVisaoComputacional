import socket

IP =  "10.112.0.15"
porta = 8000

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((IP, porta))

while True:
    coordenadas = cliente.recv(1024).decode('ascii')
    print(coordenadas)

    cliente.send("Ok".endode('ascii'))