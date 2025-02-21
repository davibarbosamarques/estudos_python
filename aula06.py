#SOMA DOS NUMEROS PARES
'''num = int(input("Digite um numero:"))

if(num > 1):
    for i in range(num, 0, num % 2 == 0):
        print(i)
else:
    "Esse numero não é suficiente"'''

num = int(input("Digite um numero:"))

soma_pares = 0

if(num > 1):
    for i in range(2, num + 1, +2):
        soma_pares += i

    print(f"A soma dos números pares de 1 até {num} é: {soma_pares}")
else:
    print("numero precisa ser maior que 1")
