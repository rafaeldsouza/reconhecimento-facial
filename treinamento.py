# -*- coding: utf-8 -*-
"""
Created on Tue May  1 21:40:56 2018
@author: Rafael de Souza
Classe que treinará usando as tecnicas EigenFace, FisherFace e LBPH
"""

import cv2
import os
import numpy as np

def Treinar():
    eigenface = cv2.face.EigenFaceRecognizer_create(num_components=50,threshold=0)
    fisherface = cv2.face.FisherFaceRecognizer_create()
    lbph = cv2.face.LBPHFaceRecognizer_create()

    #testes passando paramentros
    #eigenface = cv2.face.EigenFaceRecognizer_create(40, 8000)
    #fisherface = cv2.face.FisherFaceRecognizer_create(3, 2000)
    #lbph = cv2.face.LBPHFaceRecognizer_create(2, 2, 7, 7, 50)

    def getImagemComID():
        caminhos = [os.path.join("fotos",f) for f in os.listdir('fotos')]
        faces=[]
        ids=[]
        for caminhoImagem in caminhos:
            imagemFace = cv2.cvtColor(cv2.imread(caminhoImagem),cv2.COLOR_BGR2GRAY)
            id = int(os.path.split(caminhoImagem)[-1].split('.')[1])
            ids.append(id)
            faces.append(imagemFace)
            #print(id)
            #cv2.imshow("Face",imagemFace)
            #cv2.waitKey(20)
        return np.array(ids),faces
            
            
    ids,faces = getImagemComID()
    #print(ids)
    print('treinando...')

    eigenface.train(faces,ids)
    eigenface.write('classificadorEingen.yml')

    fisherface.train(faces,ids)
    fisherface.write('classificadorFisherface.yml')

    lbph.train(faces,ids)
    lbph.write('classificadorLbph.yml')

    print("Treinamento realizado")
