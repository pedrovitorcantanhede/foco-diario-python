print("================================")
print("          FOCO DIÁRIO")
print("================================")

prioridades = [ 
    input("Digite a primeira prioridade do dia: "),
    input("Digite a segunda prioridade do dia: "),
    input("Digite a terceira prioridade do dia: ")
]

prioridades_concluidas = [False, False, False]
print()
print("===== PRIORIDADES DO DIA =====")
print("1. [ ]", prioridades[0])
print("2. [ ]", prioridades[1])
print("3. [ ]", prioridades[2])

while True:
    numero = int(input("Qual prioridade deseja concluir? (0 para sair): "))

    if numero == 0:
        break

    if 1 <= numero <= 3:
        prioridades_concluidas[numero - 1] = True
        print("Prioridade concluída!")
    else:
        print("Número inválido. Prioridade não concluída.")

print()
print("===== SITUAÇÃO DAS PRIORIDADES =====")

for i in range(3):
    if prioridades_concluidas[i]:
        print(i + 1, ". [X]", prioridades[i])
    else:
        print(i + 1, ". [ ]", prioridades[i])
print()
print("===== OUTRAS TAREFAS =====")

tarefas = []
concluidas = [] 
resposta = input("Deseja adicionar uma tarefa? (s/n): ")
while resposta == "s" or resposta == "S":
    tarefa = input("Tarefa: ")
    tarefas.append(tarefa)
    concluidas.append(False) 
    resposta = input("Deseja adicionar outra tarefa? (s/n): ")
print()
print("===== MINHAS TAREFAS =====")
contador = 1
for tarefa in tarefas:
    print(contador, ". [ ]", tarefa)
    contador += 1    

while True:  
    numero = int(input("Qual tarefa deseja concluir? (0 para sair): "))
    if numero == 0:
      break
    if 1<= numero <= len(tarefas):
        if concluidas[numero - 1]:
            print("Essa tarefa já foi concluída.")
        concluidas[numero - 1] = True
        print("Tarefa concluída!")
    else:
        print("Número inválido. Tarefa não concluída.")

for i in range(len(tarefas)):
    if concluidas[i]:
        print(i + 1, ". [X]", tarefas[i])
    else:
        print(i + 1, ". [ ]", tarefas[i])

print()
print("Planejamento concluído.")
