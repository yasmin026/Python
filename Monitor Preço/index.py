from datetime import datetime
from bs4 import BeautifulSoup
import requests
import re


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
      return None

    texto_extraido = elemento_preco.get_text().strip()
    print(f'📄 Texto bruto encontrado no HTML: "{texto_extraido}"')

    # Expressão regular para extrair apenas números, pontos e vírgulas de preço
    # (Ex: procura por padrões como 1.999,00 ou 199.90)
    match_preco = re.search(r'[\d.,]+', texto_extraido.replace('R$', ''))

    if not match_preco:
      print(
          '❌ O elemento encontrado não contém um formato numérico de preço'
          ' válido.'
      )
      return None

    preco_texto = (
        match_preco.group(0)
        .replace('.', '')
        .replace(',', '.')
        .strip()
    )

    preco_atual = float(preco_texto)
    print(f'💵 Preço atual convertido: R$ {preco_atual:.2f}')

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
  TOKEN = 'SEU_BOT_TOKEN_AQUI'
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

  # Para testar sem erros de texto, podes usar um site real de testes de scraping
  # ou um link onde o seletor aponte para um valor numérico.
  URL_EXEMPLO = 'https://httpbin.org/html'
  # Vamos usar uma tag de teste ou podes colocar o link e seletor da tua loja favorita
  SELETOR_CSS_EXEMPLO = 'h1'
  MEU_PRECO_ALVO = 100.00

  verificar_preco_produto(URL_EXEMPLO, SELETOR_CSS_EXEMPLO, MEU_PRECO_ALVO)