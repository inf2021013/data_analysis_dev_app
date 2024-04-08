import streamlit as st
import pandas as pd
import numpy as np
from machine_learning_tab import machine_learning_tab



uploaded_file = st.file_uploader("Upload a tab-separated csv file", type="csv")
# Check if a file has been uploaded
if uploaded_file is not None:
    machine_learning_tab(uploaded_file)
    

