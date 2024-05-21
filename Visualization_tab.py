from libraries import *

# Function for PCA visualization
def visualize_pca(data,labels_names):
    # t-SNE title
    st.write("## Αλγόριθμος PCA")
    st.write("### Plot:")
    # Perform PCA and fits dataset
    pca = PCA(n_components=2)
    pca_result = pca.fit_transform(data)
    
    # get unique labels names
    unique_labels_names = np.unique(labels_names)
    
    # create plt fig
    plt.figure(figsize=(8, 6))
        
    # Plot PCA results
    try:
        # if there are labels it plots the data with different colors
        
        # each label point gets a different color
        for label in unique_labels_names:
            plt.scatter(pca_result[labels_names == label, 0], pca_result[labels_names == label, 1], 
                        label=label, cmap='viridis')
            
        # Display labels in right corner
        plt.legend(title='Labels', loc='center left', bbox_to_anchor=(1, 0.5))
    except:
        # if there are no labels it plots the data with the same color
        plt.scatter(pca_result[:,0], pca_result[:,1],color='blue')
    
    # set title, x-label, y-label names
    plt.title('PCA Visualization')
    plt.xlabel('features')
    plt.ylabel('features')

    # for streamlit pyplot
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()
    
    st.write("""
             ## Λειτουργία και Χρησιμότητα 
             Ο αλγόριθμος PCA είναι μια δημοφιλής τεχνική μείωσης διάστασης
             που χρησιμοποιείται για την ανάλυση και την απλοποίηση σύνθετων δεδομένων υψηλής διάστασης. 
             Η κύρια λειτουργία του συγκεκριμένου αλγορίθμου είναι ο μετασχηματισμός των αρχικών δεδομένων σε ένα νέο σύνολο μεταβλητών, 
             τις κύριες συνιστώσες, οι οποίες είναι και γραμμικοί συνδυασμοί των αρχικών μεταβλητών. 
             Αυτές οι κύριες συνιστώσες διατηρούν όσο το δυνατόν περισσότερη πληροφορία από τα δεδομένα, 
             επιτρέποντας να αφαιρεθούν τα περιττά στοιχεία και οι παρεμβολές.
             Τέλος, βοηθά αρκετά στην οπτικοποίηση των δεδομένων, 
             ενώ ταυτόχρονα βελτιώνει την απόδοση των αλγορίθμων μηχανικής μάθησης 
             μειώνοντας τον αριθμό των διαστάσεων.
             """)
    
# Function for t-SNE visualization
def visualize_tsne(data,labels_names):
    # t-SNE title
    st.write("## Αλγόριθμος t-SNE")
    st.write("### Plot:")
    # Perform t-SNE and fits dataset
    tsne = TSNE(n_components=2)
    tsne_result = tsne.fit_transform(data)
    
    # get unique labels names
    unique_labels_names = np.unique(labels_names)
    
    # create plt fig
    plt.figure(figsize=(8, 6))
        
    # Plots T-SNE results
    try:
        # if there are labels it plots the data with different colors
        
        # each label point gets a different color
        for label in unique_labels_names:
            plt.scatter(tsne_result[labels_names == label, 0], tsne_result[labels_names == label, 1], 
                        label=label, cmap='viridis')
            
        # Display labels in right corner
        plt.legend(title='Labels', loc='center left', bbox_to_anchor=(1, 0.5))
    except:
        # if there are no labels it plots the data with the same color
        plt.scatter(tsne_result[:,0], tsne_result[:,1],color='blue')
    
    # set title, x-label, y-label names
    plt.title('T-SNE Visualization')
    plt.xlabel('features')
    plt.ylabel('features')

    # for streamlit pyplot
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()
    st.write("""
             ### Λειτουργία και Χρησιμότητα 
             Ο αλγόριθμος t-SNE είναι πολύ χρήσιμος σε όσους χρήστες επιθυμούν 
             να οπτικοποιήσουν υψηλής διάστασης δεδομένα. 
             Πρόκειται για εικόνες, κείμενα ή μεγάλα σύνολα δεδομένων,
             ο t-SNE μπορεί να μειώσει τις διαστάσεις τους σε 2 ή 3, 
             αποκαλύπτοντας κρυφές σχέσεις, μοτίβα και συγκεντρώσεις 
             που δεν είναι εμφανείς με άλλες μεθόδους. 
             Με τη βοήθειά του, οι χρήστες μπορούν να εντοπίσουν ανωμαλίες 
             και να αναγνωρίσουν ομάδες με παρόμοια χαρακτηριστικά.
             Με λίγα λόγια είναι ένα πολύ χρήσιμο εργαλείο στην σύγχρονη ανάλυση δεδομένων και την μηχανική μάθηση.
             """)
    


