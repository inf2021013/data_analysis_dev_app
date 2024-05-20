from libraries import *

'''
    Machine learing tab (Main Function)
'''

def Machine_Learning_tab(data):
    # Tab title
    st.title("Machine Learning Algorithms")
    # tab to select classifiers or clusters 
    Classifiers,Clusters = st.tabs(
    ['Classifiers', 'Clusters']
    )
    
    with Classifiers:
        classifiers(data)
    with Clusters:
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
    if st.button("Start Analysis",key="classifiers"):
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
        st.write("""
             #### SVM vs KNN
             O SVM και ο KNN είναι δύο αρκετά χρήσιμοι αλγόριθμοι κατηγοριοποίησης, δηλαδή για την εκπαίδευση δεδομένων που παρέχουν labels.
             Ωστόσο, ύπαρχουν περιπτώσεις που η ακρίβεια και η ποιότητα τους, μπορεί να διαφέρει σε διαφορετικού είδους δεδομένα.
             
             ##### SVM χρησιμότητα 
             Πιο συγκεκριμένα, στην προσέγγιση του support vector machine (SVM) approach βρίσκουμε
             ένα μονοπάτι για να χωρίσουμε τα δεδομένα σε δύο κλάσεις. Ο αλγόριθμος βρίσκει την ευρύτερη δυνατή διαδρομή 
             (για να μεγιστοποιήσει την ακρίβεια του μέσω της παράμετρος regularization). Τέλος, τα δεδομένα θα πρέπει να έχουν κανονικοποιηθεί.

             
             ##### ΚΝΝ χρησιμότητα
             Ο KNN είναι ένας απλός αλγόριθμος που κατηγοριοποιεί νέα δεδομένα με βάση την ομοιότητα των χαρακτηριστικών τους, με τα χαρακτηριστικά των k πλησιέστερων γειτόνων της στα train data.
             Πιο συγκεκριμένα, η παράμετρος k καθορίζει πόσοι γείτονες λαμβάνονται υπόψη για την ομοιότητα αυτή που μπορεί να μετρηθεί με βάση το μέγεθος της απόστασης τους. 
             
             ##### Σε ποια περίπτωση είναι ο καθένας πιο ιδανικός?
             Ο svm αλγόριθμος είναι πιο ακριβείς σε δεδομένα υψηλής διάστασης και αραιά δεδομένα, καθώς και ιδανικός στο ελαχιστοποιεί τα errors και να αποφεύγει το να γίνει overfitting 
             αλλά είναι αρκετά δύσκολος να υλοποιηθεί καθώς χρειάζεται αρκετές διαφοροποιήσεις στην regularization παράμετρό μέχρι να δώσει την βέλτιστη ακρίβεια.
             Ωστόσο, όμως ο knn είναι αρκετά εύκολος στην κατανόηση του και στην υλοποιήση του καθώς και ιδανικός στο να χειρίζεται αρκετά καλά νέα δεδομένα, 
             αλλά είναι αρκετά αργός και δυσκολεύται στο να βρεί καλά αποτελέσματα σε μεγάλα datasets.
             """)


