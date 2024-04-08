from sklearn.model_selection import train_test_split # train - test
from sklearn.linear_model import LogisticRegression  # model
from sklearn.metrics import accuracy_score           # accuracy score
import streamlit as st
import pandas as pd
import numpy as np


def machine_learning_tab(uploaded_file):
    # Read the uploaded file as a DataFrame using pandas
    data = pd.read_csv(uploaded_file, sep=',', header=None)
    st.dataframe(data)