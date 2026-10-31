import os
import shutil
from pathlib import Path

# Mapeamento de categorias e suas respectivas extensões
CATEGORIAS = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp", ".psd", ".ai"],
    "Documentos": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".csv"],
    "Codigos": [".py", ".html", ".css", ".js", ".php", ".json", ".sql", ".java"],
    "Compactados": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Instaladores": [".exe", ".msi", ".apk"],
    "Audios_Videos": [".mp3", ".wav", ".mp4", ".mkv", ".avi"]
}
def organizar_pasta(caminho_pasta):
    pasta_target = Path(caminho_pasta)

    # Valida se o caminho informado existe
    if not pasta_target.exists():
        print(f"\n[Erro] O caminho '{caminho_pasta}' não foi encontrado!")
        return

    print(f"\n📁 Organizando a pasta: {pasta_target.resolve()}\n")
    arquivos_movidos = 0

    # Percorre todos os itens da pasta
    for item in pasta_target.iterdir():
        # Ignora diretórios (pastas), processando apenas arquivos
        if item.is_dir():
            continue

        extensao = item.suffix.lower()
        pasta_destino_nome = "Outros"

        # Identifica a categoria correspondente pela extensão
        for categoria, extensoes in CATEGORIAS.items():
            if extensao in extensoes:
                pasta_destino_nome = categoria
                break
            
            
    # Cria a pasta de destino se ela ainda não existir
        pasta_destino = pasta_target / pasta_destino_nome
        pasta_destino.mkdir(exist_ok=True)

        # Move o arquivo para a nova pasta
        caminho_destino_arquivo = pasta_destino / item.name
        
        # Evita sobrescrever arquivos com o mesmo nome
        if not caminho_destino_arquivo.exists():
            shutil.move(str(item), str(caminho_destino_arquivo))
            print(f"➜ Movido: {item.name} ➔ [{pasta_destino_nome}]")
            arquivos_movidos += 1
        else:
            print(f"⚠️ Ignorado (já existe na pasta de destino): {item.name}")

    print(f"\n✨ Concluído! Total de {arquivos_movidos} arquivos organizados.")

if __name__ == "__main__":
    print("=== ORGANIZADOR AUTOMÁTICO DE ARQUIVOS ===")
    
    