from datetime import datetime, timedelta
import numpy as np
import pandas as pd


def gerar_dataset_historico_real():
  """Gera um dataset histórico realista de 90 dias de consultas de voos

  CNF (Belo Horizonte) -> GIG (Rio de Janeiro).
  """
  np.random.seed(42)  # Garante resultados consistentes
  datas = [datetime(2026, 8, 1) + timedelta(days=i) for i in range(90)]

  precos = []
  preco_base = 650.0

  for d in datas:
    # Padrão 1: Fins de semana (Sexta e Domingo) costumam ter preços mais altos
    fator_dia = 1.25 if d.weekday() in [4, 6] else 0.95

    # Padrão 2: Variação aleatória do mercado
    ruido = np.random.normal(0, 45)

    preco_final = (preco_base * fator_dia) + ruido
    precos.append(round(max(280.0, preco_final), 2))

  # Simular uma grande promoção no último dia cadastrado
  precos[-1] = 345.00

  df = pd.DataFrame({
      'data_consulta': datas,
      'origem': 'CNF',
      'destino': 'GIG',
      'preco_brl': precos,
      'dia_semana': [d.strftime('%A') for d in datas],
  })
  return df


def analisar_padroes_mercado(df):
  """Executa a análise estatística de padrões de preços."""
  # 1. Calcular Média Móvel de 7 e 30 dias
  df['media_movel_7d'] = df['preco_brl'].rolling(window=7).mean()
  df['media_movel_30d'] = df['preco_brl'].rolling(window=30).mean()

  # 2. Dados do momento atual (última consulta)
  preco_atual = df['preco_brl'].iloc[-1]
  media_historica = df['preco_brl'].mean()
  desvio_padrao = df['preco_brl'].std()
  menor_preco = df['preco_brl'].min()
  maior_preco = df['preco_brl'].max()

  # 3. Análise do melhor dia da semana (Padrão de Viagem)
  padrao_dias = (
      df.groupby('dia_semana')['preco_brl'].mean().sort_values().round(2)
  )

  # 4. Cálculo do Z-Score para detectar promoção real
  # (Z-Score < -1.5 indica que o preço está muito abaixo da média normal)
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

  # Carregar dados
  df_historico = gerar_dataset_historico_real()

  # Executar motor estatístico
  estatisticas = analisar_padroes_mercado(df_historico)

  print(
      f"📍 Rota Analisada: {df_historico['origem'].iloc[0]} ➔"
      f" {df_historico['destino'].iloc[0]}"
  )
  print(f"🗓️ Período do Histórico: 90 dias de dados acumulados")
  print('----------------------------------------------------')
  print(f"💵 Preço Mais Recente: R$ {estatisticas['preco_atual']:.2f}")
  print(f"📈 Preço Médio Histórico: R$ {estatisticas['media_historica']:.2f}")
  print(f"📉 Menor Preço Registrado: R$ {estatisticas['menor_preco']:.2f}")
  print(f"📊 Maior Preço Registrado: R$ {estatisticas['maior_preco']:.2f}")
  print('----------------------------------------------------')

  # Diagnóstico Inteligente baseando-se no Z-Score
  if estatisticas['z_score'] <= -1.5:
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