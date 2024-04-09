from libraries import * 


tabs = st.sidebar.radio("Navigation", ["2D Visualization","machine learning","info"])
uploaded_file = st.file_uploader("Upload a tab-separated csv file", type="csv")

# Check if a file has been uploaded
if uploaded_file is not None:
    
    # 
    st.write("## features")
    # Read the uploaded file as a DataFrame using pandas
    data = pd.read_csv(uploaded_file, sep=',', header=None)
    show_data = st.button('show table')
    hide_data = st.button('hide table')
    if show_data == True and hide_data == False:
        st.dataframe(data)
        
    elif show_data == False and hide_data == True:
        st.write("")
    
    # Display content based on selected tab
    if tabs == "machine learning":
        machine_learning_tab(uploaded_file)
    elif tabs == "info":
        info_tab()
        
