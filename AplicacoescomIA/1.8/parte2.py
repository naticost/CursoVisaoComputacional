

import os
import cv2
import numpy as np
from sklearn import svm
import pickle

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