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
            valor