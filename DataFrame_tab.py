from libraries import *


def DataFrame_tab(data):
    
    '''
        Tab that lets the type of their data set 
        
        if it has labels:
            The Dataframe splits into 2 tables
                1. samples X features (SXF)
                2. labels (F+1)
        
        if it has no labels:
            The Dataframe stays as it is:
                1. samples X features (SXF)
    '''
    st.write("### Choose the type of your Dataframe:")
    st.write("#### (labels or no labels)")
    labels,no_labels = st.tabs(['Labels', 'no Labels'])
    with labels:
        Labels(data)
    with no_labels: 
        no_Labels(data)
    
def no_Labels(data):
    # no Labels title
    st.write("## Dataset with No Labels (SXF)")

    
    # Gets and writes the shape of the dataset
    st.write('Shape of dataset:', data.shape)
    
    # buttons to show - hide the dataFrame
    ## if no labels is selected then it shows only the features because it has no labels
    show_data = st.button('show table',key='show_button_no_labels')
    hide_data = st.button('hide table',key='hide_button_no_labels')
    if show_data == True and hide_data == False:
        st.write("## Samples X Features",data)
    elif show_data == False and hide_data == True:
        st.write("")
    
def Labels(data):
    # Labels title
    st.write("## Dataset with Labels (SXF) and (F+1)")

    
    # Extract the labels by popping the last column
    labels = data.iloc[:, -1]
    # Extract features by dropping the last column
    features = data.iloc[:, :-1]
    
    # Get and write shape of dataset, classes, number of classes
    unique_labels = np.unique(labels)
    st.write('Shape of dataset:', data.shape)
    st.write('Classes:',unique_labels)
    st.write('Number of classes:', len(unique_labels))
    
    # buttons to show - hide the dataFrame
    ## if labels is selected then it shows the features and the labels seperetely
    show_data = st.button('show tables',key='show_button_labels')
    hide_data = st.button('hide tables',key='hide_button_labels')
    if show_data == True and hide_data == False:
        st.write("## Samples X Features",features)
        st.write("## Labels",labels)
    elif show_data == False and hide_data == True:
        st.write("")