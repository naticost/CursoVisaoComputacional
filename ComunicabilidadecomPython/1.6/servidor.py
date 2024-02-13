import socket
import cv2

IP =  "10.112.0.15"
porta = 8000

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((IP, porta))
servidor.listen(1)
print(f"Aguardando conexão na porta {porta}...")

conexao, endereco_cliente = servidor.accept()
print(f"Conexão estabelecida com {endereco_cliente}")

captura = cv2.VideoCapture(0)
detector_rosto = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    ret, frame = captura.read()
    cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rostos = detector_rosto.detectMultiScale(cinza, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    if len(rostos) > 0:
        x, y, w, h = rostos[0]
        coordenadas = f"Rosto encontrado: x={x}, y={y}, largura={w}, altura={h}"
        conexao.send(coordenadas.encode('ascii'))

    conexao.close()