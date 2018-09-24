import cv2
import numpy as np
import util

arqFace = 'haarcascade_frontalface_default.xml'
arqOlhos = 'haarcascade-eye.xml'

classificador = cv2.CascadeClassifier(arqFace)
classificadorOlho = cv2.CascadeClassifier(arqOlhos)

largura, altura = util.getDimensao()

amostra=1

def histogram_eq(image):
    '''
    Perform histogram equalization on the input image.

    See https://en.wikipedia.org/wiki/Histogram_equalization.
    '''

    image1 = np.copy(image)

    image1 = cv2.cvtColor(image1, cv2.COLOR_RGB2HSV)

    image1[:,:,2] = cv2.equalizeHist(image1[:,:,2])

    #image1 = cv2.cvtColor(image1, cv2.COLOR_HSV2RGB)
    image1 = cv2.cvtColor(image1, cv2.COLOR_HSV2BGR)

    return image1 


webcam = util.Camera()
while True:
    # pega efetivamente a imagem da webcam
    s, imagem = webcam.read()
    #imagem = histogram_eq(imagem)
    original = np.copy(imagem)
    imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    #eq = histogram_eq(imagem)

    facesDetectadas = classificador.detectMultiScale(imagem)
    for (x, y, l, a) in facesDetectadas:
        cv2.rectangle(imagem, (x, y), (x+l, y+a), (0, 255, 0), 2)

        regiao = imagem[y:y+a, x:x+l]
        regiaoCinzaOlho = cv2.cvtColor(regiao, cv2.COLOR_BGR2GRAY)

        olhosDetectados = classificadorOlho.detectMultiScale(regiaoCinzaOlho)
        # Desenha um retângulo nos olhos detectados
        if len(olhosDetectados)==2:
            for (ox, oy, ol, oa) in olhosDetectados:
                cv2.rectangle(regiao, (ox, oy),(ox+ol, oy+oa), (0, 0, 255), 2)
                imageFace = cv2.resize(imagemCinza[y:y+a, x:x+l], (largura, altura))
                cv2.imwrite("passos/hist.original."+str(amostra)+".jpg", original)
                cv2.imwrite("passos/hist.detectada."+str(amostra)+".jpg", imagem)
                cv2.imwrite("passos/hist.face."+str(amostra)+".jpg", imageFace)
                amostra += 1           
            

    cv2.imshow('Video', imagem)  # mostra a imagem captura na janela
    #cv2.imshow('VideoEqua', eq)
    cv2.waitKey(1)
    






'''
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite("passos/normal.jpg", imagem)
        

        break
    
    
    cv2.waitKey(1)
'''