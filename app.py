from libraries import * 

# Application title
st.title("2D Data Visualization - Machine learning application")
tabs = st.sidebar.radio("Tabs", ["DataFrame","2D Visualization","machine learning","info"])
uploaded_file = st.file_uploader("Upload a comma-separated csv file", type="csv")

# Check if a file has been uploaded
if uploaded_file is not None:

    # Read the uploaded file as a DataFrame using pandas
    data = pd.read_csv(uploaded_file, sep=',', header=0)
    
    # Display content based on selected tab (dataframe)
    if tabs == "DataFrame":
        DataFrame_tab(data)
    elif tabs == "2D Visualization":
        Visualization_tab(data)
    elif tabs == "machine learning":
        Machine_Learning_tab(data)
    elif tabs == "info":
        Info_tab()
        
