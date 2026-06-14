print("=====================================")
print("Bem-vindo à sua agenda!")
print("=====================================")

contatos = {}

while True:
    print("\n--- MENU ---")
    print("1 - Adicionar ou Atualizar contato")
    print("2 - Buscar um contato")
    print("3 - Ver todos os contatos")
    print("4 - Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':
        nome = input("Digite o nome do contato: ").title()
        telefone = input("Digite o telefone do contato: ")
        
        contatos[nome] = telefone
        print(f"✅ Contato de {nome} salvo com sucesso!")
    elif opcao == '2':
        nome = input("Digite o nome do contato que deseja buscar: ").title()
        
        telefone = contatos.get(nome)
        if telefone:
            print(f"📞 O telefone de {nome} é: {telefone}")
        else:
            print(f"❌ Contato de {nome} não encontrado.")
    elif opcao == '3':
        print("\n--- MEUS CONTATOS ---")
        if len(contatos) == 0:
            print("Sua agenda está vazia.")
        else:
            for nome, telefone in contatos.items():
                print(f"👤 {nome} - 📱 {telefone}")
        print("----------------------")
    elif opcao == '4':
        print("Saindo da agenda. Até mais!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")