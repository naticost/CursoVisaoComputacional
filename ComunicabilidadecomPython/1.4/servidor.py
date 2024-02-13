import socket #SERVIDOR

IP = "10.113.163.91"
porta = 8000

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket.AF_INET = usará Ipv4 como protocolo  -- Socket.SOCK_STREAM = usará conexao bidimencional TCP
servidor.bind((IP, porta))  # função é usada para associar um socket a um endereço IP
servidor.listen(1) # .bind = aceitar conexões de processos clientes, (4) = 

while True :
    cliente, endereco = servidor.accept() #Este método retorna dois valores: o socket com a conexão do processo cliente e uma tupla com o endereço e porta do processo cliente.
    msg = input('Escreva uma mensagem : ')
    msgBytes = msg.encode('ascii')
    cliente.send(msgBytes) #Gera a string em formato de dados + encode = indica codificação da string
    print('Aguardando mensagem do cliente ...')
    msgBytes = cliente.recv(1024) # Retorna dados codificados  
    print(msgBytes.decode('ascii')) #transforma os dados codificados em string
    cliente.close() #Finaliza a conexão
