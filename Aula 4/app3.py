import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 📥 Função para carregar os dados
@st.cache_data
def carregar_dados(caminho):
    return pd.read_csv(caminho)

# 📊 Função para filtrar os dados
def filtrar_segmentos(df, segmentos):
    return df[df['Segmento'].isin(segmentos)]

# 📈 Função para gerar gráfico de indicadores
def grafico_indicadores(df, tipo):
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.set_palette("Set2")
    if tipo == 'Barra':
        sns.barplot(data=df, x='Segmento', y='Valor', hue='Indicador', ax=ax)
    else:
        sns.lineplot(data=df, x='Segmento', y='Valor', hue='Indicador', marker='o', ax=ax)
    ax.set_title("Indicadores por Segmento")
    ax.set_ylabel("Valor")
    ax.set_xlabel("Segmento")
    plt.xticks(rotation=45)
    return fig

# 📊 Função para gráfico de valor de mercado
def grafico_valor_mercado(df):
    media_segmento = df.groupby('Segmento')['Valor de Mercado'].mean().reset_index()
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.bar(media_segmento['Segmento'], media_segmento['Valor de Mercado'], color='orange')
    ax.set_title("Valor de Mercado dos Fundos Imobiliários do IFIX")
    ax.set_ylabel("Valor")
    ax.set_xlabel("Segmento")
    plt.xticks(rotation=45)
    return fig, media_segmento

# 🚀 Início do app
st.set_page_config(page_title="Dashboard FII", layout="wide")
st.title("📈 Dashboard de Fundos Imobiliários")

# 🔄 Carregar dados
caminho = "https://raw.githubusercontent.com/CarlosLaud/dashboard-streamlit/refs/heads/main/Aula%204/df_novo.csv"
df = carregar_dados(caminho)

st.subheader("📊 Quantidades por Segmento")
df['Segmento'].value_counts().reset_index()

# 🔄 Transformar em formato longo
df_melted = df.melt(id_vars='Segmento', 
                    value_vars=['FFO Yield', 'Dividend Yield'],
                    var_name='Indicador', 
                    value_name='Valor')

# 🎛️ Layout com colunas
col1, col2 = st.columns(2)
with col1:
    segmentos = st.multiselect("Selecione os segmentos:", 
                               options=df_melted['Segmento'].unique(),
                               default=df_melted['Segmento'].unique())
with col2:
    tipo_grafico = st.radio("Tipo de gráfico:", ['Barra', 'Linha'])

# 🔍 Filtrar dados
df_filtrado = filtrar_segmentos(df_melted, segmentos)

# 📉 Gráfico de indicadores
st.subheader("📊 Indicadores por Segmento")
fig_indicadores = grafico_indicadores(df_filtrado, tipo_grafico)
st.pyplot(fig_indicadores)

# 📈 Métrica resumida
valor_medio = df_filtrado['Valor'].mean()
st.metric(label="Valor Médio dos Indicadores Selecionados", value=f"{valor_medio:.2f}")

# 📥 Botão para download
st.download_button("📥 Baixar dados filtrados", data=df_filtrado.to_csv(index=False), file_name="dados_filtrados.csv", mime="text/csv")

# 📄 Mostrar dados originais
st.subheader("📄 Dados Originais")
st.dataframe(df)

# 📊 Gráfico de valor de mercado
st.subheader("💰 Valor de Mercado por Segmento")
fig_valor, media_segmento = grafico_valor_mercado(df)
st.pyplot(fig_valor)



