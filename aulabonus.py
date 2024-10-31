import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import random


# Configura a página principal com título, layout em tela cheia e barra lateral expandida
st.set_page_config(
    page_title="Aula Bônus",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Exemplo de Sidebar
st.sidebar.title("Exemplo de Sidebar")
st.sidebar.write("Use a sidebar para agrupar controles e navegadores adicionais.")

# Título da aula
st.title("FT1 School: Crie aplicativos web com o Streamlit para Motorsport")
st.write("Explore algumas das funcionalidades para desenvolver o seu aplicativo.")

# Input de Texto
st.header("Input de Texto")
name = st.text_input("Digite seu nome:")
if name:
    st.write(f"Seja bem-vindo a FT1 School, {name}!")

# Input Numérico e Sliders
st.header("Input Numérico e Sliders")
age = st.number_input("Digite sua idade:", min_value=1, max_value=100, step=1)
rating = st.slider("Avalie este curso:", 1, 5)
st.write(f"Idade: {age}, Avaliação: {rating}")

# Checkbox, Radio e Selectbox
st.header("Checkbox, Radio e Selectbox")
if st.checkbox("Eu quero participar do grupo gratuito da FT1 School"):
    st.write("Basta seguir a @ft1school no instagram e clicar no link da bio para participar!")

# Dicionário mapeando os pilotos para seus Instagrams
instagram_handles = {
    'Arthur Leist': '@arthurleist',
    'Dudu Barrichello': '@dudubarrichello',
    'Gianluca Petecof': '@gpetecof',
    'Rubens Barrichello': '@rubarrichello'
}

favorite_pilot = st.radio("Escolha seu piloto favorito:", list(instagram_handles.keys()))
instagram = instagram_handles.get(favorite_pilot, "")
st.write(f"Então siga seu piloto favorito no Instagram: {instagram}")

# Dicionário mapeando as opções para suas URLs
urls = {
    "Website Oficial": "http://www.fulltimesports.com.br/index.html",
    "Loja Online": "https://fulltimestore.lojavirtuolpro.com/",
    "Vlog Youtube": "https://www.youtube.com/@fulltimesports1",
    "Escola FT1": "https://www.instagram.com/ft1school/"
}

# Selectbox para escolher a opção
option = st.selectbox("Escolha uma opção:", list(urls.keys()))

# Exibe o link como um botão de link usando `st.link_button`
st.link_button(f"Acessar {option}", urls[option])

# Carregamento de Arquivo
st.header("Carregamento de Arquivo")
uploaded_file = st.file_uploader("Envie um arquivo Excel", type=["xlsx"])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    st.write("Visualização dos dados:")
    st.write(df.head(10))

# Gráficos com Plotly
st.header("Gráficos com Plotly")
data = pd.DataFrame({
    'X': np.random.randn(100),
    'Y': np.random.randn(100)
})
fig = px.scatter(data, x='X', y='Y', title="Exemplo de Gráfico de Dispersão")
st.plotly_chart(fig)

# Mapa Interativo
st.header("Mapa Interativo")
# Coordenadas exatas da oficina em Vinhedo - SP
map_data = pd.DataFrame({
    'lat': [-23.04350554279046],
    'lon': [-46.97885418114834]
})
st.map(map_data)

# Exibir Imagens
st.header("Exibir Imagens")

# Lista de URLs de imagens
image_urls = [
    "http://fulltimesports.com.br/images/2015/equipe.jpg",
    "http://fulltimesports.com.br/images/2015/equipe2022.jpg",
    "http://fulltimesports.com.br/images/2015/equipeF42022.jpg",
    "http://fulltimesports.com.br/images/2015/equipe2.jpg",
    "http://fulltimesports.com.br/images/2019/equipe.jpg"
]

# Botão para exibir uma imagem aleatória da equipe
if st.button("Exibir imagem da equipe da Fulltime Sports"):
    # Selecionar uma imagem aleatória
    selected_image = random.choice(image_urls)
    st.image(selected_image, caption="Equipe Fulltime Sports", use_column_width=True)

# Exibir um Vídeo do Vlog
st.header("Vídeo")
st.write("Vlog Fulltime Sports")
st.video("https://www.youtube.com/watch?v=jF1MpPcImf8")

# Exibir Código
st.header("Exibir Código")
st.code("""
def hello():
    print("Hello, Streamlit!")
""")

# Mensagens de Alerta e Sucesso
st.header("Mensagens de Alerta e Sucesso")
st.success("Sucesso! Operação realizada com sucesso.")
st.warning("Aviso! Algo pode estar errado.")
st.error("Erro! Algo deu errado.")

# Progresso e Spinner
st.header("Barra de Progresso e Spinner")
import time

# Botão para iniciar a contagem
if st.button("Finlizar aula"):
    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        progress.progress(i + 1)

    with st.spinner("Carregando..."):
        time.sleep(2)
    
    st.success("Parabéns! Você concluiu o curso Streamlit para Motorsports da FT1 School")

