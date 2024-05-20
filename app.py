from libraries import * 


# Application title

st.set_page_config(page_title="2D Data Visualization - Machine learning application")
st.title("2D Data Visualization - Machine learning application")
uploaded_file = st.file_uploader("Upload a comma-separated csv file", type="csv")
dataFrame_tab,visualization_tab,machine_Learning_tab,info_tab = st.tabs(["DataFrame","2D Visualization","Machine Learning","info"])




with info_tab:
    Info_tab()
# Check if a file has been uploaded
if uploaded_file is not None:

    # Read the uploaded file as a DataFrame using pandas
    data = pd.read_csv(uploaded_file, sep=',', header=0)
    
    # get dataset name
    dataset_name = uploaded_file.name.replace('.csv','').replace('_',' ')
    # Display content based on selected tab (dataframe)
    with dataFrame_tab:
        DataFrame_tab(data)
    with visualization_tab:
        Visualization_tab(data,dataset_name)
    with machine_Learning_tab:
        Machine_Learning_tab(data)
    
            
 
