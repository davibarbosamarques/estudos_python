soma = contador = 0
n = 0

while n >= 0:
    n = int(input("digite um numero positivo ou negativo: "))

    if n >= 0:
        soma += n
        contador += 1

print(f"soma total: {soma}")
print(f"Quantidade de números digitados: {contador}")
