from libraries import *

# Function for PCA visualization
def visualize_pca(data):
    # Perform PCA
    pca = PCA(n_components=2)
    pca_result = pca.fit_transform(data)
    
    # Plot PCA results
    plt.figure(figsize=(8, 6))
    plt.scatter(pca_result[:,0], pca_result[:,1])
    plt.title('PCA Visualization')
    plt.xlabel('features')
    plt.ylabel('samples')
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()
    

# Function for exploratory data analysis (EDA)
def exploratory_data_analysis(data):
   
    melted_data = data.melt(var_name='Column')
    
    # Histogram
    plt.figure(figsize=(10, 6))
    sns.histplot(data=melted_data, x='value', hue='Column', kde=True, multiple='stack')
    plt.title('Histogram of all columns')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.legend(title='Column')
    st.pyplot()

    plt.figure(figsize=(10, 6))
    sns.kdeplot(data=melted_data, x='value', hue='Column', shade=True)
    plt.title('Density Plot of all columns')
    plt.xlabel('Value')
    plt.ylabel('Density')
    plt.legend(title='Column')
    st.pyplot()

    # Boxplot
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=melted_data, x='Column', y='value')
    plt.title('Boxplot of all columns')
    plt.xlabel('Column')
    plt.ylabel('Value')
    plt.xticks(rotation=45)  # Περιστροφή των ετικετών του x για καλύτερη αναγνώριση
    st.pyplot()

    


# Function for t-SNE visualization
def visualize_tsne(data):
    # Perform t-SNE
    tsne = TSNE(n_components=2)
    tsne_result = tsne.fit_transform(data)
    
    # Plot t-SNE results
    plt.figure(figsize=(8, 6))
    plt.scatter(tsne_result[:,0], tsne_result[:,1])
    plt.title('t-SNE Visualization')
    plt.xlabel('features')
    plt.ylabel('samples')
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()
    

# Main function to display the tab content
def Visualization_tab(data):
    
    st.title('2D Visualization Tab')

    # Dropdown for selecting visualization algorithm
    selected_algorithm = st.selectbox('Select Dimensionality Reduction Algorithm', ['PCA', 't-SNE'])
    
    if selected_algorithm == 'PCA':
        visualize_pca(data)
    elif selected_algorithm == 't-SNE':
        visualize_tsne(data)
    
    
    # Display exploratory data analysis
    st.header('Exploratory Data Analysis')
    exploratory_data_analysis(data)

