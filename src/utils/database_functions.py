import os
import pandas as pd
import streamlit as st

def get_measures_from_csv(self):
    """Retrieve measures data from a CSV file."""
    measures_csv_path = "./database/measures/data.csv"
    if os.path.exists(measures_csv_path):
        try:
            measures_df = pd.read_csv(measures_csv_path)
            measures_df["Tyre ID"] = measures_df["Tyre ID"].astype(str)
            return measures_df
        except Exception as e:
            st.write(f"Error reading measures data from CSV: {e}")
            return pd.DataFrame()  
    else:
        st.warning("No measures data available.")
        return pd.DataFrame()  
    
def get_damages_from_csv(self):
    """Retrieve damages data from a CSV file."""
    damaged_csv_path = "./database/damaged/data.csv"
    if os.path.exists(damaged_csv_path):
        damage_df = pd.read_csv(damaged_csv_path)

    filtered_damage_df = damage_df[
        (damage_df["Season"] == int(self.filters.selected_season))
    ]

    return filtered_damage_df

def save_damage_to_csv(self):
    """Salvar os dados de pneus danificados no arquivo CSV, removendo duplicatas."""
    if not self.tyre_id or not self.tyre_number or not self.tyre_notes or not self.uploaded_image:
        st.warning('Please fill in all fields and upload an image.')
        return

    data = {
        "Tyre ID": self.tyre_id,
        "Tyre Number": self.tyre_number,
        "Notes": self.tyre_notes,
        "Image": self.uploaded_image.name,
        "Season": self.selected_filters['season'],
        "Stage": self.selected_filters['stage'],
        "Last Session": self.selected_filters['session'],
        "Date": self.selected_filters['date'],
        "Time": self.selected_filters['time'],
        "Car Number": self.selected_filters['number_car']
    }

    database_dir = "./database/damaged"
    os.makedirs(database_dir, exist_ok=True)
    csv_file_path = f'{database_dir}/data.csv'

    if os.path.exists(csv_file_path):
        existing_df = pd.read_csv(csv_file_path)
    else:
        existing_df = pd.DataFrame()

    new_df = pd.DataFrame([data])
    updated_df = pd.concat([existing_df, new_df], ignore_index=True)
    updated_df = updated_df.drop_duplicates()
    updated_df.to_csv(csv_file_path, index=False)

    image_dir = "./database/damaged/images"
    os.makedirs(image_dir, exist_ok=True)
    with open(os.path.join(image_dir, self.uploaded_image.name), "wb") as f:
        f.write(self.uploaded_image.getbuffer())

    st.success('The data was loaded correctly')

def save_measure_to_csv(self):
    """
    Função para salvar os dados no arquivo CSV.
    """
    final_df = self.measure_df.copy()

    final_df["Season"] = self.selected_filters['season']
    final_df["Stage"] = self.selected_filters['stage']
    final_df["Last Session"] = self.selected_filters['session']
    final_df["Date"] = self.selected_filters['date']
    final_df["Time"] = self.selected_filters['time']
    final_df["Car Number"] = self.selected_filters['number_car']

    columns = ["Tyre ID", "Tyre Number"] + [f"Measure {i}" for i in range(1, self.selected_inputs['number_measures'] + 1)]
    final_df = final_df[["Season", "Stage", "Last Session", "Date", "Time", "Car Number"] + columns]

    database_dir = "./database/measures"
    os.makedirs(database_dir, exist_ok=True)
    csv_file_path = f'{database_dir}/data.csv'

    if os.path.exists(csv_file_path):
        existing_df = pd.read_csv(csv_file_path)
        updated_df = pd.concat([existing_df, final_df], ignore_index=True).drop_duplicates()
    else:
        updated_df = final_df

    updated_df.to_csv(csv_file_path, index=False)
    st.success('The data was loaded correctly')

def query_measures_from_csv(self):
    """Função para buscar e exibir os dados de medidas a partir de um arquivo CSV."""
    csv_file_path = './database/measures/data.csv'
    columns = ["Tyre ID", "Tyre Number"] + [f"Measure {i}" for i in range(1, self.selected_inputs['number_measures'] + 1)]
    final_columns = ["Season", "Stage", "Last Session", "Date", "Time", "Car Number"] + columns

    if os.path.exists(csv_file_path):
        try:
            measures_df = pd.read_csv(csv_file_path)
            #st.write(measures_df)
            
            filtered_measures_df = measures_df[
                (measures_df['Season'] == int(self.selected_filters['season'])) &
                (measures_df['Stage'] == self.selected_filters['stage']) &
                (measures_df['Car Number'] == self.selected_filters['number_car'])
            ]
            if filtered_measures_df.empty:
                st.warning("No matching measures data found.")
            else:
                #columns_to_display = ['Tyre ID', 'Tyre Number', 'Last Session', 'Measure 1', 'Measure 2', 'Measure 3']  # Adapte as colunas conforme necessário
                #filtered_measures_df = filtered_measures_df[columns_to_display]
                filtered_measures_df = filtered_measures_df[final_columns]
                edited_measures_df = st.data_editor(filtered_measures_df, num_rows="dynamic", use_container_width=True)
                if st.button("Save Changes", key='save_measures'):
                    edited_measures_df.to_csv(csv_file_path, index=False)
                    st.success("Changes saved successfully!")
        except Exception as e:
            st.error(f"Error reading measures data: {e}")
    else:
        st.warning(f"No data file found at {csv_file_path}.")

def query_damages_from_csv(self):
    """Função para buscar e exibir os dados de danos a partir de um arquivo CSV."""
    csv_file_path = './database/damaged/data.csv'
    # Defina as colunas que deseja exibir, adaptando conforme necessário
    final_columns = ["Season", "Stage", "Last Session", "Date", "Time", "Car Number", "Tyre ID", "Tyre Number", "Notes", "Image"]

    if os.path.exists(csv_file_path):
        try:
            damages_df = pd.read_csv(csv_file_path)

            # Aplique os mesmos filtros que você está usando na função de medidas, se necessário
            filtered_damages_df = damages_df[
                (damages_df['Season'] == int(self.selected_filters['season'])) & 
                (damages_df['Stage'] == self.selected_filters['stage']) & 
                (damages_df['Car Number'] == self.selected_filters['number_car'])
            ]
            if filtered_damages_df.empty:
                st.warning("No matching damage data found.")
            else:
                # Exiba as colunas que você definiu
                filtered_damages_df = filtered_damages_df[final_columns]
                edited_damages_df = st.data_editor(filtered_damages_df, num_rows="dynamic", use_container_width=True)
                if st.button("Save Changes", key='save_damages'):
                    edited_damages_df.to_csv(csv_file_path, index=False)
                    st.success("Changes saved successfully!")
        except Exception as e:
            st.error(f"Error reading damage data: {e}")
    else:
        st.warning(f"No data file found at {csv_file_path}.")

