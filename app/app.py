from libraries import * 


tabs = st.sidebar.radio("Tabs", ["DataFrame","2D Visualization","machine learning","info"])
st.write("## upload a csv DataFrame (features + labels):")
uploaded_file = st.file_uploader("Upload a tab-separated csv file", type="csv")


# Check if a file has been uploaded
if uploaded_file is not None:
    # App title
    st.title("2D Data Visualization - Machine learning application")
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
        
