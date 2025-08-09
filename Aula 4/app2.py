import streamlit as st
import pandas as pd
#import seaborn as sns
import matplotlib.pyplot as plt

# Dados de exemplo
df = pd.DataFrame({
    'Segmento': ['Logística', 'Shopping', 'Escritório'],
    'FFO_Yield': [0.06, 0.07, 0.05],
    'Dividend_Yield': [0.05, 0.065, 0.045]
})

# Transformar em formato longo
df_melted = df.melt(id_vars='Segmento', 
                    value_vars=['FFO_Yield', 'Dividend_Yield'],
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