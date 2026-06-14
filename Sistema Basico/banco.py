print("=====================================")
print("              BANCO PYTHON           ")
print("=====================================")

saldo = 0.0
extrato = []

while True:
    print("\nEscolha uma opção:")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Ver extrato")
    print("4 - Sair")
    
    opcao = input("Digite a opção desejada: ")
    if opcao == '1':
        try:
            valor = float(input("Digite o valor do depósito: "))
            if valor >0:
                saldo += valor
                extrato.append(f"+ Depósito: R$ {valor:.2f}")
                print("✅ Depósito realizado com sucesso!")
            else:
                print("❌ Valor inválido. O depósito deve ser maior que zero.")
        except ValueError:
            print("❌ Entrada inválida. Por favor, digite um número válido.")
    elif opcao == '2':
        try:
            valor = float(input("Digite o valor do saque:R$"))
            if valor > 0:
                    if valor <= saldo:
                        saldo -= valor
                        extrato.append(f"- Saque: R$ {valor:.2f}")
                        print("✅ Saque realizado com sucesso! Retire seu dinheiro.")
                    else:
                        print("❌ Saldo insuficiente para este saque.")
            else:
                    print("❌ O valor deve ser maior que zero.")
        except ValueError:
                print("❌ Valor inválido! Digite apenas números.")   
    elif opcao == '3':
        print("\n--- EXTRATO BANCÁRIO ---")
        if len(extrato) == 0:
            print("Nenhuma movimentação realizada hoje.")
        else:
            for movimento in extrato:
                print(movimento)
        print("------------------------")

    elif opcao == '4':
        print("Obrigado por usar o Banco Python. Até logo!")
        break

    else:
        print("❌ Opção inválida! Digite 1, 2, 3 ou 4.") 