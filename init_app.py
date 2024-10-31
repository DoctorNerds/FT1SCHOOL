import streamlit as st
from src.classes.app import App

# Configurações da página
st.set_page_config(
    page_title="FT1 TYRE CONTROL",  # Título da página
    layout="wide",                   # Layout em tela cheia
    initial_sidebar_state="expanded"  # Barra lateral expandida ao abrir
)

# Inicializa a aplicação
app = App() 

def run_app():
    """
    Função principal para executar a aplicação.
    Esta função configura a interface da aplicação, 
    incluindo cabeçalhos, abas e as respectivas telas de medição, 
    pneus danificados e consulta ao banco de dados.
    """
    app.header_filters()  # Chama a função para exibir os filtros no cabeçalho
    # Define as abas da aplicação
    tabs = st.tabs(["Input Measures", "Damaged Tyres", "Query Database"])
    
    # Aba para medidas de entrada
    with tabs[0]:
        app.measurements_screen()  # Chama a tela de medições

    # Aba para pneus danificados
    with tabs[1]:
        app.damaged_screen()  # Chama a tela de pneus danificados

    # Aba para consulta ao banco de dados
    with tabs[2]:
        app.database_screen()  # Chama a tela de consulta ao banco de dados

# Executa a aplicação
if __name__ == "__main__":
    run_app()  # Chama a função principal para iniciar a aplicação
