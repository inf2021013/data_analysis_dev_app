from libraries import *


def machine_learning_tab(uploaded_file):
    # Read the uploaded file as a DataFrame using pandas
    data = pd.read_csv(uploaded_file, sep=',', header=None)
    st.dataframe(data)