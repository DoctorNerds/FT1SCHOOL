import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Configurações da página
st.set_page_config(
    page_title="Aula 03",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Carregar os dados do arquivo Excel
data_cronometragem = pd.read_excel('./data/cronometragem.xlsx')

# Definir as abas
tab1, tab2, tab3 = st.tabs(["Gráficos de linha", "Gráfico de dispersão", "Tabelas"])

with tab1:
    # Dividir a tela em duas colunas para seleções
    col1, col2 = st.columns(2)
    
    # Coluna 1: Multiselect para selecionar os carros
    with col1:
        carros_selecionados = st.multiselect(
            "Selecione os Carros:",
            options=data_cronometragem['Carro'].unique(),
            #default=data_cronometragem['Carro'].unique()[:5]  # Seleciona alguns carros como padrão
            key="carros_tab1"
        )

    # Coluna 2: Selectbox para selecionar a variável de interesse para o eixo Y
    with col2:
        variavel_y = st.selectbox(
            "Selecione a variável para o eixo Y:",
            options=['Setor 1', 'Setor 2', 'Setor 3', 'Tempo de volta'],
            key="variavel_y_tab1"
        )

    # Filtrar o DataFrame com os carros selecionados
    dados_filtrados = data_cronometragem[data_cronometragem['Carro'].isin(carros_selecionados)]

    # Plotar o gráfico de linha com Plotly
    fig = go.Figure()

    for carro in carros_selecionados:
        dados_carro = dados_filtrados[dados_filtrados['Carro'] == carro]
        fig.add_trace(go.Scatter(
            x=dados_carro['Volta'],
            y=dados_carro[variavel_y],
            mode='lines+markers',
            name=f'Carro {carro}'
        ))

    # Configurações do layout do gráfico
    fig.update_layout(
        xaxis_title="Volta",
        yaxis_title=variavel_y,
        legend_title="Carros",
        margin=dict(l=0, r=0, t=30, b=0)
    )

    # Exibir o gráfico
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    # Dividir a tela em duas colunas para seleções
    col1, col2 = st.columns(2)
    
    # Coluna 1: Multiselect para selecionar os carros
    with col1:
        carros_selecionados = st.multiselect(
            "Selecione os Carros:",
            options=data_cronometragem['Carro'].unique(),
            #default=data_cronometragem['Carro'].unique()[:5]  # Seleciona alguns carros como padrão
            key="carros_tab2"
        )

    # Coluna 2: Selectbox para selecionar a variável para o eixo Y
    with col2:
        variavel_y = st.selectbox(
            "Selecione a variável para o eixo Y:",
            options=['Setor 1', 'Setor 2', 'Setor 3', 'Tempo de volta'],
            key="variavel_y_tab2"
        )

    # Filtrar o DataFrame com os carros selecionados
    dados_filtrados = data_cronometragem[data_cronometragem['Carro'].isin(carros_selecionados)]

    # Plotar o gráfico de dispersão com Plotly
    fig_scatter = go.Figure()

    # Adicionar os pontos ao gráfico para cada carro selecionado
    for carro in carros_selecionados:
        dados_carro = dados_filtrados[dados_filtrados['Carro'] == carro]
        fig_scatter.add_trace(go.Scatter(
            x=dados_carro['Gap'],
            y=dados_carro[variavel_y],
            mode='markers',
            name=f'Carro {carro}',
            marker=dict(size=10)  # Tamanho dos marcadores
        ))

    # Configurações do layout do gráfico
    fig_scatter.update_layout(
        xaxis_title="Gap",
        yaxis_title=variavel_y,
        legend_title="Carros",
        margin=dict(l=0, r=0, t=30, b=0)
    )

    # Exibir o gráfico
    st.plotly_chart(fig_scatter, use_container_width=True)

# Tab 3
with tab3:
    # Criar um layout de 4 colunas
    col1, col2, col3, col4 = st.columns(4)

    # Calcular os valores mínimos para cada setor e tempo de volta
    min_setor_1 = data_cronometragem.groupby('Carro')['Setor 1'].min().reset_index()
    min_setor_2 = data_cronometragem.groupby('Carro')['Setor 2'].min().reset_index()
    min_setor_3 = data_cronometragem.groupby('Carro')['Setor 3'].min().reset_index()
    min_tempo_volta = data_cronometragem.groupby('Carro')['Tempo de volta'].min().reset_index()

    # Ordenar os DataFrames pelos valores mínimos
    min_setor_1 = min_setor_1.sort_values(by='Setor 1').reset_index(drop=True)
    min_setor_2 = min_setor_2.sort_values(by='Setor 2').reset_index(drop=True)
    min_setor_3 = min_setor_3.sort_values(by='Setor 3').reset_index(drop=True)
    min_tempo_volta = min_tempo_volta.sort_values(by='Tempo de volta').reset_index(drop=True)

    # Exibir o DataFrame do Setor 1 na primeira coluna
    with col1:
        st.subheader('Setor 1')
        min_setor_1.index = min_setor_1.index + 1
        st.table(min_setor_1)

    # Exibir o DataFrame do Setor 2 na segunda coluna
    with col2:
        st.subheader('Setor 2')
        min_setor_2.index = min_setor_2.index + 1
        st.table(min_setor_2)

    # Exibir o DataFrame do Setor 3 na terceira coluna
    with col3:
        st.subheader('Setor 3')
        min_setor_3.index = min_setor_3.index + 1
        st.table(min_setor_3)

    # Exibir o DataFrame do Tempo de volta na quarta coluna
    with col4:
        st.subheader('Tempo de Volta')
        min_tempo_volta.index = min_tempo_volta.index + 1
        st.table(min_tempo_volta)

