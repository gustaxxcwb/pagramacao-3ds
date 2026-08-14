# --- 1. Entrada de Dados ---
qtd_tarefas = int(input("Quantas tarefas deseja cadastrar? "))

lista_tarefas = []
for i in range(qtd_tarefas):
    nome = input(f"Digite a tarefa {i + 1}: ")
    lista_tarefas.append(nome)

# --- 2. Processamento de Dados ---
banco_dados_tarefas = []

# Percorre a lista gerando IDs a partir de 1 e calculando prazos progressivos
for id_tarefa, nome_tarefa in enumerate(lista_tarefas, start=1):
    prazo_dias = id_tarefa * 2  # Exemplo de progressão: Tarefa 1 -> 2 dias, Tarefa 2 -> 4 dias, etc.
    status = "Pendente"
    
    # Armazena as informações estruturadas em uma tupla
    banco_dados_tarefas.append((id_tarefa, nome_tarefa, prazo_dias, status))

# --- 3. Saída de Dados com Desempacotamento ---
print("\n--- RESUMO DO SISTEMA ---")

# Percorre o banco de dados desempacotando diretamente a tupla
for id_tarefa, nome_tarefa, prazo_dias, status in banco_dados_tarefas:
    print(f"ID: {id_tarefa} | Tarefa: {nome_tarefa} | Prazo: {prazo_dias} dias | Status: {status}")

# Exibição do total de tarefas utilizando len()
print(f"\nTotal de tarefas gerenciadas: {len(banco_dados_tarefas)}")
