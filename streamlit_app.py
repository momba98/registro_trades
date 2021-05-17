import streamlit as st
from PIL import Image
import os

st.set_page_config(
    page_title='Teste Drive',
    #page_icon="https://static.streamlit.io/examples/cat.jpg",
    layout='centered',
    initial_sidebar_state='auto'
)

st.title("""

Teste Drive

""")

image_file = st.file_uploader("Upload An Image",type=['png','jpeg','jpg'])

def save_uploadedfile(uploadedfile):
     with open(os.path.join("tempDir",uploadedfile.name),"wb") as f:
         f.write(uploadedfile.getbuffer())
     return st.success("Saved File:{} to tempDir".format(uploadedfile.name))

if image_file is not None:
    save_uploadedfile(image_file)

    st.image(f'tempDIR/{image_file.name}',use_column_width=True)
