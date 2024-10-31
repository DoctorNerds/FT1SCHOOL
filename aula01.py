import streamlit as st
from fpdf import FPDF
from datetime import datetime
import os

# Configura a página principal com título, layout em tela cheia e barra lateral expandida
st.set_page_config(
    page_title="Aula 01",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Função para salvar as informações em um arquivo PDF
def save_to_pdf(file_name, pilot_name, tire_choice, feedback, setup_changes, date, time, track_temp, asphalt_temp, outing_number, fuel_amount):
    """Cria e salva um arquivo PDF com as informações fornecidas, incluindo detalhes sobre o piloto, configurações e feedback.

    Args:
        file_name (str): Nome do arquivo PDF a ser salvo.
        pilot_name (str): Nome do piloto.
        tire_choice (str): Tipo de pneu utilizado.
        feedback (str): Comentários do piloto sobre a corrida.
        setup_changes (str): Mudanças feitas no setup do carro.
        date (datetime): Data da corrida.
        time (datetime): Hora da corrida.
        track_temp (int): Temperatura da pista em °C.
        asphalt_temp (int): Temperatura do asfalto em °C.
        outing_number (int): Número do outing (saída).
        fuel_amount (int): Quantidade de combustível em litros.

    Returns:
        None
    """
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Workbook", ln=True, align='C')
    pdf.cell(200, 10, txt=f"Data: {date.strftime('%d/%m/%Y')}", ln=True)
    pdf.cell(200, 10, txt=f"Hora: {time.strftime('%H:%M')}", ln=True)
    pdf.cell(200, 10, txt=f"Piloto: {pilot_name}", ln=True)
    pdf.cell(200, 10, txt=f"Pneu Utilizado: {tire_choice}", ln=True)
    pdf.cell(200, 10, txt=f"Temperatura da Pista: {track_temp} °C", ln=True)
    pdf.cell(200, 10, txt=f"Temperatura do Asfalto: {asphalt_temp} °C", ln=True)
    pdf.cell(200, 10, txt=f"Número do Outing: {outing_number}", ln=True)
    pdf.cell(200, 10, txt=f"Quantidade de Combustível: {fuel_amount} litros", ln=True)
    pdf.cell(200, 10, txt="Feedback do Piloto:", ln=True)
    pdf.multi_cell(0, 10, txt=feedback)
    pdf.cell(200, 10, txt="Mudanças de Setup:", ln=True)
    pdf.multi_cell(0, 10, txt=setup_changes)

    pdf.output(file_name)

# Título da aplicação
st.title("Workbook")

# Dividindo a tela em três colunas
col1, col2, col3 = st.columns([1, 1.5, 0.5])

# Coluna 1: Dividindo em duas subcolunas
with col1:
    subcol1, subcol2 = st.columns(2)
    
    # Subcoluna 1: Seleção de data, hora e listas
    with subcol1:
        date = st.date_input("Selecione a Data:", value=datetime.now())
        time = st.time_input("Selecione a Hora:", value=datetime.now().time())
        pilot_name = st.selectbox("Selecione o Piloto:", ["Piloto A", "Piloto B", "Piloto C"])
        tire_choice = st.selectbox("Selecione o Pneu Utilizado:", ["Duro", "Médio", "Macio"])

    # Subcoluna 2: Inputs de temperatura e outros
    with subcol2:
        track_temp = st.number_input("Temperatura da Pista (°C):", min_value=-10, max_value=50, value=25)
        asphalt_temp = st.number_input("Temperatura do Asfalto (°C):", min_value=-10, max_value=50, value=25)
        outing_number = st.number_input("Número do Outing:", min_value=1, value=1)
        fuel_amount = st.select_slider("Quantidade de Combustível (litros):", options=list(range(10, 71)), value=10)

# Coluna 2: Inputs de Texto
with col2:
    feedback = st.text_area("Feedback do Piloto:", "")
    setup_changes = st.text_area("Mudanças de Setup:", "", height=160)

# Coluna 3: Seleção de imagem e exibição
with col3:
    # Diretório das imagens
    image_folder = './images/aula01/'

    # Obtendo todos os arquivos de imagem na pasta e removendo a extensão para exibir só o nome
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.png')]
    image_names = [os.path.splitext(f)[0] for f in image_files]

    # Seleção da imagem pelo nome (sem extensão)
    image_name = st.selectbox("Selecione uma Imagem:", image_names)
    selected_image_path = os.path.join(image_folder, image_name + ".png")

    # Exibindo a imagem com tamanho definido
    if os.path.exists(selected_image_path):
        st.image(selected_image_path, width=250)

# Linha abaixo das três colunas: Nome do arquivo e botão de salvar
st.markdown("---")
output_dir = './reports/aula01/'
os.makedirs(output_dir, exist_ok=True)

# Dividindo a tela em duas colunas
col_filename, _ = st.columns([1, 3])  # Deixa a segunda coluna vazia para dar espaço ao campo

# Campo de entrada para o nome do arquivo
with col_filename:
    file_name = st.text_input("Nome do arquivo (sem extensão):") + ".pdf"

# Botão para salvar as anotações, posicionado logo abaixo do campo de entrada
if st.button("Salvar Anotações"):
    if pilot_name and tire_choice and feedback and setup_changes:
        # Atualiza o caminho para salvar o PDF na nova pasta
        file_path = os.path.join(output_dir, file_name)
        save_to_pdf(file_path, pilot_name, tire_choice, feedback, setup_changes, date, time, track_temp, asphalt_temp, outing_number, fuel_amount)
        st.success(f"Anotações salvas com sucesso em {file_path}!")
    else:
        st.error("Por favor, preencha todos os campos antes de salvar.")
