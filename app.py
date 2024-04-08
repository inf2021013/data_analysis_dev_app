import streamlit as st
import pandas as pd
import numpy as np
from machine_learning_tab import machine_learning_tab
from hello import hello_tab

tabs = st.sidebar.radio("Navigation", ["machine learning", "hello"])
uploaded_file = st.file_uploader("Upload a tab-separated csv file", type="csv")

# Check if a file has been uploaded
if uploaded_file is not None:
    # Display content based on selected tab
    if tabs == "machine learning":
        machine_learning_tab(uploaded_file)
    elif tabs == "hello":
        hello_tab()

