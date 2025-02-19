#Entendendo funções no python

def imprimirMensagens(linguagem, curso):
    msn = (f"essa é minha primeira função usando {linguagem} no curso de {curso}")
    return msn

qualLinguagem = input("Digite a linguagem que vc esta estudando: ")
qualCurso = input("Digite o curso que vc esta fazendo: ")

mensagem = imprimirMensagens(qualLinguagem, qualCurso)
print(mensagem)