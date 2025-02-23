#entendendo while

n = 1
pares = impares = 0

while n != 0:
    n = int(input("Digite um número: "))
    if n != 0:
        if n % 2 == 0:
            pares += 1
        else:
            impares += 1

print(f"vc digitou {pares} números pares e {impares} números impares")


