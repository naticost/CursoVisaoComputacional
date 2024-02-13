

import cv2 as cv
import os
import time 

def capturar_imagens(classe, quantidade, diretorio):
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)

    cap = cv.VideoCapture(0, cv.CAP_DSHOW)
    contador = 1

    while contador <= quantidade:
        ret, frame = cap.read()

        cv.imshow('Capturando Imagens', frame)
        
        nome_arquivo = f'{diretorio}/imagem_{classe}_{contador}.png'
        cv.imwrite(nome_arquivo, frame)

        print(f'Imagem {contador} capturada para {classe}')

        contador += 1

        time.sleep(0.1)

        key = cv.waitKey(1)
        if key == 27:
            break

    cap.release()
    cv.destroyAllWindows()


# Exemplo de uso:
diretorio_verde = 'Modulo 4 - Alunos\imgs/verde'
capturar_imagens('verde', 400, diretorio_verde)

time.sleep(15.0)

diretorio_rosa = 'Modulo 4 - Alunos\imgs/rosa'
capturar_imagens('rosa', 400, diretorio_rosa)