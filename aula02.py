#CALCULADORA DE MEDIA 2.0

nota01 = float(input("digite sua primeira nota: "))
nota02 = float(input("digite sua segunda nota: "))

if(nota01 < 4 or nota02 < 4):
    segundachamada = float(input("digite sua nota da segunda chamada: "))
    if(nota01 < 4):
        nota01 = segundachamada
    else:
        nota02 = segundachamada


media = (nota01 + nota02) / 2
faltas = 7 

if(media >= 7 and faltas <= 4):
    print("sua media foi" + " " + str(media))
    print("e suas faltas foram " + str(faltas) + "/4")
    print("situação: aprovado")

elif(7 > media >= 4 and faltas <= 4):
    print("sua media foi" + " " + str(media))
    print("e suas faltas foram " + str(faltas) + "/4")
    print("situação: recuperação")

else:
    print("sua media foi" + " " + str(media))
    print("e suas faltas foram " + str(faltas) + "/4")
    if(faltas > 4 and media < 7):
        print("Reprovado por excesso de faltas e nota")
    elif(faltas > 4):
        print("Reprovado por excesso de faltas")
    else:
        print("Reprovado por nota")

