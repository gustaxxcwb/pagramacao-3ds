palavra_secreta = "girafa".lower()
letras_acertadas = ["_"] * len(palavra_secreta)
tentativas = 6
erros = 0

# Desenho da forca dividido em 6 partes
forca = [
    "   O   ",  # cabeça
    "   |   ",  # tronco
    "  /    ",  # braço esquerdo
    "  \\    ", # braço direito
    "  /     ", # perna esquerda
    "  \\     " # perna direita
]

def mostrar_forca(erros):
    print(" _______")
    print(" |     |")
    if erros > 0: print(" |    " + forca[0])
    if erros > 1: print(" |    " + forca[1])
    if erros > 2: print(" |   " + forca[2])
    if erros > 3: print(" |   " + forca[3])
    if erros > 4: print(" |   " + forca[4])
    if erros > 5: print(" |   " + forca[5])
    print(" |")
    print("_|_")

while tentativas > 0 and "_" in letras_acertadas:
    palpite = input("Digite uma letra: ").lower()

    if palavra_secreta.count(palpite) > 0:  # verifica se a letra aparece na palavra
        pos = palavra_secreta.find(palpite)  # primeira ocorrência
        while pos != -1:
            letras_acertadas[pos] = palavra_secreta[pos].upper()  # mostra em maiúscula
            pos = palavra_secreta.find(palpite, pos + 1)  # busca próxima ocorrência
    else:
        tentativas -= 1
        erros += 1
        print(f"Você errou! Restam {tentativas} tentativas.")
        mostrar_forca(erros)

    print(" ".join(letras_acertadas))

if "_" not in letras_acertadas:
    print("Parabéns, você ganhou!")
else:
    print("Que pena, você perdeu. A palavra era:", palavra_secreta.upper())
