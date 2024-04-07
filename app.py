import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split # train - test
from sklearn.linear_model import LogisticRegression  # model
from sklearn.metrics import accuracy_score           # accuracy score




uploaded_file = st.file_uploader("Upload a tab-separated csv file", type="csv")
# Check if a file has been uploaded
if uploaded_file is not None:
    # Read the uploaded file as a DataFrame using pandas
    data = pd.read_csv(uploaded_file, sep=',', header=None)
    st.dataframe(data)
    


def run_Logistic_regression(data):
    train,test,train_labels,test_labels = train_test_split()
    pass