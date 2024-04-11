import streamlit as st
from img_classif.utils.common import read_yaml
from pathlib import Path
from app import Navbar
import yaml

Navbar()
params_fn = Path("params.yaml")
params = read_yaml(params_fn)

with st.sidebar:
    st.header('CNN model training')
    st.image('/pages/CNN_model.png')
    st.subheader('Number of default epochs: ' + str(params.epochs))


nepoch = st.slider('Insert the number of epochs', min_value=1, max_value=10, value=3, step=1)

params = dict(params)
params['epochs'] = int(nepoch)
with open("params.yaml", 'w') as outfile:
    yaml.dump(params, outfile)

train = st.button("start model retraining")
if train:
    st.write('Model training in progess')