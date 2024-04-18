from libraries import *

'''
    Machine learing tab (Main Function)
'''

def Machine_Learning_tab(data):
    # Tab title
    st.title("Machine Learning Algorithms")
    
    # tab to select classifiers or clusters 
    ml_algorithm_type = st.selectbox(
    'Select type of machine learning algorithms',
    ('Classifiers', 'Clusters')
    )
    if ml_algorithm_type == 'Classifiers':
        classifiers(data)
    elif ml_algorithm_type == 'Clusters':
        clusters(data)


'''
        Classifiers
'''

    
def classifiers(data):
    # algorithm type
    st.write("# Classifiers")
    
    # classifiers inputs
    st.write("### Support Vector Machines")
    c = st.number_input("Enter the regularization parameter for the Support Vector Machines:", min_value=0.01, value=0.01)
    
    st.write("### K-Nearest Neighbors")
    k_neighbors = st.number_input("Enter the k neighbors for the K-Nearest Neighbors:", min_value=1, value=3)
    
    
    
    # Create a button to start the analysis
    if st.button("Start Analysis"):
        # Separate the features (K-1 columns) and the target (last column) from the data
        features = data.iloc[:, :-1]
        labels = data.iloc[:, -1]
        
        ## Classification accuracy scores
        svm_accuracy = run_support_vector_machines(features, labels, c)
        knn_accuracy = run_KNN(features, labels, k_neighbors)
        
        
        # format %
        svm_accuracy_per = svm_accuracy * 100
        knn_accuracy_per = knn_accuracy * 100
        
        
        # Evaluation Results in a dataframe:
        Eval_results = {"Classication Algorithm": ["Support Vector Machines","K-Nearest Neighbors"],
                               "Parameter": [f'{c}'+" (regularization parameter)",f'{k_neighbors}'+" (k-neighbors)"],
                               "Score": [f'{svm_accuracy:.4f}' ,f'{knn_accuracy:.4f}'],
                               "%": [f'{svm_accuracy_per:.2f}%',f'{knn_accuracy_per:.2f}%']
                               }
        
        # Display the evaluation results in a table
        st.write("Evaluation Results (Accuracy Score):")
        st.write(pd.DataFrame(Eval_results))
        best_accuracy,algorthm_name=best_acc_algorithm(Eval_results,'Classication Algorithm')
        st.write("Recommended Algorithm: `"+ algorthm_name +"`")
        st.write("Best Accuracy: `" +str(best_accuracy) + "`.")


def run_support_vector_machines(X,y,c):
    # Split the data into training and testing sets (70% training, 30% testing)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    # train the svm model and return accuracy
    svm = SVC(C=c)
    svm.fit(X_train, y_train)       
    y_pred = svm.predict(X_test)    
    accuracy = accuracy_score(y_test, y_pred)
    return accuracy

def run_KNN(X,y,k_neighbors):
    # Split the data into training and testing sets (70% training, 30% testing)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    # train the K-NN model and return accuracy
    knn = KNeighborsClassifier(n_neighbors=k_neighbors)
    knn.fit(X_train,y_train)
    y_pred = knn.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    return accuracy


'''
        Clusters
'''
def clusters(data):
    # algorithm type
    st.write("# Clusters")
    
    # Clusters inputs
    st.write("### Agglomerative Clustering")
    n_clusters_agg_clust = st.number_input("Enter the number of clusters for Agglomerative Clustering:", min_value=2, value=2)
    
    st.write("### Affinity Propagation")
    damping_aff_prop = st.number_input("Enter the bandwidth parameter for Affinity Propagation Clustering:", min_value=0.5,max_value=0.91, value=0.7)

    
    # Create a button to start the analysis
    if st.button("Start Analysis"):
        # Separate the features (K-1 columns) in case of labeled data
        features = data.iloc[:, :-1]
        
        # Clustering Silhouette Score
        agg_clust_labels,agg_clust_score = run_agglomerative_clustering(features,n_clusters_agg_clust)
        aff_prop_labels,aff_prop_score = run_affinity_propagation(features, damping_aff_prop)
        
        # format %
        agg_clust_per = agg_clust_score * 100
        aff_prop_per  = aff_prop_score  * 100
        
        # Evaluation Results in a dataframe:
        Eval_results = {"Cluster Algorithm": ["Agglomerative Clustering","Affinity Propagation"],
                               "Parameter": [f'{n_clusters_agg_clust}'+" (Clusters)",f'{damping_aff_prop:.2f}'+" (Damping)"],
                               "Score": [f'{agg_clust_score:.4f}' ,f'{aff_prop_score:.4f}'],
                               "%": [f'{agg_clust_per:.2f}%',f'{aff_prop_per:.2f}%']
                               }
        
        # Display the evaluation results in a table
        st.write("Evaluation Results (Silhouette Score):")
        st.write(pd.DataFrame(Eval_results))
        best_accuracy,algorthm_name=best_acc_algorithm(Eval_results,'Cluster Algorithm')
        st.write("Recommended Algorithm: `"+ algorthm_name +"`")
        st.write("Best Accuracy: `" +str(best_accuracy) + "`.")

def run_agglomerative_clustering(data, n_clusters):
    # train the agglomerative clustering model and return the predicted labels plus the silhouette_score
    agglomerative = AgglomerativeClustering(n_clusters=n_clusters)
    labels = agglomerative.fit_predict(data)
    score = silhouette_score(data, labels)
    return labels, score


def run_affinity_propagation(data,damping):
    # train the affinity propagation model and return the predicted labels plus the silhouette_score
    affinity_propagation = AffinityPropagation(damping=damping)
    affinity_propagation.fit(data)
    labels = affinity_propagation.labels_
    score = silhouette_score(data,labels)
    return labels,score




'''
    Gets the Evaluation results dataframe and what category is:
        - Classication Algorithm  
                    or 
        - Cluster Algorithm
    And returns the score and the name of the algorithm with the best accuracy score 
'''

def best_acc_algorithm(Eval_results,category):
    # From a dict into a pandas dataframe
    df = pd.DataFrame(Eval_results)     
    
    # get highest score index
    max_index = df['Score'].idxmax()    
    
    # locate the algorithm with the best accuracy and their accuracy
    best_accuracy  = df.loc[max_index,'%']
    algorithm_name = df.loc[max_index,category]
    return best_accuracy,algorithm_name





