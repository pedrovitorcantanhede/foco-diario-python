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

resposta = input("Deseja adicionar uma tarefa? (s/n): ")

while resposta == "s" or resposta == "S":
    tarefa = input("Tarefa: ")
    resposta = input("Deseja adicionar outra tarefa? (s/n): ")

print()
print("Planejamento concluído.")
