import socket #CLIENTE

IP = "10.113.162.233"
porta = 8000

while True :
    conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conexao.connect((IP,porta))
    msgByte = conexao.recv(1024)
    print(msgByte.decode('ascii'))
    msg = input('Mande sua mensagem : ')
    conexao.send(msg.encode('ascii'))
    conexao.close