import requests

def convert_moeda():
    print("=== CONVERSOR DE MOEDAS EM PYTHON ===")
    print("Exemplos de moedas: USD, BRL, EUR, GBP, BTC, ARS\n")
    
    #Entrada de Dados
    moeda_origem = input(
        "Digite a moeda de origem (ex: USD): "
    ).upper().strip()
    moeda_destino = input(
        "Digite a moeda de destino (ex: BRL): "
    ).upper().strip()
    
    try:
        valor = float(input(f"Digite o valor em {moeda_origem} que deseja converter: "))
    except ValueError:
        print("\n[Erro] Valor inválido! Digite apenas números.")
        return
    
    par_moedas = f"{moeda_origem}-{moeda_destino}"
    url = f"https://economia.awesomeapi.com.br/json/last/{par_moedas}"
    
    try:
        resposta = requests.get(url)
        dados = resposta.json()
        
        chave_json = moeda_origem + moeda_destino
        
        if chave_json in dados:
            cotacao = float(dados[chave_json]["bid"])
            nome_par = dados[chave_json]["name"]
            valor_convertido = valor * cotacao
            
            print("\n----------------------------------------")
            print(f"Cotação atual ({nome_par}): R$ {cotacao:.4f}")
            print(
                f"Valor convertido: {moeda_origem} {valor:.2f} = {moeda_destino} {valor_convertido:.2f}"
            )
            print("----------------------------------------")
        else:
            print(
                f"\n[Erro] Não foi encontrada cotação para o par {par_moedas}."
            )
    except requests.exceptions.RequestException:
        print(
            "\n[Erro] Falha de conexão com a internet ou serviço indisponível."
        )
if __name__ == "__main__":
    convert_moeda()   
    