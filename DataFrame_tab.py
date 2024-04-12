from libraries import *


def DataFrame_tab(data):
    # The data frame split into 2 tables
    # 1. samples X features (SXF)
    # 2. labels (F+1) 
    st.write("## DataFrame, samples X features + labels")
    
    # Extract the labels by popping the last column
    labels = data.iloc[:, -1]

    # Extract features by dropping the last column
    features = data.iloc[:, :-1]
    
    # buttons to show - hide the dataFrame
    show_data = st.button('show table',key='show_button')
    hide_data = st.button('hide table',key='hide_button')
    if show_data == True and hide_data == False:
        st.write("## Features",features)
        st.write("## Labels",labels)
    elif show_data == False and hide_data == True:
        st.write("")
    