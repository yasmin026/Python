print("=====================================")
print("Bem-vindo ao sistema de tarefas!")
print("=====================================")

tarefas = []
while True:
    print("\n0 O que você deseja fazer?")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3 - Concluir/Remover uma tarefa")
    print("4. Sair")
    
    opcao = input("Digite o número da opção desejada: ") 
    
    if opcao == "1":
        nova_tarefa = input("Qual é a nova tarefa? ")
        tarefas.append(nova_tarefa)
        print(f"✅ Tarefa '{nova_tarefa}' adicionada com sucesso!")
    elif opcao == "2":
        print("\n📋 Lista de Tarefas:")
        if len(tarefas) == 0:
            print("Você não tem tarefas pendentes. Tudo em dia!")
        else:
            for indice, tarefa in enumerate(tarefas):
                print(f"{indice + 1}. {tarefa}")
        print("=====================================")
    elif opcao == "3":
        if len(tarefas) == 0:
            print("Não há tarefas para concluir ou remover.")
        else:
            numero_str = input("Digite o número da tarefa que deseja concluir/remover: ")
            try:
                numero = int(numero_str)
                if 1 <= numero <= len(tarefas):
                    tarefa_removida = tarefas.pop(numero - 1)
                    print(f"✅ Tarefa '{tarefa_removida}' concluída/removida com sucesso!")
                else:
                    print("Número inválido. Por favor, tente novamente.")
            except ValueError:
                print("Por favor, digite um número válido.")
    elif opcao == "4":
        print("Saindo do sistema de tarefas. Até a próxima!")
        break
    else:
        print("Opção inválida. Por favor, tente novamente.")