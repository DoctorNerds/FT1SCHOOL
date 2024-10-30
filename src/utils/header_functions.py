import streamlit as st
import datetime

def header_filters(self):
    cl1, cl2, cl3, cl4, cl5, cl6 = st.columns([0.8, 1.5, 1.5, 1, 1, 1])
    with cl1:
        seasons = list(self.config.informations.keys())
        self.selected_season = st.selectbox("Select Season", seasons)
    if self.selected_season:
        current_season_data = self.config.informations.get(self.selected_season, {})
        with cl2:
            self.selected_stage = st.selectbox("Select Stage", current_season_data.get('stage', []))
        with cl3:
            self.selected_session = st.selectbox("Select Last Session", current_season_data.get('session', []))
        with cl4:
            self.number_car = st.selectbox("Number of the car", current_season_data.get('car_numbers', []))
    with cl5:
        default_date = datetime.date.today()
        self.selected_date = st.date_input("Select a Date", value=default_date)
    with cl6:
        default_time = datetime.time(9, 0)  
        self.selected_time = st.time_input("Select a Time", value=default_time)

def get_filters(self):
    return {
        "season": self.selected_season,
        "stage": self.selected_stage,
        "session": self.selected_session,
        "number_car": self.number_car,
        "date": self.selected_date,
        "time": self.selected_time
    }