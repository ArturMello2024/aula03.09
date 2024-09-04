lista_tarefas = []
# LISTA_TAREFA = []
# DICIONARIO ={
#     'id': "" ,
#     'descricao': "",
#     'status': "",
#     'prioridade': "",
# }
# LISTA = [x for x in LISTA if DICIONARIO in x]


def adicionar_tarefa(lista_tarefas, descricao, status, prioridade):
    if lista_tarefas:
        id = max(tarefa['id'] for tarefa in lista_tarefas) + 1
    else:
        id = 1

    novas_tarefas ={
        'id': id ,
        'descricao': descricao,
        'status': status,
        'prioridade': prioridade,
    }
    
    lista_tarefas.append(novas_tarefas)
    print(f"Tarefa {id} cadastrada com sucesso!")

def exibir_tarefa():
    for tarefa in lista_tarefas:
        print(f"Tarefa ID {lista_tarefas[0]}, descricao {lista_tarefas[1]}, status {lista_tarefas[2]}, prioridade{lista_tarefas[3]}.")

def filtrar_tarefa (status, prioridade):
    for tarefa in lista_tarefas:
        if tarefa == "status":
            print(f"status {lista_tarefas[2]}")
        if tarefa == "prioridade":
            print(f"prioridade{lista_tarefas[3]}")

def menu():
    while True:
        print("1 - ADICIONAR TAREFA")
        print("2 - EXIBIR LISTA DE TAREFAS")
        print("3 - FILTRAR TAREFA")
        opcao = input("Escolha uma opção")
        if opcao == "1":
            adicionar_tarefa(lista_tarefas, "estudar python", "pendente", "alta")

        elif opcao  == "2":
            print(lista_tarefas)

        elif opcao  == "3":
            buscarid = input("Entre com o status ou prioridade")
            filtrar_tarefa(id)
        else:
            return
menu()