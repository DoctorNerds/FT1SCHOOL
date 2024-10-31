import streamlit as st
import pandas as pd

# Importa classes e funções de configuração e utilidades
from src.classes.config import Config
from src.utils.header_functions import header_filters, get_filters
from src.utils.database_functions import (
    get_measures_from_csv,
    get_damages_from_csv,
    save_damage_to_csv,
    save_measure_to_csv,
    query_measures_from_csv,
    query_damages_from_csv
)
from src.utils.text_instructions import measure_instructions, damage_instructions

class App:
    """
    Classe que representa a aplicação de controle de pneus.
    
    A classe gerencia a configuração, manipulação de dados e interface da aplicação,
    incluindo telas para medições, pneus danificados e consultas ao banco de dados.
    """

    def __init__(self):
        """
        Inicializa a classe App.
        
        Define os atributos iniciais da aplicação, incluindo configurações, 
        informações do pneu, e um DataFrame para medições.
        """
        self.config = Config()  # Carrega as configurações da aplicação
        self.tyre_id = ''  # ID do pneu
        self.tyre_number = ''  # Número do pneu
        self.tyre_notes = ''  # Notas sobre o pneu
        self.uploaded_image = None  # Imagem carregada do pneu
        self.selected_filters = {}  # Filtros selecionados
        self.selected_inputs = {}  # Entradas selecionadas
        self.measure_df = pd.DataFrame()  # DataFrame para medições

    def header_filters(self):
        """Chama a função para exibir os filtros no cabeçalho da aplicação."""
        header_filters(self)

    def get_filters(self):
        """Retorna os filtros selecionados pela aplicação."""
        return get_filters(self)

    def get_measures_from_csv(self):
        """Obtém medições a partir de um arquivo CSV."""
        return get_measures_from_csv()

    def get_damages_from_csv(self):
        """Obtém danos a partir de um arquivo CSV."""
        return get_damages_from_csv(self)

    def save_damage_to_csv(self):
        """Salva informações de danos em um arquivo CSV."""
        save_damage_to_csv(self)

    def save_measure_to_csv(self):
        """Salva medições em um arquivo CSV."""
        save_measure_to_csv(self)

    def query_measures_from_csv(self):
        """Consulta medições a partir de um arquivo CSV."""
        query_measures_from_csv(self)

    def query_damages_from_csv(self):
        """Consulta danos a partir de um arquivo CSV."""
        query_damages_from_csv(self)

    def measure_instructions(self):
        """Exibe instruções sobre como fazer medições."""
        measure_instructions()

    def damage_instructions(self):
        """Exibe instruções sobre como registrar danos."""
        damage_instructions()

    def measurements_screen(self):
        """
        Exibe a tela de medições, que inclui campos para entrada de dados 
        e instruções sobre medições.
        """
        cl1, cl2 = st.columns([1.7, 1])  # Cria duas colunas
        with cl1:
            self.measure_number()  # Chama a função para selecionar o número de medições
            self.input_dataframe()  # Chama a função para entrada de dados
        with cl2:
            self.measure_instructions()  # Exibe instruções de medições

    def measure_number(self):
        """
        Permite ao usuário selecionar o número de medições a serem feitas.
        """
        cl1, cl2 = st.columns([1, 6])  # Cria duas colunas
        with cl1:
            try:
                # Obtém o índice do número de medições padrão na configuração
                index = self.config.measures.index(self.config.measure_default)
            except ValueError:
                index = len(self.config.measures) - 1  # Usa o último índice se não encontrado

            # Cria um seletor para o número de medições
            self.number_measures = st.selectbox("Number of measures", self.config.measures, index=index)
        with cl2:
            st.empty()  # Coluna vazia

    def input_dataframe(self):
        """
        Permite ao usuário inserir dados de medições em um DataFrame dinâmico.
        """
        self.selected_filters = self.get_filters()  # Obtém filtros selecionados
        self.selected_inputs = self.get_inputs()  # Obtém entradas selecionadas

        # Define as colunas do DataFrame
        columns = ["Tyre ID", "Tyre Number"] + [f"Measure {i}" for i in range(1, self.selected_inputs['number_measures'] + 1)]
        df = pd.DataFrame(columns=columns)  # Cria um DataFrame vazio com as colunas definidas

        # Cria um editor de dados para o DataFrame
        self.measure_df = st.data_editor(df, num_rows="dynamic", use_container_width=True)

        # Botão para submeter dados
        if st.button("Submit Data", key="measure_tyres"):
            self.save_measure_to_csv()  # Salva medições se o botão for clicado

    def get_inputs(self):
        """
        Retorna as entradas selecionadas para medições.
        
        Returns:
            dict: Um dicionário contendo o número de medições.
        """
        return {
            "number_measures": self.number_measures,
        }

    def damaged_screen(self):
        """
        Função principal para a aba de pneus danificados.
        Exibe campos de entrada para dados de pneus danificados e instruções relacionadas.
        """
        self.selected_filters = self.get_filters()  # Obtém filtros selecionados
        cl1, cl2 = st.columns([1.7, 1])  # Cria duas colunas
        with cl1:
            self.input_damaged_tyres()  # Chama a função para entrada de dados dos pneus danificados

        with cl2:
            self.damage_instructions()  # Exibe instruções sobre danos

    def input_damaged_tyres(self):
        """
        Função para lidar com o layout e entrada de dados relacionados a pneus danificados.
        Permite ao usuário inserir informações sobre o pneu danificado.
        """
        subcl1, subcl2 = st.columns([1, 1])  # Cria duas subcolunas
        with subcl1:
            self.tyre_id = st.text_input('Tyre ID (e.g., 1234)', '')  # Entrada para ID do pneu
        with subcl2:
            self.tyre_number = st.text_input('Tyre Number (e.g., FT 12)', '')  # Entrada para número do pneu

        self.tyre_notes = st.text_area('Notes about what happened to the tyre', '')  # Área de texto para notas
        self.uploaded_image = st.file_uploader("Upload an image file", type=["jpg", "jpeg", "png"])  # Carregador de imagem

        # Botão para submeter dados de pneus danificados
        if st.button('Submit Data', key="damaged_tyres"):
            self.save_damage_to_csv()  # Salva dados de danos se o botão for clicado

    def database_screen(self):
        """
        Exibe a tela de consulta ao banco de dados com duas abas:
        uma para medições e outra para danos.
        """
        tabs = st.tabs(["Measures", "Damaged"])  # Cria abas para medições e danos
        with tabs[0]:
            self.query_measures_from_csv()  # Chama a função para consultar medições
        with tabs[1]:
            self.query_damages_from_csv()  # Chama a função para consultar danos

# Executa a aplicação
if __name__ == "__main__":
    app = App()  # Cria uma instância da classe App
