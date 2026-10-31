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