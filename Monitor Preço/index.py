from datetime import datetime
from bs4 import BeautifulSoup
import requests


def verificar_preco_produto(url, seletor_css, preco_desejado):
  # Headers para simular um navegador real e evitar bloqueios básicos de bot
  headers = {
      'User-Agent': (
          'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
          ' (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
      ),
      'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
  }

  print(f'🔍 A aceder à página do produto...')

  try:
    resposta = requests.get(url, headers=headers)
    if resposta.status_code != 200:
      print(
          f'❌ Erro ao aceder à página. Código de estado:'
          f' {resposta.status_code}'
      )
      return None

    # Parse do HTML com BeautifulSoup
    soup = BeautifulSoup(resposta.text, 'html.parser')

    # Encontra o elemento do preço com base no seletor CSS da página
    elemento_preco = soup.select_one(seletor_css)

    if not elemento_preco:
      print('❌ Não foi possível encontrar o elemento do preço na página.')
      print(
          'Dica: Os sites costumam mudar as classes HTML com frequência ou'
          ' exigir JavaScript.'
      )
      return None

    # Limpeza da string de preço (ex: "R$ 1.999,00" -> 1999.00)
    preco_texto = (
        elemento_preco.get_text()
        .replace('R$', '')
        .replace('$', '')
        .replace('.', '')
        .replace(',', '.')
        .strip()
    )

    preco_atual = float(preco_texto)
    print(f'💵 Preço atual encontrado: R$ {preco_atual:.2f}')

    # Verificação de Alerta
    if preco_atual <= preco_desejado:
      print(
          f'🚨 ALERTA: O preço atingiu o valor desejado (<= R$'
          f' {preco_desejado:.2f})!'
      )
      enviar_alerta_telegram(
          f'🔥 PROMOÇÃO DETECTADA!\nPreço atual: R$ {preco_atual:.2f}\nLink:'
          f' {url}'
      )
    else:
      print(
          'ℹ️ O preço ainda está acima do valor desejado. A aguardar novas'
          ' baixas.'
      )

    return preco_atual

  except Exception as e:
    print(f'❌ Ocorreu um erro durante o scraping: {e}')
    return None


def enviar_alerta_telegram(mensagem):
  """Função responsável por enviar a mensagem de alerta para o teu Telegram."""
  # Substituir pelo teu Token do Bot (criado através do @BotFather no Telegram)
  TOKEN = 'SEU_BOT_TOKEN_AQUI'
  # Substituir pelo teu Chat ID (obtido através do @userinfobot)
  CHAT_ID = 'SEU_CHAT_ID_AQUI'

  url_api = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
  payload = {'chat_id': CHAT_ID, 'text': mensagem}

  try:
    resposta = requests.post(url_api, json=payload)
    if resposta.status_code == 200:
      print('📲 Alerta enviado com sucesso para o Telegram!')
    else:
      print(f'❌ Erro ao enviar mensagem no Telegram: {resposta.text}')
  except Exception as e:
    print(f'❌ Erro de conexão com a API do Telegram: {e}')


if __name__ == '__main__':
  print('====================================================')
  print('🤖 WEB SCRAPER MONITOR DE PREÇOS COM TELEGRAM')
  print('====================================================\n')

  # Exemplo de parâmetros (podes substituir por um link real de e-commerce)
  URL_EXEMPLO = 'https://httpbin.org/html'  # URL de teste para começar
  SELETOR_CSS_EXEMPLO = 'h1'  # Seletor de exemplo
  MEU_PRECO_ALVO = 100.00

  verificar_preco_produto(URL_EXEMPLO, SELETOR_CSS_EXEMPLO, MEU_PRECO_ALVO)