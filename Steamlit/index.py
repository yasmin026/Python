from datetime import datetime
import os
import pandas as pd
import streamlit as st

# Configuração da página (deve ser a primeira linha do Streamlit)
st.set_page_title="Financify | Controle Financeiro"
st.set_page_config(
    page_title="Financify", page_icon="💰", layout="wide", initial_sidebar_state="expanded"
)

# Arquivo local para salvar os dados
ARQUIVO_DADOS = "dados_financas.csv"


def carregar_dados():
    if os.path.exists(ARQUIVO_DADOS):
        return pd.read_csv(ARQUIVO_DADOS)
    else:
        # Cria um DataFrame vazio caso o arquivo não exista
        return pd.DataFrame(
            columns=["Data", "Tipo", "Categoria", "Valor", "Descricao"]
        )


def salvar_dados(df):
    df.to_csv(ARQUIVO_DADOS, index=False)


# Carrega os dados existentes
df_transacoes = carregar_dados()

# --- BARRA LATERAL (MENU E CADASTRO) ---
st.sidebar.title("💰 Financify")
st.sidebar.markdown("Gerencie suas finanças de forma simples.")

st.sidebar.markdown("---")
st.sidebar.subheader("➕ Nova Transação")

tipo = st.sidebar.selectbox("Tipo", ["Receita", "Despesa"])
categoria = st.sidebar.selectbox(
    "Categoria",
    [
        "Salário",
        "Freelance",
        "Alimentação",
        "Moradia",
        "Transporte",
        "Lazer",
        "Outros",
    ],
)
valor = st.sidebar.number_input(
    "Valor (R$)", min_value=0.01, format="%.2f", step=10.0
)
descricao = st.sidebar.text_input("Descrição (Opcional)")

if st.sidebar.button("Adicionar Transação", type="primary"):
    nova_linha = pd.DataFrame(
        [
            {
                "Data": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "Tipo": tipo,
                "Categoria": categoria,
                "Valor": valor,
                "Descricao": descricao if descricao else "-",
            }
        ]
    )

    df_transacoes = pd.concat([df_transacoes, nova_linha], ignore_index=True)
    salvar_dados(df_transacoes)
    st.sidebar.success("Transação adicionada com sucesso!")
    st.rerun()

# --- TELA PRINCIPAL (DASHBOARD) ---
st.title("📊 Painel de Controle Financeiro")
st.markdown("Acompanhe suas entradas, saídas e saúde financeira em tempo real.")

if df_transacoes.empty:
    st.info(
        "👋 Nenhuma transação cadastrada ainda. Use a barra lateral à esquerda para adicionar sua primeira receita ou despesa!"
    )
else:
    # Cálculos dos totais
    total_receitas = df_transacoes[df_transacoes["Tipo"] == "Receita"][
        "Valor"
    ].sum()
    total_despesas = df_transacoes[df_transacoes["Tipo"] == "Despesa"][
        "Valor"
    ].sum()
    saldo_total = total_receitas - total_despesas

    # Exibição de Métricas (Cartões no topo)
    col1, col2, col3 = st.columns(3)
    col1.metric("Total de Receitas", f"R$ {total_receitas:,.2f}")
    col2.metric("Total de Despesas", f"R$ {total_despesas:,.2f}")

    # Cor dinâmica para o saldo (verde se positivo, vermelho se negativo)
    col3.metric(
        "Saldo Atual",
        f"R$ {saldo_total:,.2f}",
        delta=f"R$ {saldo_total:,.2f}",
        delta_color="normal" if saldo_total >= 0 else "inverse",
    )

    st.markdown("---")

    # Gráficos e Tabelas
    col_tabela, col_grafico = st.columns([2, 1])

    with col_tabela:
        st.subheader("📋 Histórico de Transações")
        # Mostra a tabela formatada
        st.dataframe(df_transacoes, use_container_width=True)

        # Botão para limpar dados de teste
        if st.button("🗑️ Limpar Todos os Dados"):
            if os.path.exists(ARQUIVO_DADOS):
                os.remove(ARQUIVO_DADOS)
            st.rerun()

    with col_grafico:
        st.subheader("📉 Despesas por Categoria")
        df_despesas = df_transacoes[df_transacoes["Tipo"] == "Despesa"]

        if not df_despesas.empty:
            # Agrupa por categoria para o gráfico
            despesas_por_cat = df_despesas.groupby("Categoria")[
                "Valor"
            ].sum()
            st.bar_chart(despesas_por_cat)
        else:
            st.write("Nenhuma despesa registrada para exibir no gráfico.")
            