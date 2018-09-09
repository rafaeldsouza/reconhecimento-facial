import cv2
#import urllib.request
import numpy as np
import util

#arquivo do classificador obtido
#https://github.com/opencv/opencv/tree/master/data/haarcascades
arqCasc = 'haarcascade_frontalface_default.xml'
classificador = cv2.CascadeClassifier(arqCasc)
classificadorOlho = cv2.CascadeClassifier('haarcascade-eye.xml')

amostra=1
#determina quantas imagens serão capturdas
numeroAmostra=25
#codigo que irá compor o nome da imagem e servirá para identificar a pessoa.
#obs.: na classe util deixei fixo o nome da pessoa, e futuramente irei cadastrar no banco de dados
id=input("Digite seu identificador: ")

largura,altura=220,220

print("Capturando as faces..")
#instancia o uso da webcam, na classe util será determinado qual camera será usada
webcam = util.Camera()  

while True:
    #pega efetivamente a imagem da webcam
    s, imagem = webcam.read()
    
    imagemCinza = cv2.cvtColor(imagem,cv2.COLOR_BGR2GRAY)

    #facesDetectadas=classificador.detectMultiScale(imagemCinza,
    #                                               scaleFactor=1.5,
    #                                               minSize=(150,150))

    facesDetectadas = classificador.detectMultiScale(imagem)
    

    # Desenha um retângulo nas faces detectadas
    for (x, y, l, a) in facesDetectadas:
        cv2.rectangle(imagem, (x, y), (x+l, y+a), (0, 255, 0), 2)

        regiao = imagem[y:y+a,x:x+l]
        regiaoCinzaOlho=cv2.cvtColor(regiao,cv2.COLOR_BGR2GRAY)
        
        olhosDetectados=classificadorOlho.detectMultiScale(regiaoCinzaOlho)
        # Desenha um retângulo nos olhos detectados
        for (ox, oy, ol, oa) in olhosDetectados:
             cv2.rectangle(regiao, (ox, oy), (ox+ol, oy+oa), (0, 0, 255), 2)
             #if np.average(imagemCinza) > 70: #indice de luminozidade           
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    imageFace=cv2.resize(imagemCinza[y:y+a,x:x+l],(largura,altura))
                    cv2.imwrite("fotos/pessoa."+str(id)+"."+str(amostra)+".jpg",imageFace)
                    print("[foto "+str(amostra)+ " capturada com sucesso]")
                    amostra+=1

    cv2.imshow('Video', imagem) #mostra a imagem captura na janela
    cv2.waitKey(1)
    if(amostra>=numeroAmostra+1):
        break

    

webcam.release() #dispensa o uso da webcam
cv2.destroyAllWindows() #fecha todas a janelas abertas
