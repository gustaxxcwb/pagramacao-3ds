import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 10)
    tentativas = 0
    max_tentativas = 5

    print("🎉 Bem-vindo ao jogo de adivinhação!")
    print("Tente adivinhar o número que estou pensando, entre 1 e 10.")
    print(f"Você tem {max_tentativas} tentativas.\n")

    while tentativas < max_tentativas:
        try:
            palpite = int(input("Digite seu palpite: "))
        except ValueError:
            print("⚠️ Entrada inválida! Digite apenas números inteiros.")
            continue

        if palpite < 1 or palpite > 10:
            print("⚠️ O número deve estar entre 1 e 10.")
            continue

        tentativas += 1

        if palpite == numero_secreto:
            print(f"✅ Parabéns! Você acertou o número em {tentativas} tentativa(s).")
            break
        elif palpite < numero_secreto:
            print("🔼 Quase lá! Tente um número maior.")
        else:
            print("🔽 Quase lá! Tente um número menor.")

        if tentativas < max_tentativas:
            print(f"Você ainda tem {max_tentativas - tentativas} tentativa(s).\n")

    else:
        print(f"❌ Infelizmente, você não acertou. O número era {numero_secreto}.")
        print("Fim do jogo!")

# Executa o jogo
if __name__ == "__main__":
    jogo_adivinhacao()
