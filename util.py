import cv2
##Metodo que determina qual será a camera usada, apenas para padronizar o uso
def Camera():
    #camera do computador
    camera = cv2.VideoCapture(0)  
    #camera ip
    #camera = cv2.VideoCapture('http://192.168.15.7/videostream.cgi?user=admin&amp;pwd=&amp;resolution=32&amp;rate=0') 
    return camera

#mock com os nomes para colocar nas imagens
def getNome(id):
    nome = ""
    if id==1:
        nome = "Rafael"
    elif id==2:
        nome = "Suzana"    
    return nome


