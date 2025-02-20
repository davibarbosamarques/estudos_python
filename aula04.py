#CALCULADORA DE OPERAÇÕES 1.0

num01 = float(input("Digite o primeiro numero: "))
num02 = float(input("Digite o segundo numero: "))

calculo = str(input("Digite a operação (ex: somar, subtrair, multiplicar ou dividir): "))

def soma():
    return num01 + num02

def subtrair():
    return num01 - num02

def multiplicar():
    return num01 * num02

def dividir():
    return num01 / num02

if(calculo == "somar"):
    print(soma())
elif(calculo == "subtrair"):
    print(subtrair())
elif(calculo == "multiplicar"):
    print(multiplicar())
elif(calculo == "dividir"):
    print(dividir())
else:
    print("A operação escolhida não está nas opções")