def Histogram_plot(data,dataset_name):
    # if Histogram Plot tab is select it plots a histogram
    st.write("## Histogram Graph")
    st.write("### Plot:")
    plt.figure(figsize=(10, 6))
    sns.histplot(data, x='value', hue=dataset_name, kde=True, multiple='stack')
    plt.title('Histogram of all columns')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.legend(title=dataset_name)
    st.pyplot()
    st.write("""
             ### Λειτουργία και Χρησιμότητα 
             Το Ιστόγραμμα είναι ένα γράφημα που δείχνει την συχνότητα εμφάνισης των
             διαφορετικών τιμών σε ένα σύνολο δεδομένων. 
             Κάθε στήλη του ιστογράμματος αντιστοιχεί σε ένα διάστημα τιμών,
             ενώ το ύψος της στήλης, αντιπροσωπεύει τον αριθμό των παρατηρήσεων που πέφτουν 
             εντός αυτού του διαστήματος.
             """)


def Density_plot(data,dataset_name):
    # if Density Plot tab is select it plots a Density Plot
    st.write("## Density Graph")
    st.write("### Plot:")
    plt.figure(figsize=(10, 6))
    sns.kdeplot(data, x='value', hue=dataset_name, shade=True)
    plt.title('Density Plot of all columns')
    plt.xlabel('Value')
    plt.ylabel('Density')
    plt.legend(title=dataset_name)
    st.pyplot()
    st.write("""
             ### Λειτουργία και Χρησιμότητα 
             Η πυκνότητα (Density) δεδομένων δείχνει το πόσο συχνά εμφανίζονται διάφορες τιμές 
             κατά μήκος μιας συνεχούς μεταβλητής, 
             παρέχοντας έτσι μια εικόνα της συγκέντρωσης ή της διασποράς των δεδομένων. 
             Με λίγα λόγια, παρουσιάζει το πόσο συχνά εμφανίζονται οι τιμές των δεδομένων κατά μήκος μιας συνεχούς μεταβλητής.
             """)
    
def Box_plot(data,dataset_name):
    # if Boxplot tab is select it plots a Boxplot
    st.write("## Boxplot Graph")
    st.write("### Plot:")
    plt.figure(figsize=(10, 6))
    sns.boxplot(data, x=dataset_name, y='value')
    plt.title('Boxplot of all columns')
    plt.xlabel(dataset_name)
    plt.ylabel('Value')
    plt.xticks(rotation=45)  
    st.pyplot()
    st.write("""
             ### Λειτουργία και Χρησιμότητα 
             Το Boxplot παρουσιάζει πέντε βασικές πληροφορίες για ένα σύνολο δεδομένων: 
                - Μέση τιμή (mean)
                - Πρώτο και Τρίτο Τεταρτημόριο (που ορίζουν τα όρια του Βox)
                - Διακύμανση (variance)
                - Πιθανή παρουσία υπερβολικά υψηλών τιμών
             """)



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
    
    '''
        Data analysis - visualization tabs for users to choose from:
            - DRA: Dimensionality Reduction Algorithms (ex. PCA, T-SNE)
            - EDA: Exploratory Data Analysis (ex. histogram, density plot, boxplot)
    ''' 
    DRA,EDA = st.tabs(["Dimensionality Reduction Algorithms","Exploratory Data Analysis"])
    
    with DRA:
        st.header("Select Dimensionality Reduction Algorithm (PCA, T-SNE)")
        PCA,TSNE = st.tabs(["PCA","t-SNE"])
        with PCA:
            visualize_pca(data,labels)
        with TSNE:
            visualize_tsne(data,labels)
    
    with EDA:
        st.header('Exploratory Data Analysis')
        histogramplot,Densityplot,Boxplot = st.tabs(["Histogram","Density","Boxplot"])
        '''
        3 plots:
            - Histogram
            - Density plot
            - Boxplot
        '''
        # connects the dataset into a single column named 
        melted_data = data.melt(var_name=dataset_name)
        # Display exploratory data analysis
        with histogramplot:
            Histogram_plot(melted_data,dataset_name)
            
        with Densityplot:
            Density_plot(melted_data,dataset_name)
        
        with Boxplot:
            Box_plot(melted_data,dataset_name)