def run_support_vector_machines(X,y,c):
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
    st.write("### Agglomerative Hierachical Clustering")
    n_clusters_agg_clust = st.number_input("Enter the number of clusters for Agglomerative Hierachical Clustering:", min_value=2, value=2)
    
    st.write("### Affinity Propagation")
    similarity_between_data_points = st.number_input("Enter the bandwidth parameter for Affinity Propagation Clustering:", min_value=0.5,max_value=0.91, value=0.7)

    
    # Create a button to start the analysis
    if st.button("Start Analysis",key="clusters"):
        
        try:
            st.write("""
                 ```
                    WARNING:
                    the results may not be correct if your dataset already has labels
                    (ex. 0 or 1)
                 ```                   
                 """)
            # Clustering Silhouette Score
            agg_clust_labels,agg_clust_score = run_agglomerative_clustering(data,n_clusters_agg_clust)
            aff_prop_labels,aff_prop_score = run_affinity_propagation(data, similarity_between_data_points)
            
            # format %
            agg_clust_per = agg_clust_score * 100
            aff_prop_per  = aff_prop_score  * 100
            
            # Evaluation Results in a dataframe:
            Eval_results = {"Cluster Algorithm": ["Agglomerative Hierachical Clustering","Affinity Propagation"],
                                "Parameter": [f'{n_clusters_agg_clust}'+" (Clusters)",f'{similarity_between_data_points:.2f}'+" (Damping)"],
                                "Score": [f'{agg_clust_score:.4f}' ,f'{aff_prop_score:.4f}'],
                                "%": [f'{agg_clust_per:.2f}%',f'{aff_prop_per:.2f}%']
                                }
            
            # Display the evaluation results in a table
            st.write("Evaluation Results (Silhouette Score):")
            st.write(pd.DataFrame(Eval_results))
            best_accuracy,algorthm_name=best_acc_algorithm(Eval_results,'Cluster Algorithm')
            st.write("Recommended Algorithm: `"+ algorthm_name +"`")
            st.write("Best Accuracy: `" +str(best_accuracy) + "`.")
            st.write("""
                #### Agglomerative Hierachical Clustering vs Affinity Propagation
                O Agglomerative Hierachical Clustering  και ο Affinity Propagation είναι δύο πολύ χρήσιμοι αλγόριθμοι ομαδοποίησης δεδομένων, 
                δηλαδή για την εκπαίδευση δεδομένων που δεν παρέχουν labels αλλά βγάζουν οι ίδιοι labels ως αποτέλεσμα.
                Απο την άλλη μεριά, είναι περιπτώσεις που η ακρίβεια και η ποιότητα τους, μπορεί να διαφέρει σε διαφορετικού είδους δεδομένα.
                
                ##### Agglomerative Hierachical Clustering χρησιμότητα 
                Πιο συγκεκριμένα, όσον αφορά τον Agglomerative Hierachical Clustering, αρχικά υπολογίζει όλες τις αρχικές αποστάσεις μεταξύ datapoints σε ένα πίνακα με βάση μία ιεραρχία.
                Έπειτα, ενώνει το ζευγάρι από clusters σε 1 cluster που έχει την κοντινότερη απόσταση μεταξύ datapoints και κάνει update τις αποστάσεις του αρχικού πίνακα.
                Ο αλγόριθμος επαναλαμβάνεται ώσπου να συναντήσει τον απαιτούμενο αριθμό clusters που χρειαζόμαστε.
                

                ##### Affinity Propagation χρησιμότητα
                Ο Affinity Propagation είναι ένας απλός αλγόριθμος που κατηγοριοποιεί νέα δεδομένα με βάση την ομοιότητα των χαρακτηριστικών τους, με τα χαρακτηριστικά των k πλησιέστερων γειτόνων της στα train data.
                Πιο συγκεκριμένα, η παράμετρος k καθορίζει πόσοι γείτονες λαμβάνονται υπόψη για την ομοιότητα αυτή που μπορεί να μετρηθεί με βάση το μέγεθος της απόστασης τους. 

                Ο Affinity Propagation βασίζεται στην ιδέα της ανταλλαγής μηνυμάτων μεταξύ των datapoints για την εύρεση του συνόλου των κέντρων (exemplars).
                Αρχικά, όλα τα datapoints στέλνουν και λαμβάνουν μηνύματα σχετικά με το πόσο κατάλληλο είναι κάθε άλλο datapoint για να είναι το κέντρο του.
                Οι ανταλλαγές αυτών των μηνυμάτων συνεχίζονται, ενημερώνοντας σταδιακά τις προτιμήσεις και την ευθύνη κάθε σημείου.
                Τελικά, η διαδικασία φτάνει στο τέλος της, έχοντας καθορίσει ποια σημεία θα είναι τα κέντρα και ποια θα ανήκουν σε κάθε cluster.
                Ο αλγόριθμος επαναλαμβάνεται έως ότου επιτευχθεί μια σταθερή λύση, χωρίς να είναι αναγκαίο να ορίσουμε τον αριθμό των clusters.

                
                ##### Σε ποια περίπτωση είναι ο καθένας πιο ιδανικός?
                Ο αλγόριθμος Agglomerative Hierarchical Clustering είναι απλός και πιο αποτελεσματικός 
                όταν γνωρίζουμε τον αριθμό των clusters καθώς και όταν έχουμε μικρότερα datasets 
                με καλά διαχωρισμένα clusters, καθώς μπορεί να δημιουργήσει μια σαφή ιεραρχία των δεδομένων. 
                Ωστόσο, δεν είναι τόσο αποδοτικός και ακριβείς σε πολύ μεγάλα datasets.
                
                Από την άλλη πλευρά, ο αλγόριθμος Affinity Propagation είναι πόλυ χρήσιμος
                όταν δεν γνωρίζουμε τον αριθμό των clusters καθώς είναι ιδανικός και προσφέρει αρκετή ευελιξία 
                όταν έχουμε πολύπλοκα και αρκετά μεγάλα datasets, παρά τους πολλούς υπολογισμούς που πραγματοποιεί λόγω της ανταλλαγής μηνυμάτων.
                """)
        except ValueError as e:
            # if it has strings in the labels, it shows a specific error message
            if str(e).startswith("could not convert string to float:"):
                st.error("An error occurred: your dataframe already has labels (strings)")
            else:
                raise e

def run_agglomerative_clustering(data, n_clusters):
    # train the agglomerative clustering model and return the predicted labels plus the silhouette_score
    agglomerative = AgglomerativeClustering(n_clusters=n_clusters)
    labels = agglomerative.fit_predict(data)
    score = silhouette_score(data, labels)
    return labels, score


def run_affinity_propagation(data,similarity_between_data_points):
    # train the affinity propagation model and return the predicted labels plus the silhouette_score
    affinity_propagation = AffinityPropagation(damping=similarity_between_data_points)
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
    print(df['Score'])
    # locate the algorithm with the best accuracy and their accuracy
    best_accuracy  = df.loc[max_index,'%']
    algorithm_name = df.loc[max_index,category]
    return best_accuracy,algorithm_name





