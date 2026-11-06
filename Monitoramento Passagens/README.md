# ✈️ SkyPatterns: Analisador e Monitor de Padrões de Passagens Aéreas

Um sistema interativo desenvolvido em Python para análise estatística de séries temporais de preços de passagens aéreas, permitindo calcular tendências de mercado, identificar o melhor dia da semana para voar e detetar promoções reais com base em desvios estatísticos.

---

## 🚀 Funcionalidades

- **🔀 Rotas Dinâmicas:** Permite ao utilizador definir qualquer aeroporto de origem e destino diretamente no terminal para análise personalizada.
- **📊 Análise Estatística Avançada:** Cálculo de médias móveis (7 e 30 dias), desvio padrão e aplicação de **Z-Score** para identificar desvios anômalos de preço no mercado.
- **📅 Padrão por Dia da Semana:** Identifica estatisticamente quais dias da semana apresentam as médias de preços mais baratas para a rota escolhida.
- **🤖 Diagnóstico e Recomendação de Compra:** O sistema avalia automaticamente se o preço atual está abaixo da média e emite um alerta de compra ("COMPRE AGORA" ou "AGUARDE").

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Pandas:** Manipulação e agregação de dados em DataFrames.
- **NumPy:** Computação numérica e simulação de modelos estatísticos e ruídos de mercado.

---

## 📦 Como Executar o Projeto

### Pré-requisitos
Certifica-te de que tens o **Python** instalado na tua máquina, juntamente com as bibliotecas necessárias.

1. **Clona o repositório:**
   ```bash
   git clone [https://github.com/yasmin026/Python.git](https://github.com/yasmin026/Python.git)
   cd Python