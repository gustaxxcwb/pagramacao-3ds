# 1. Recebe a quantidade n de números
n = int(input("Digite um número inteiro positivo n: "))

# 2. Cria a lista e adiciona n números nela
lista = []
print(f"Digite os {n} números da lista:")
for i in range(n):
    num = int(input(f"Número {i+1}: "))
    lista.append(num)

# 3. Recebe o número x para verificar
x = int(input("Digite um número x para buscar na lista: "))

# 4. Verifica se x pertence à lista e exibe o resultado
if x in lista:
    print(f"O número {x} pertence à lista.")
else:
    print(f"O número {x} NÃO pertence à lista.")
