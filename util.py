import cv2
import os.path
import numpy as np

##Metodo que determina qual será a camera usada, apenas para padronizar o uso
arqDados = 'dados.npy'
def Camera():
    #camera do computador
    camera = cv2.VideoCapture(0)  
    #camera ip
    #camera = cv2.VideoCapture('http://192.168.25.164/videostream.cgi?user=admin&amp;pwd=&amp;resolution=32&amp;rate=0') 
    return camera

def getDimensao():
    return 220,220 #220, 220

#mock com os nomes para colocar nas imagens
def getNome(id):
    nome = ""
    if os.path.isfile(arqDados):
        ls = list(np.load(arqDados))
        nome = ls[id-1]
    return nome

def setNome(nome):
    ls = []
    if os.path.isfile(arqDados):
        ls = list(np.load(arqDados))
    ls.append(nome)
    np.save(arqDados,ls)

def getProximoId():
    ls = []
    if os.path.isfile(arqDados):
        ls = list(np.load(arqDados))
    return len(ls)+1

def histogram_eq(image):
    '''
    Perform histogram equalization on the input image.

    See https://en.wikipedia.org/wiki/Histogram_equalization.
    '''

    image1 = np.copy(image)

    image1 = cv2.cvtColor(image1, cv2.COLOR_RGB2HSV)

    image1[:,:,2] = cv2.equalizeHist(image1[:,:,2])

    image1 = cv2.cvtColor(image1, cv2.COLOR_HSV2RGB)

    return image1