import random
numero_secreto = random.randint(1, 100)
contador = 0
n = 0
while True:
    n = int(input("Tente adivinhar o número entre 1 e 100:")) 
    
    if n < 1 or n > 100:
        print("Número fora do intervalo! Digite um número entre 1 e 100.")
        continue

    contador += 1

    if n > numero_secreto:
        print("o número é menor que o digitado")
    elif n < numero_secreto:
        print("o número é maior que o digitado")
    else:
        print(f"Parabens vc acertou com {contador} tentativas")
        break
