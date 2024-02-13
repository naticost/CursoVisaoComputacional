
import cv2
import numpy as np
from sklearn import svm
import pickle
import os

def carregar_dados(diretorio, rotulo):
    dados = []
    rotulos = []
    for arquivo in os.listdir(diretorio):
        caminho = os.path.join(diretorio, arquivo)
        imagem = cv2.imread(caminho)
        imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)
        dados.append(imagem.flatten())
        rotulos.append(rotulo)
    return dados, rotulos

diretorio_rosa = 'Modulo 4 - Alunos\imgs/rosa'
diretorio_verde = 'Modulo 4 - Alunos\imgs/verde'

dados_rosa, rotulos_rosa = carregar_dados(diretorio_rosa, 'rosa')
dados_verde, rotulos_verde = carregar_dados(diretorio_verde, 'verde')

dados_treino = np.concatenate([dados_rosa, dados_verde])
rotulos_treino = np.concatenate([rotulos_rosa, rotulos_verde])

svm_modelo = svm.SVC(kernel='linear', C=1)
svm_modelo.fit(dados_treino, rotulos_treino)

with open('modelo_svm_cores.pkl', 'wb') as arquivo:
    pickle.dump(svm_modelo, arquivo)

webcam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

estado_anterior = "Indefinida"

while True:
    _, frame = webcam.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    imagem_achatada = frame.flatten()

    predicao = svm_modelo.predict([imagem_achatada])[0]

    if predicao != estado_anterior:
        estado_anterior = predicao
        print(f'Cor: {predicao}')

    cor_bgr = (255, 0, 255) if predicao == 'rosa' else (0, 255, 0) if predicao == 'verde' else (128, 128, 128)
    cv2.putText(frame, f'Cor: {predicao}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, cor_bgr, 2)
    cv2.imshow('Classificacao em Tempo Real', cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))

    key = cv2.waitKey(1)
    if key == 27:
        break


webcam.release()
cv2.destroyAllWindows()