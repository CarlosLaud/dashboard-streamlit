import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#df = pd.read_csv("https://raw.githubusercontent.com/CarlosLaud/dashboard-streamlit/main/Aula%204/df_novo.csv")
#df = pd.read_csv("df_novo.csv")  # Coloque o arquivo no mesmo diretório do script

df = pd.read_csv("https://raw.githubusercontent.com/CarlosLaud/dashboard-streamlit/refs/heads/main/Aula%204/df_novo.csv")

# Transformar em formato longo
df_melted = df.melt(id_vars='Segmento', 
                    value_vars=['FFO Yield', 'Dividend Yield'],
                    var_name='Indicador', 
                    value_name='Valor')

# Título do dashboard
st.title("📈 Dashboard de Indicadores por Segmento")

# Filtros
segmentos = st.multiselect("Selecione os segmentos:", 
                           options=df_melted['Segmento'].unique(),
                           default=df_melted['Segmento'].unique())

tipo_grafico = st.radio("Tipo de gráfico:", ['Barra', 'Linha'])

# Filtrar dados
df_filtrado = df_melted[df_melted['Segmento'].isin(segmentos)]

# Criar gráfico
fig, ax = plt.subplots(figsize=(8, 5))

if tipo_grafico == 'Barra':
    sns.barplot(data=df_filtrado, x='Segmento', y='Valor', hue='Indicador', ax=ax)
else:
    sns.lineplot(data=df_filtrado, x='Segmento', y='Valor', hue='Indicador', marker='o', ax=ax)

ax.set_title("Indicadores por Segmento")
ax.set_ylabel("Valor")
ax.set_xlabel("Segmento")
st.pyplot(fig)


# import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Título do app
st.title("📊 Gráfico de Barras com Matplotlib")

media_segmento = df.groupby('Segmento')['Valor de Mercado'].mean().reset_index()

# Mostrar os dados
st.subheader("📄 Dados")
st.dataframe(df)

# Criar o gráfico
fig, ax = plt.subplots(figsize=(6, 4))  # Cria uma figura e um eixo
#ax.bar(df['Segmento'], df['Dividend Yield'], color='skyblue')  # Gráfico de barras
ax.bar(media_segmento['Segmento'], media_segmento['Valor de Mercado'], color='orange')


ax.set_title("Valor de Mercado dos Fundos Imobiliários do IFIX")  # Título do gráfico
ax.set_ylabel("Valor")  # Rótulo do eixo Y
ax.set_xlabel("Segmento")   # Rótulo do eixo X
ax.set_xticklabels(media_segmento['Segmento'], rotation=45)

#plt.xticks(rotation=45)

# Mostrar o gráfico no Streamlit
st.subheader("📈 Visualização")
st.pyplot(fig)

