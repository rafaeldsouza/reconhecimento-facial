import captura
import treinamento
while True:
    print("Escolha uma opção:")
    print(" Digite 1 para: Capturar Fotos.")
    print(" Digite 2 para: Treinar.")
    print(" Digite 3 para: Reconhecer.")
    print(" Qualquer outra opção encerrará o programa")
    entrada = input("Entre com o número correspondente:")
    if entrada=="1":
        cap = captura.CapturaFace()
        cap.Capturar(25)
    elif entrada=="2":
        treinamento.Treinamento()
    elif entrada=="3":
        print("reconhece")
    else:
        break
    