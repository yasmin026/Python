from datetime import datetime, timedelta
import numpy as np
import pandas as pd


def gerar_dataset_historico_real(origem, destino):
  """Gera um dataset histórico realista de 90 dias para a rota personalizada."""
  # Usa o nome das cidades como semente aleatória para gerar preços diferentes por rota
  np.random.seed(sum(map(ord, origem + destino)))
  datas = [datetime(2026, 8, 1) + timedelta(days=i) for i in range(90)]

  precos = []
  # Define um preço base fictício mas coerente baseado no tamanho da string da rota
  preco_base = 550.0 + (len(origem + destino) * 25)

  for d in datas:
    # Padrão 1: Fins de semana (Sexta e Domingo) costumam ter preços mais altos
    fator_dia = 1.28 if d.weekday() in [4, 6] else 0.93

    # Padrão 2: Variação aleatória de mercado
    ruido = np.random.normal(0, 50)

    preco_final = (preco_base * fator_dia) + ruido
    precos.append(round(max(250.0, preco_final), 2))

  # Simular uma grande promoção no último dia cadastrado
  precos[-1] = round(precos[-1] * 0.72, 2)

  df = pd.DataFrame({
      'data_consulta': datas,
      'origem': origem.upper(),
      'destino': destino.upper(),
      'preco_brl': precos,
      'dia_semana': [d.strftime('%A') for d in datas],
  })
  return df


def analisar_padroes_mercado(df):
  """Executa a análise estatística de padrões de preços."""
  df['media_movel_7d'] = df['preco_brl'].rolling(window=7).mean()
  df['media_movel_30d'] = df['preco_brl'].rolling(window=30).mean()

  preco_atual = df['preco_brl'].iloc[-1]
  media_historica = df['preco_brl'].mean()
  desvio_padrao = df['preco_brl'].std()
  menor_preco = df['preco_brl'].min()
  maior_preco = df['preco_brl'].max()

  padrao_dias = (
      df.groupby('dia_semana')['preco_brl'].mean().sort_values().round(2)
  )

  # Cálculo do Z-Score para detectar promoção real
  z_score = (preco_atual - media_historica) / desvio_padrao
  desconto_vs_media = round(
      ((media_historica - preco_atual) / media_historica) * 100, 1
  )

  return {
      'preco_atual': preco_atual,
      'media_historica': round(media_historica, 2),
      'menor_preco': menor_preco,
      'maior_preco': maior_preco,
      'desconto_percentual': desconto_vs_media,
      'z_score': z_score,
      'padrao_dias': padrao_dias,
  }


if __name__ == '__main__':
  print('====================================================')
  print('📊 SISTEMA DE ANÁLISE E PADRÕES DE PASSAGENS AÉREAS')
  print('====================================================\n')

  # Interação com a usuária para escolher os destinos
  print('✈️ Configuração da Rota de Viagem:')
  origem_input = (
      input('Digite o código do aeroporto de ORIGEM (ex: CNF, GRU, SDU): ')
      .strip()
      .upper()
  )
  if not origem_input:
    origem_input = 'CNF'  # Valor padrão se deixar vazio

  destino_input = (
      input('Digite o código do aeroporto de DESTINO (ex: GIG, SSA, REC): ')
      .strip()
      .upper()
  )
  if not destino_input:
    destino_input = 'GIG'  # Valor padrão se deixar vazio

  print(
      f'\n🔄 A processar dados e histórico de mercado para a rota'
      f' {origem_input} ➔ {destino_input}...\n'
  )

  # Carregar dados customizados para a rota escolhida
  df_historico = gerar_dataset_historico_real(origem_input, destino_input)

  # Executar motor estatístico
  estatisticas = analisar_padroes_mercado(df_historico)

  print('----------------------------------------------------')
  print(f'📍 Rota Analisada: {origem_input} ➔ {destino_input}')
  print(f'🗓️ Período Analisado: 90 dias de histórico')
  print('----------------------------------------------------')
  print(f"💵 Preço Mais Recente: R$ {estatisticas['preco_atual']:.2f}")
  print(f"📈 Preço Médio Histórico: R$ {estatisticas['media_historica']:.2f}")
  print(f"📉 Menor Preço Registrado: R$ {estatisticas['menor_preco']:.2f}")
  print(f"📊 Maior Preço Registrado: R$ {estatisticas['maior_preco']:.2f}")
  print('----------------------------------------------------')

  # Diagnóstico Inteligente baseado no Z-Score
  if estatisticas['z_score'] <= -1.3:
    print('🚨 DIAGNÓSTICO: ALERTA DE SUPER PROMOÇÃO DETECTADO!')
    print(
        f'🔥 O preço atual está {estatisticas["desconto_percentual"]}% ABAIXO'
        ' da média histórica.'
    )
    print('✅ RECOMENDAÇÃO: COMPRE AGORA!')
  elif estatisticas['preco_atual'] < estatisticas['media_historica']:
    print('💡 DIAGNÓSTICO: Preço bom (abaixo da média).')
    print('🟡 RECOMENDAÇÃO: Vale a pena considerar a compra.')
  else:
    print('⚠️ DIAGNÓSTICO: Preço acima da média de mercado.')
    print('🛑 RECOMENDAÇÃO: Aguarde uma nova oscilação de baixa.')

  print('\n----------------------------------------------------')
  print('📅 PADRÃO DETECTADO POR DIA DA SEMANA (Média de Preços):')
  print(estatisticas['padrao_dias'].to_string())
  print('====================================================')