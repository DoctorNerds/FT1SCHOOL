import streamlit as st
import pandas as pd
import os
import json

class Config:
    """Classe para gerenciar as configurações a partir de um arquivo JSON."""
    def __init__(self):
        """Inicializa a classe Config carregando as configurações de um arquivo JSON."""
        self.config_path = './src/utils/configurations.json'
        
        # Verifica se o arquivo de configuração existe
        if os.path.exists(self.config_path):
            with open(self.config_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Recupera 'informations' dos dados carregados
            self.informations = data.get("informations", {})

            # Seleciona a última temporada disponível
            last_season = sorted(self.informations.keys())[-1]
            last_season_data = self.informations[last_season]

            # Inicializa os atributos com base na última temporada
            self.season = last_season
            self.stage = last_season_data.get('stage', [])
            self.session = last_season_data.get('session', [])
            self.measures = last_season_data.get('measures', [])
            self.car_numbers = last_season_data.get('car_numbers', [])
            self.measure_default = last_season_data.get('measure_default', 1)           
        else:
            # Exibe um aviso se o arquivo de configuração não existir
            st.warning("Please create the JSON file with the default information.")
            