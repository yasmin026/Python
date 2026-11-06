from datetime import datetime
import re
import time
from bs4 import BeautifulSoup
import cloudscraper  # Substitui o requests para driblar o bloqueio 403
import schedule


def verificar_preco_produto(url, seletor_css, preco_desejado):
  print(
      f'\n[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] 🔍 A aceder à página'
      f' do produto...'
  )

  try:
    # Cria um scraper inteligente que contorna barreiras anti-bot (Cloudflare 403)
    scraper = cloudscraper.create_scraper(
        browser={'browser': 'chrome', 'platform': 'windows', 'desktop': True}
    )

    resposta = scraper.get(url, timeout=20)
    if resposta.status_code != 200:
      print(
          f'❌ Erro ao aceder à página. Código de estado:'
          f' {resposta.status_code}'
      )
      return

    soup = BeautifulSoup(resposta.text, 'html.parser')
    elemento_preco = soup.select_one(seletor_css)

    if not elemento_preco:
      print(
          '❌ Não foi possível encontrar o elemento do preço com o seletor'
          f' fornecido: "{seletor_css}"'
      )
      print(
          'Dica: O site pode carregar o preço via JavaScript. Verifique se o'
          ' seletor está correto.'
      )
      return

    texto_extraido = elemento_preco.get_text().strip()

    # Expressão regular para extrair valores numéricos de preço
    match_preco = re.search(r'[\d.,]+', texto_extraido.replace('R$', ''))

    if not match_preco:
      print(
          '❌ O elemento encontrado não contém um formato numérico de preço'
          f' válido. Texto lido: "{texto_extraido}"'
      )
      return

    preco_texto = (
        match_preco.group(0)
        .replace('.', '')
        .replace(',', '.')
        .strip()
    )
    preco_atual = float(preco_texto)

    print(f'💵 Preço atual encontrado no site: R$ {preco_atual:.2f}')
    print(f'🎯 O seu preço-alvo desejado: R$ {preco_desejado:.2f}')

    # Verificação de Alerta
    if preco_atual <= preco_desejado:
      print(
          f'🚨 ALERTA: O preço atingiu ou ficou abaixo do valor desejado!'
      )
      enviar_alerta_telegram(
          f'🔥 PROMOÇÃO DETECTADA!\n💵 Preço Atual: R$'
          f' {preco_atual:.2f}\n🎯 Meta: R$ {preco_desejado:.2f}\n🔗 Link:'
          f' {url}'
      )
    else:
      print(
          'ℹ️ O preço ainda está acima da meta. A aguardar próximas'
          ' verificações.'
      )

  except Exception as e:
    print(f'❌ Ocorreu um erro durante a requisição ou scraping: {e}')


def enviar_alerta_telegram(mensagem):
  """Função responsável por enviar a mensagem de alerta para o Telegram."""
  import requests

  TOKEN = 'SEU_BOT_TOKEN_AQUI'
  CHAT_ID = 'SEU_CHAT_ID_AQUI'

  url_api = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
  payload = {'chat_id': CHAT_ID, 'text': mensagem}

  try:
    resposta = requests.post(url_api, json=payload, timeout=10)
    if resposta.status_code == 200:
      print('📲 Alerta enviado com sucesso para o Telegram!')
    else:
      print(f'❌ Erro ao enviar mensagem no Telegram: {resposta.text}')
  except Exception as e:
    print(f'❌ Erro de conexão com a API do Telegram: {e}')


if __name__ == '__main__':
  print('====================================================')
  print('🤖 WEB SCRAPER MONITOR DE PREÇOS COM TELEGRAM E AGENDAMENTO')
  print('====================================================\n')

  url_produto = input('🔗 Cole o link (URL) do produto que deseja monitorar: ').strip()
  seletor_css_produto = input(
      '🏷️ Digite o Seletor CSS do preço (ex: span.price-tag, .product-price): '
  ).strip()
  preco_alvo = float(
      input('💰 Digite o valor máximo que deseja pagar (ex: 150.00): ').strip()
  )

  print(
      '\n✅ Produto configurado com sucesso! O sistema iniciará o'
      ' monitoramento automático.'
  )
  print(
      'Pressione CTRL+C no terminal a qualquer momento para interromper o'
      ' programa.\n'
  )

  # Verificação imediata
  verificar_preco_produto(url_produto, seletor_css_produto, preco_alvo)

  # Agendamento periódico
  schedule.every(1).hours.do(
      verificar_preco_produto, url_produto, seletor_css_produto, preco_alvo
  )

  while True:
    schedule.run_pending()
    time.sleep(1)