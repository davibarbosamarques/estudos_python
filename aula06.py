#SOMA DOS NUMEROS PARES
num = int(input("Digite um numero: "))

soma_pares = 0

if(num > 1):
    for i in range(2, num + 1, +2):
        soma_pares += i

    print(f"A soma dos números PARES de 1 até {num} é: {soma_pares}")
else:
    print("numero precisa ser maior que 1")
