import requests
import cv2 as cv
import base64
import numpy as np

url = 'http://10.113.163.47:5000/img'

while True:
    resposta = requests.post(url)
   
    if resposta.status_code == 200:
        resultado = resposta.json()
        buffer = base64.b64decode(resultado["imagem"].replace("data:image/jpg;base64,",''))
        imgArray = np.frombuffer(buffer, np.int8)
        img = cv.imdecode(imgArray, cv.IMREAD_UNCHANGED)
        cv.imshow('Imagem',img)
        tecla = cv.waitKey(1)
        if tecla ==ord('q'):
            break
    elif resposta.status_code == 400:
        error = resposta.json
        print(f'Erro :{error}')
        break
    else:
        print("erro de requisição")
        break