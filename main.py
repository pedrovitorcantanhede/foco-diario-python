print("================================")
print("          FOCO DIÁRIO")
print("================================")

prioridade_1 = input("Meta principal: ")
prioridade_2 = input("Meta secundária: ")
prioridade_3 = input("Meta terciária: ")

print()
print("===== PRIORIDADES DO DIA =====")
print("1. [ ]", prioridade_1)
print("2. [ ]", prioridade_2)
print("3. [ ]", prioridade_3)

print()
print("===== OUTRAS TAREFAS =====")

tarefas = []

resposta = input("Deseja adicionar uma tarefa? (s/n): ")
while resposta == "s" or resposta == "S":
    tarefa = input("Tarefa: ")
    tarefas.append(tarefa)
    resposta = input("Deseja adicionar outra tarefa? (s/n): ")
print()
print("===== MINHAS TAREFAS =====")
contador = 1
for tarefa in tarefas:
    print(contador, ". [ ]", tarefa)
    contador += 1

print()
print("Planejamento concluído.")
