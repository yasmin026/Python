import random

print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = random.randint(1, 100)
tentativas = 0
acertou = False

while not acertou:
    chute_str = input("Digite um número entre 1 e 100: ")
    chute = int(chute_str)
    tentativas += 1

    if chute == numero_secreto:
        print(f"🎉 Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas!")
        acertou = True

    elif chute < numero_secreto:
        print("O número secreto é MAIOR. Tente de novo.\n")
    else:
        print("O número secreto é MENOR. Tente de novo.\n")
print("Fim do jogo. Obrigado por jogar!")
    
    