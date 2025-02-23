soma = 0
contador_pares = 0
contador_impares = 5

for i in range(0, 5):
    num = int((input("Digite um numero: ")))
    if num % 2 == 0:
        soma += num
        contador_pares += 1
    else:
       if contador_impares == 0:
           print("Nenhum numero par digitado")

media = soma / contador_pares

print(f"foram digitados {contador_pares} números pares")
print(f"a soma dos números pares é {soma}, a média é {media}")