import random

print("*********************************")
print("Bem vindo ao jogo de Jokenpô!")
print("*********************************")

opcoes = ["pedra", "papel", "tesoura"]
pontos_jogador = 0
pontos_computador = 0

while True:
    print(f"\n--- PLACAR: Você {pontos_jogador} x {pontos_computador} Computador ---")
    jogada = input("Escolha pedra, papel ou tesoura (ou 'sair' para encerrar): ").lower()
    
    if jogada == "sair":
        print("Obrigado por jogar! Até a próxima!")
        break
    if jogada not in opcoes:
        print("Opção inválida. Por favor, escolha pedra, papel ou tesoura.")
        continue
    
    escolha_computador = random.choice(opcoes)
    print(f"\n🤖 O computador escolheu: {escolha_computador.upper()}")
    if jogada == escolha_computador:
        print("Empate! Ninguém pontua.")
        
    elif (jogada == "pedra" and escolha_computador == "tesoura") or \
            (jogada == "papel" and escolha_computador == "pedra") or \
            (jogada == "tesoura" and escolha_computador == "papel"):
        print("🎉 Você ganhou esta rodada!")
        pontos_jogador += 1
    else:
        print("😔 Você perdeu esta rodada!")
        pontos_computador += 1