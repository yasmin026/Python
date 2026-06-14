import json
import os
ARQUIVO_BD ='estoque_loja.json'

def carregar_dados():
    if os.path.exists(ARQUIVO_BD):
        with open(ARQUIVO_BD, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    return []
def salvar_dados(dados):
    with open(ARQUIVO_BD, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)
def adicionar_produto(estoque):
    nome = input("Digite o nome do produto: ").title()
    try:
        quantidade = int(input(f"Quantidade de '{nome}' no estoque: "))
        preco = float(input(f"Preço unitário: R$ "))
        
        novo_produto = {"nome": nome, "quantidade": quantidade, "preco": preco}
        estoque.append(novo_produto)
        
        salvar_dados(estoque)
        print(f"✅ Produto '{nome}' cadastrado com sucesso!")
    except ValueError:
        print("❌ Erro: Digite números válidos para quantidade e preço.")

def listar_produtos(estoque):
    print("\n--- ESTOQUE ATUAL ---")
    if not estoque:
        print("O estoque está vazio.")
    else:
        for i, produto in enumerate(estoque):
            nome = produto['nome']
            qtd = produto['quantidade']
            preco = produto['preco']
            print(f"{i + 1}. {nome} | Qtd: {qtd} | Preço: R$ {preco:.2f}")
    print("---------------------")

def excluir_produto(estoque):
    listar_produtos(estoque)
    if estoque:
        try:
            indice = int(input("Digite o número do produto que deseja excluir: ")) - 1
            if 0 <= indice < len(estoque):
                removido = estoque.pop(indice)
                salvar_dados(estoque)
                print(f"🗑️ Produto '{removido['nome']}' excluído do sistema.")
            else:
                print("❌ Número não encontrado.")
        except ValueError:
            print("❌ Erro: Digite um número válido.")
 
meu_estoque = carregar_dados()
           
print("==================================")
print("📦 GERENCIADOR DE ESTOQUE  📦")
print("==================================")

while True:
    print("\nEscolha uma opção:")
    print("1. Adicionar produto")
    print("2. Listar produtos")
    print("3. Excluir produto")
    print("4. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':
        adicionar_produto(meu_estoque)
    elif opcao == '2':
        listar_produtos(meu_estoque)
    elif opcao == '3':
        excluir_produto(meu_estoque)
    elif opcao == '4':
        print("Saindo do sistema. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")