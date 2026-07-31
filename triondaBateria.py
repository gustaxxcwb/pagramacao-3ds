# 1. Definição das variáveis (exemplos de teste, altere os valores para testar)
bateria_atual = 10  # Número inteiro de 0 a 100
bola_em_jogo = True  # Valor booleano: True ou False

# 2. Processamento das condições (If / Elif / Else) de forma ordenada
if bateria_atual < 15 and bola_em_jogo:
    # Condição 1
    print(
        "ALERTA MÁXIMO: Bateria baixa! Substitua a bola na próxima paralisação."
    )

elif bateria_atual < 15 and not bola_em_jogo:
    # Condição 2
    print("Aviso: Bateria baixa. Aproveite a bola parada para trocá-la.")

else:
    # Condição 3 (Caso Geral)
    print("Sistema Trionda operando normalmente. Bateria ok.")
