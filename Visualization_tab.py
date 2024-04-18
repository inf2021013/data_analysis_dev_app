from libraries import *

# Function for PCA visualization
def visualize_pca(data):
    # t-SNE title
    st.write("## PCA algorithm")
    
    # Perform PCA and fits dataset
    pca = PCA(n_components=2)
    pca_result = pca.fit_transform(data)
    
    # Plot PCA results
    plt.figure(figsize=(8, 6))
    plt.scatter(pca_result[:,0], pca_result[:,1])
    
    # set title, x-label, y-label names
    plt.title('PCA Visualization')
    plt.xlabel('features')
    plt.ylabel('samples')
    
    # for streamlit pyplot
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()
    
# Function for t-SNE visualization
def visualize_tsne(data):
    # t-SNE title
    st.write("## t-SNE algorithm")
    
    # Perform t-SNE and fits dataset
    tsne = TSNE(n_components=2)
    tsne_result = tsne.fit_transform(data)
    
    # Plot t-SNE results
    plt.figure(figsize=(8, 6))
    plt.scatter(tsne_result[:,0], tsne_result[:,1])
    
    # set title, x-label, y-label names
    plt.title('t-SNE Visualization')
    plt.xlabel('features')
    plt.ylabel('samples')
    
    # for streamlit pyplot
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()
    


# Function for exploratory data analysis (EDA)
def exploratory_data_analysis(data,dataset_name):
    '''
        3 plots:
            - Histogram
            - Density
            - Boxplot
    '''
    # connects the dataset into a single column named 
    melted_data = data.melt(var_name=dataset_name)
    
    # Histogram
    plt.figure(figsize=(10, 6))
    sns.histplot(data=melted_data, x='value', hue=dataset_name, kde=True, multiple='stack')
    plt.title('Histogram of all columns')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.legend(title=dataset_name)
    st.pyplot()

    # Density
    plt.figure(figsize=(10, 6))
    sns.kdeplot(data=melted_data, x='value', hue=dataset_name, shade=True)
    plt.title('Density Plot of all columns')
    plt.xlabel('Value')
    plt.ylabel('Density')
    plt.legend(title=dataset_name)
    st.pyplot()

    # Boxplot
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=melted_data, x=dataset_name, y='value')
    plt.title('Boxplot of all columns')
    plt.xlabel(dataset_name)
    plt.ylabel('Value')
    plt.xticks(rotation=45)  
    st.pyplot()

    




# Main function to display the tab content
def Visualization_tab(data,dataset_name):
    
    # visualization tab title
    st.title('2D Visualization Tab')

    # Extract the labels by popping the last column
    labels = data.iloc[:, -1]
    # Extract features by dropping the last column
    features = data.iloc[:, :-1]
    
    # if the labels column is has any string then we encode this columns in numbers
    has_string = labels.dtype == 'object'
    if has_string:
        labels_encoded = labels.astype('category').cat.codes
        
        # we give to the encoded labels column name the labels column name
        labels_encoded.name = labels.name
        
        # we connect the encoded labels to the features dataset
        data = pd.concat([features,labels_encoded], axis=1)
    
    # Dropdown for selecting visualization algorithm (PCA) or (t-SNE)
    selected_algorithm = st.selectbox('Select Dimensionality Reduction Algorithm', ['PCA', 't-SNE'])
    if selected_algorithm == 'PCA':
        visualize_pca(data)
    elif selected_algorithm == 't-SNE':
        visualize_tsne(data)
    
    
    # Display exploratory data analysis
    st.header('Exploratory Data Analysis')
    exploratory_data_analysis(data,dataset_name)

