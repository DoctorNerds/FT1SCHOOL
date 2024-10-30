import streamlit as st


def measure_instructions():
    st.warning("""
    The information in the table must be entered as follows:
    - **Tire identification:** Only numbers in sequence (ex: 12345).
    - **Tyre number:** Two letters + space + two or three numbers (ex: FT 01).
    - **Measurement:** One number to two decimal places (ex: 1.23).
    - Size 1 is always the inside size of the tyre (see image above).
    """)

def damage_instructions():
    st.warning("""
    The information in the table must be entered as follows:
    - **Tire identification:** Only numbers in sequence (ex: 12345).
    - **Tyre number:** Two letters + space + two or three numbers (ex: FT 01).
    - **Tyre Notes:** Summary information about what happened.
    - **Tyre Image:** A photo must be uploaded to illustrate the tyre damage.
    """)
