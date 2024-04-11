import streamlit as st
import warnings
from img_classif.pipeline.prediction import Image_label_prediction
import numpy as np
warnings.filterwarnings('ignore')



# set some pre-defined configurations for the page, such as the page title, logo-icon, page loading state (whether the page is loaded automatically or you need to perform some action for loading)
st.set_page_config(
    page_title="Satellite image classification",
    page_icon = ":satellite:",
    initial_sidebar_state = 'auto'
)

def Navbar():
    with st.sidebar:
        st.page_link('app.py', label='Main - Predictions')
        st.page_link('pages/01_train.py', label='CNN model training')

Navbar()

# hide the part of the code, as this is just for adding some custom CSS styling but not a part of the main idea 
hide_streamlit_style = """
	<style>
  #MainMenu {visibility: hidden;}
	footer {visibility: hidden;}
  </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True) # hide the CSS code from the screen as they are embedded in markdown text. Also, allow streamlit to unsafely process as HTML


with st.sidebar:
    st.header('Sattelite image classification')
    st.image('/pagesimg_classif.jfif')
    st.subheader('Using advanced CNN model for satellite image classification')


progress_text = "Loading CNN model in progess. Please wait."
my_bar = st.progress(0, text=progress_text)
my_bar.progress(0, text='Model running')
model = Image_label_prediction()
model.load_model_labels()

file = st.file_uploader("", type=["jpg", "png"])


if file:
    st.image(file, use_column_width=True)
    predicted_label,proba = model.predict(file)

    st.sidebar.error("Accuracy : " + str(np.round(proba)) + " %")
    st.sidebar.success('Predicted label: ' + str(predicted_label))
    my_bar.progress(100, text='Image predicted successfully')

