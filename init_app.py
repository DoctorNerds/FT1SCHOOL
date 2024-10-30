import streamlit as st
from src.classes.app import App

st.set_page_config(
    page_title="FT1 TYRE CONTROL",
    layout="wide",
    initial_sidebar_state="expanded"
)

app = App() 

def run_app():
    app.header_filters()
    tabs = st.tabs(["Input Measures", "Damaged Tyres", "Query Database"])
    with tabs[0]:
        app.measurements_screen()
    with tabs[1]:
        app.damaged_screen()
    with tabs[2]:
        app.database_screen()

if __name__ == "__main__":
    run_app()

