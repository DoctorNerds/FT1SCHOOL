import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Configura a página principal com título, layout em tela cheia e barra lateral expandida
st.set_page_config(
    page_title="Aula 02",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Carregar os dados do arquivo Excel
data_overall = pd.read_excel('./data/estatisticas.xlsx')


# Dividir a interface em abas
tab1, tab2 = st.tabs(["Aproveitamento por Piloto", "Resumo Estatístico"])

with tab1:
    # A partir do DataFrame, vamos extrair as colunas necessárias
    data_sorted = data_overall.sort_values(by='Aproveitamento Geral', ascending=False)
    pilotos = data_sorted['Piloto']  # Convertendo para string, se necessário
    aproveitamento_geral = data_sorted['Aproveitamento Geral']
    aproveitamento_r1 = data_sorted['Aproveitamento R1']
    aproveitamento_r2 = data_sorted['Aproveitamento R2']

    # Criar o gráfico de barras
    fig = go.Figure()

    # Adicionar traços para cada aproveitamento
    fig.add_trace(go.Bar(
        x=pilotos,
        y=aproveitamento_geral,
        name='Geral',
        marker_color='rgb(55, 83, 109)'
    ))
    fig.add_trace(go.Bar(
        x=pilotos,
        y=aproveitamento_r1,
        name='Corrida 1',
        marker_color='rgb(26, 118, 255)'
    ))
    fig.add_trace(go.Bar(
        x=pilotos,
        y=aproveitamento_r2,
        name='Corrida 2',
        marker_color='rgb(255, 165, 0)'  # Cor laranja para R2
    ))

    # Atualizar layout do gráfico
    fig.update_layout(
        title='Aproveitamento dos Pilotos',
        xaxis_title='Pilotos',
        yaxis_title='Aproveitamento (%)',
        xaxis_tickfont_size=12,
        yaxis=dict(
            title=dict(
                text="Aproveitamento (%)",
                font=dict(
                    size=14
                )
            ),
            tickfont_size=12,
        ),
        legend=dict(
            x=0.95,
            y=1.0,
            bgcolor='rgba(255, 255, 255, 0)',
            bordercolor='rgba(255, 255, 255, 0)'
        ),
        barmode='group',  # Colocar as barras lado a lado
        bargap=0.15,  # Espaçamento entre barras de locais adjacentes
        bargroupgap=0.1  # Espaçamento entre barras do mesmo local
    )
    # Exibir gráfico
    st.plotly_chart(fig)

# Dicionário para renomear as colunas
column_names_map = {
    'Evo_Largada1': 'Evolução na Largada na Corrida 1',
    'Evo_PrePit_Corrida1': 'Evolução pré Pit Stop na Corrida 1',
    'Pos_Final_Corrida1': 'Posição final na Corrida 1',
    'Pontos_Corrida1': 'Pontos na Corrida 1',
    'Evo_Largada2': 'Evolução na Largada na Corrida 2',
    'Evo_PrePit_Corrida2': 'Evolução pré Pit Stop na Corrida 2',
    'Pos_Final_Corrida2': 'Posição final na Corrida 2',
    'Pontos_Corrida2': 'Pontos na Corrida 2',
    'Aproveitamento_Etapa': 'Aproveitamento na Etapa'
}

with tab2:
    # Carregar e renomear colunas
    data_results = pd.read_excel('./data/resultados.xlsx')
    data_results.rename(columns=column_names_map, inplace=True)

    # Selecionar o piloto
    piloto_selecionado = st.selectbox('Selecione o Piloto', data_results['Carro'].unique())

    # Filtrar dados do piloto
    dados_piloto = data_results[data_results['Carro'] == piloto_selecionado]

    # Dividir a tela em duas colunas
    col1, col2 = st.columns(2)

    # Primeira coluna - Estatísticas
    with col1:
        st.subheader(f'Estatísticas para o Piloto {piloto_selecionado}')
        st.dataframe(dados_piloto[column_names_map.values()].describe().T)

    # Segunda coluna - Gráfico
    with col2:
        variavel_y = st.selectbox('Selecione a variável para o gráfico', column_names_map.values())
        
        # Plotar gráfico de linha
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=dados_piloto['Etapa'],
            y=dados_piloto[variavel_y],
            mode='lines+markers',
            line=dict(color='royalblue', width=2),
            marker=dict(size=6)
        ))
        fig.update_layout(
            xaxis_title='Etapa',
            yaxis_title=variavel_y,
            xaxis=dict(tickmode='linear'),
            yaxis=dict(tickformat=',.2f'),
            height=400,
            showlegend=False
        )
        # Exibir gráfico
        st.plotly_chart(fig)