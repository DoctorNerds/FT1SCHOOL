import pandas as pd
import streamlit as st
import plotly.express as px

# Configura a página principal com título, layout em tela cheia e barra lateral expandida
st.set_page_config(
    page_title="Aula 04",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Carregar o DataFrame
data_kpis = pd.read_excel('./data/kpis.xlsx')

# Seleção de abas na sidebar
selected_tab = st.sidebar.selectbox("Selecione uma aba", ["Vitais", "Performance"])

# Exibir o título selecionado
st.title(selected_tab)

if selected_tab == "Vitais":
    with st.container():
        # Criar e exibir o box plot para todas as colunas de temperatura
        st.subheader("Gráfico de Box Plot")
        fig_vital = px.box(
            data_kpis,
            y=['ECU_Oil_Temp (°C)', 'ECU_Coolant_Temp (°C)', 'ECU_Fuel_Temp (°C)', 'Gear Temp (°C)'],
            color='variable',
        )

        # Atualizar os rótulos dos eixos
        fig_vital.update_layout(
            yaxis_title='Temp. (°C)',  # Rótulo do eixo Y
            xaxis_title='',            # Sem rótulo para o eixo X
        )

        # Exibir o gráfico
        st.plotly_chart(fig_vital)

elif selected_tab == "Performance":
    # Criar abas dentro da aba de Performance
    tab1, tab2 = st.tabs(["Box Plot", "Gráficos de Linha e Dispersão"])

    # Aba 1 - Box Plot
    with tab1:
        st.subheader("Gráfico de Box Plot")
        coluna_performance = ['Grip Factor Aero KPI (G)', 'Grip Factor Braking KPI (G)',
                              'Grip Factor Cornering KPI (G)', 'Grip Factor Traction KPI (G)', 'Grip Factor Overall KPI (G)']

        fig_performance_box = px.box(data_kpis, y=coluna_performance, color='variable')
        st.plotly_chart(fig_performance_box)

    # Aba 2 - Gráficos de Linha e Dispersão
    with tab2:
        # Criar duas colunas
        col1, col2 = st.columns(2)

        # Coluna 1 - Gráfico de linha
        with col1:
            st.subheader("Gráfico de Linha")
            coluna_linha = st.selectbox(
                "Escolha a coluna para o gráfico de linha:",
                ['Steering Smoothness KPI (°)', 'Steering Integral KPI', 
                'Brake Balance KPI (%)']
            )
            fig_line = px.line(data_kpis, x=data_kpis.index, y=coluna_linha)
            st.plotly_chart(fig_line)

        # Coluna 2 - Gráfico de dispersão
        with col2:
            st.subheader("Gráfico de Dispersão")
            coluna_dispercao = st.selectbox(
                "Escolha a coluna para o gráfico de dispersão:",
                ['Steering Smoothness KPI (°)', 'Steering Integral KPI', 
                'Brake Balance KPI (%)', 'Braking Aggression KPI', 
                'Braking Release Smoothness KPI', 'Brake Efficiency KPI', 
                'Full Throttle Time KPI (s)', 'Throttle Agression KPI']
            )
            fig_scatter = px.scatter(data_kpis, x='Lap Time', y=coluna_dispercao)
            st.plotly_chart(fig_scatter)