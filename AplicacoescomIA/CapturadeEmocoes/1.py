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
diretorio_Surpreso = 'Aplicacao_AI2/imgs/surpreso'
capturar_imagens('Surpreso', 400, diretorio_Surpreso)


time.sleep(15.0)

diretorio_Neutro = 'Aplicacao_AI2/imgs/neutro'
capturar_imagens('Neutro', 400, diretorio_Neutro)

time.sleep(15.0)

diretorio_Feliz = 'Aplicacao_AI2/imgs/feliz'
capturar_imagens('Feliz', 400, diretorio_Feliz)