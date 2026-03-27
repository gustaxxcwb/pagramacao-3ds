import random

print("Bem-vindo ao jogo de adivinhação!")
print("Escolha o nível de dificuldade:")
print("1 - Fácil (número entre 1 e 10)")
print("2 - Médio (número entre 1 e 50)")
print("3 - Difícil (número entre 1 e 100)")

# Captura a escolha do usuário
nivel = input("Digite sua escolha (Fácil, Médio ou Difícil): ").strip().lower()

# Define o intervalo de acordo com o nível
if nivel == "fácil" or nivel == "facil" or nivel == "1":
    limite_superior = 10
elif nivel == "médio" or nivel == "medio" or nivel == "2":
    limite_superior = 50
elif nivel == "difícil" or nivel == "dificil" or nivel == "3":
    limite_superior = 100
else:
    print("Opção inválida. O jogo será iniciado no nível Fácil por padrão.")
    limite_superior = 10

# Gera o número secreto conforme o nível escolhido
numero_secreto = random.randint(1, limite_superior)
max_tentativas = 5

print(f"Tente adivinhar o número que estou pensando, entre 1 e {limite_superior}. Você tem {max_tentativas} tentativas.")

# Loop do jogo
for tentativa in range(max_tentativas):
    palpite = int(input(f"Tentativa {tentativa + 1}/{max_tentativas}. Digite seu palpite: "))

    if palpite == numero_secreto:
        print(f"Parabéns! Você acertou o número em {tentativa + 1} tentativas.")
        break
    elif palpite < numero_secreto:
        print("Quase lá! Tente um número maior.")
    else:
        print("Quase lá! Tente um número menor.")

    if tentativa == max_tentativas - 1:
        print(f"Suas tentativas acabaram. O número era {numero_secreto}.")

print("Fim do jogo!")
