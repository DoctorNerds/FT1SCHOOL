*COMANDOS IMPORTANTES NO TERMINAL*

Para criar um ambiente virtual
python -m venv venv

Para ativar o ambiente virtual (venv):
./venv/Scripts/Activate.ps1

Como criar o requirements.txt
1) instalar o pigar:
pip install pigar
2) criar o requirements.txt
pigar generate

Para rodar arquivo com streamlit (caminho: D:\Hello_World\main.py)
python -m streamlit run "D:\Hello_World\main.py"

Para criar executável
criar os arquivos run.py e setup.py
python setup.py build

bibliotecas instaladas:
pip install streamlit
pip install plotly
pip intall openpyxl