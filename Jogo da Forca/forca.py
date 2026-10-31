import os 
import random

ESTAGIOS_BONECO = [
    """
       +---+
       |   |
           |
           |
           |
           |
    =========""",
    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========""",
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========""",
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========""",
    """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
    =========""",
    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========""",
    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========""",
]

PALAVRAS = [
    "PYTHON",
    "DESENVOLVIMENTO",
    "PROGRAMACAO",
    "ALGORITMO",
    "VARIAVEL",
    "TERMINAL",
    "REQUISICAO",
    "INTERFACE",
]

def limpar_tela():
    os.system ("cls" if os.name == "nt" else "clear")
    
def jogar():
    palavra_secreta = random.choice(PALAVRAS).upper()
    letras_descobertas = ["_"] * len(palavra_secreta)
    letras_tentadas = set()
    erros = 0
    max_erros = len(ESTAGIOS_BONECO) - 1
    
    while erros < max_erros and "_" in letras_descobertas:
        limpar_tela()
        print("=== JOGO DA FORCA EM PYTHON ===")
        print(ESTAGIOS_BONECO[erros])
        
        print("\nPalavra: " + " ".join(letras_descobertas))
        print(
            f"Letras já tentadas: {', '.join(sorted(letras_tentadas)) if letras_tentadas else 'Nenhuma'}"
        )
        print(f"Tentativas restantes: {max_erros - erros}")

        palpite = input("\nDigite uma letra: ").strip().upper()
        
        #Validação de Entrada
        if len(palpite) != 1 or not palpite.isalpha():
            print("\n[Erro] Digite apenas uma única letra!")
            input("Pressione Enter para continuar...")
            continue
        
        if palpite in letras_tentadas:
            print(f"\nVocê já tentou a letra '{palpite}'!")
            input("Pressione Enter para continuar...")
            continue
        
        letras_tentadas.add(palpite)
        
        #Checa se as letras existe na palavra
        if palpite in palavra_secreta:
            for i, letra in enumerate(palavra_secreta):
                if letra == palpite:
                    letras_descobertas[i] = palpite
        else:
            erros += 1
    #Tela Final
    limpar_tela()    
    print(ESTAGIOS_BONECO[erros])
    
    if "_" not in letras_descobertas:
        print ("\n🎉 PARABÉNS! Você venceu!")
        print(f"A palavra era: {palavra_secreta}")
    else:
        print("\n☠️ GAME OVER! Você foi enforcado...")
        print(f"A palavra correta era: {palavra_secreta}")
        
if __name__ == "__main__":
    jogar()
    
    
#Deu Certo