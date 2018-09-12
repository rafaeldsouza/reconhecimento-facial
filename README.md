## Sistema de Reconhecimento Facial

# Objetivo

Desenvolver técnicas de reconhecimento facial utilizando câmera IP fazendo tratamentos de ruídos (inicialmente a baixa luminosidade usando câmera com visão noturna).

# Pré Requisito

*Python 3.6*

*OpenCV-contrib*

https://pypi.org/project/opencv-contrib-python/

comando para instalar: pip install opencv-contrib-python

# Projeto

Quando falamos em reconhecer algo devemos pensar primeiramente como iremos detectar o objeto, para tanto, foi utilizado o metodo Viola-Jones para a criação e execução de um detector. Inicialmente treina-se um detector, salvando-o em um arquivo XML para que este, em seguida, possa ser utilizado sempre que se deseje detectar faces em imagens. 

*Detecção de rostos com OpenCv*

Para nossa sorte o OpenCv já possui vários classificadores pré-treinados para detecção de faces, olhos, e sorrisos e nesse projeto estou utilizando apenas a detecção da face e dos olhos.
