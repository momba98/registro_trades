import streamlit as st
import pandas as pd
from PIL import Image
from datetime import datetime, timedelta
import time
import os
import xlrd
import numpy as np
import io

#incluir gráfico: selecione o ativo e veja seu desempenho no ranking ao longo do tempo
#incluir customização: adicionar ou não o ranking definido por mim, que vai comparar
#o desemepnho do ativo com o desempenho do ibov naquele ano. começar em 2015 e ir até 2020.
#TROCAR O NOME DO REPO

st.set_page_config(
    page_title='Teste Drive',
    #page_icon="https://static.streamlit.io/examples/cat.jpg",
    layout='centered',
    initial_sidebar_state='auto'
)

st.title("""

Teste Drive

""")


st.title("Upload + Classification Example")

image_file = st.file_uploader("Upload An Image",type=['png','jpeg','jpg'])

def save_uploadedfile(uploadedfile):
     with open(os.path.join("tempDir",uploadedfile.name),"wb") as f:
         f.write(uploadedfile.getbuffer())
     return st.success("Saved File:{} to tempDir".format(uploadedfile.name))

if image_file is not None:
    save_uploadedfile(image_file)
