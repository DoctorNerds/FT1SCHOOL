import streamlit as st
import pandas as pd

from src.classes.config import Config
from src.utils.header_functions import header_filters, get_filters
from src.utils.database_functions import get_measures_from_csv, get_damages_from_csv, save_damage_to_csv, save_measure_to_csv, query_measures_from_csv, query_damages_from_csv
from src.utils.text_instructions import measure_instructions, damage_instructions

class App:
    def __init__(self):
        self.config = Config()
        self.tyre_id = ''
        self.tyre_number = ''
        self.tyre_notes = ''
        self.uploaded_image = None
        self.selected_filters = {}
        self.selected_filters = {}
        self.selected_inputs = {}
        self.measure_df = pd.DataFrame()

    def header_filters(self):
        header_filters(self)

    def get_filters(self):
        return get_filters(self)

    def get_measures_from_csv(self):
        return get_measures_from_csv()

    def get_damages_from_csv(self):
        return get_damages_from_csv(self)

    def save_damage_to_csv(self):
        save_damage_to_csv(self)

    def save_measure_to_csv(self):
        save_measure_to_csv(self)

    def query_measures_from_csv(self):
        query_measures_from_csv(self)

    def query_damages_from_csv(self):
        query_damages_from_csv(self)

    def measure_instructions(self):
        measure_instructions()

    def damage_instructions(self):
        damage_instructions()

    def measurements_screen(self):
        cl1, cl2 = st.columns([1.7, 1])       
        with cl1:
            self.measure_number()           
            self.input_dataframe()      
        with cl2:
            self.measure_instructions()

    def measure_number(self):
        cl1, cl2 = st.columns([1, 6])
        with cl1:
            try:
                index = self.config.measures.index(self.config.measure_default)
            except ValueError:
                index = len(self.config.measures) - 1

            self.number_measures = st.selectbox("Number of measures", self.config.measures, index=index)
        with cl2:
            st.empty()

    def input_dataframe(self):
        self.selected_filters = self.get_filters()
        self.selected_inputs = self.get_inputs()

        columns = ["Tyre ID", "Tyre Number"] + [f"Measure {i}" for i in range(1, self.selected_inputs['number_measures'] + 1)]
        df = pd.DataFrame(columns=columns)

        self.measure_df = st.data_editor(df, num_rows="dynamic", use_container_width=True)

        if st.button("Submit Data", key="measure_tyres"):
            self.save_measure_to_csv()

    def get_inputs(self):
        return {
            "number_measures": self.number_measures,
        }

    def damaged_screen(self):
        """Função principal para a aba de pneus danificados."""
        self.selected_filters = self.get_filters()
        cl1, cl2 = st.columns([1.7, 1])
        with cl1:
            self.input_damaged_tyres()  

        with cl2:
            self.damage_instructions()

    def input_damaged_tyres(self):
        """Função para lidar com o layout e entrada de dados relacionados a pneus danificados."""
        subcl1, subcl2 = st.columns([1, 1])
        with subcl1:
            self.tyre_id = st.text_input('Tyre ID (e.g., 1234)', '')
        with subcl2:
            self.tyre_number = st.text_input('Tyre Number (e.g., FT 12)', '')

        self.tyre_notes = st.text_area('Notes about what happened to the tyre', '')
        self.uploaded_image = st.file_uploader("Upload an image file", type=["jpg", "jpeg", "png"])

        if st.button('Submit Data', key="damaged_tyres"):
            self.save_damage_to_csv()

    def database_screen(self):
        tabs = st.tabs(["Measures", "Damaged"])
        with tabs[0]:
            self.query_measures_from_csv()
        with tabs[1]:
            self.query_damages_from_csv()

if __name__ == "__main__":
    app = App()
    