from libraries import * 


def Info_tab():
    st.write("""
# Info Tab

## General App Information

Η συγκεκριμένη εφαρμογή χρησιμοποιείται για την οπτικοποίηση δεδομένων και σύγκριση αλγορίθμων μηχανική μάθησης όπου για να επιτευχθεί αυτή η λειτουργία γίνεται χρήση του εργαλείου Streamlit. Πιο συγκεκριμένα, η εφαρμογή υποστηρίζει διάφορες λειτουργίες όπως: 
  - Φόρτωση tabular δεδομένων (.csv).
  - Προδιαγραφές πινάκων (Dataframes). 
  - 2D οπτικοποιήσεις βασισμένες σε διαφορετικούς αλγορίθμους.
  - Mηχανική Mάθηση όπου δίνονται δύο επιλογές ειδών αλγορίθμων για τον χρήστη (κατηγοριοποίησης ή ομαδοποίησης) όπου μπορεί να πραγματοποιηθεί και σύγκριση των προαναφερόμενων αλγορίθμων με σκοπό την εύρεση του πιο αποδοτικού. 
  - Μια παρουσίαση του τρόπου λειτουργίας της εφαρμογής (Η συγκεκριμένη σελίδα).

## How to Use it?

Η χρήση της εφαρμογής είναι απλοϊκή και εύκολα κατανοητή για όλους. Αρχικά ο χρήστης θα χρειαστεί να ανεβάσει τα δεδομένα που θέλει σε μορφή `CSV, Excel`. Έπειτα από αυτό ο χρήστης μπορεί να αποφασίσει ποια λειτουργία της εφαρμογής θέλει να εκμεταλευτεί. Στα αριστερά του ανοιχτού παραθύρου βρίσκονται οι ακόλουθες επιλογές: `DataFrame_tab, Visualization_tab, Machine_Learning_tab, Info_tab` με κάθε μια από αυτές να εκτελεί μια διαφορετική λειτουργία με λεπτομερής περιγραφή παρακάτω:

### Data Frame tab:

Εάν ο χρήστης ενδιαφέρεται για την `εμφάνιση του Dataset` του σε μορφή πινάκων τότε επιλέγοντας την DataFrame_tab μπορεί να το επισκοπήσει. Αρχικά εμφανίζονται διάφορες πληροφορίες για το Dataset του και έπειτα του δίνεται η επιπλέον επιλογή για τον τρόπο παρουσίασης του Data set με ή χωρίς labels. 

#### Labels επιλογή
Αν επιλέξει την επιλογή labels διαχωρίζει το Dataset του δύο κομμάτια, σε `Samples X Features` και `Labels` παίρνοντας την τελευταία στήλη του Dataset:

![dataframe_labels](https://github.com/inf2021013/test/assets/166173503/b6abd089-b0bd-43bf-b307-4f77eb2f5705)


#### Νo labels επιλογή
Αν επιλέξει την επιλογή no labels τότε εμφανίζει ολόκληρο το Dataset, σε `Samples X Features`.

![dataframe_no_labels](https://github.com/inf2021013/test/assets/166173503/2b1a60cd-356c-4382-9659-c9b63ba5fd4b)

### Visualization tab:

Εάν ο χρήστης επιθυμεί να εκτελέσει 2D οπτικοποιήση βασισμένη σε δύο αλγορίθμους μείωσης διάστασης (PCA,t-SNE) μπορεί να επιλέξει την Visualization_tab. Εδώ με την χρήση των δεδομένων που παρείχε στο αρχικό βήμα ο χρήστης δημιουργούνται και εμφανίζονται οι οπτικοποιήσεις τους ανάλογα με τον αλγόριθμο που έχει επιλέξει.

- Οι δύο αλγόριθμοι που προσφέρονται είναι οι PCA και t-SNE.
- Επιπρόσθετα παρουσιάζονται 3 διαγράμματα exploratory data analysis (EDA), αναλυτικότερα, ένα ιστόγραμμα (Histogram), ένα διάγραμμα πυκνότητας (Density) και ένα διάγραμμα Boxplot βασιμσένα στα παρεχόμενα δεδομένα του χρήστη.

### Machine Learning tab:

Εάν ο χρήστης θέλει να υλοποιήσει και να συγκρίνει αλγορίθμους Μηχανικής Μάθησης μπορεί να επιλέξει το Machine_Learning_tab. Εδώ του δίνεται η δυνατότητα να διαλέξει ανάμεσα σε αλγορίθμους κατηγοριοποίησης (Support Vector Machines, K-Nearest Neighbors) και αλγορίθμους ομαδοποίησης (Agglomerative Clustering, Affinity Propagation). Αφότου επιλέξει τους επιθυμητούς αλγορίθμους χρειάζεται να παρέχει τιμή για την μεταβλητή κάθε αλγορίθμου

#### **Αλγορίθμοι Κατηγοριοποίησης:**

**Xρειάζεται να παρέχει:**

- **α)** την regularization C παράμετρο για τον Support Vector Machines,
- **β)** των k αριθμό γειτόνων για την K-Nearest Neighbors

#### **Αλγορίθμοι Ομαδοποίησης:**

**Xρειάζεται να παρέχει:**

- **α)** των αριθμό των clusters για τον Agglomerative Clustering,
- **β)** το bandwidth της παραμέτρου για τον Affinity Propagation Clustering.

Επιπλέον μπορεί να συγκρίνει την αποδοτικότητα των αλγορίθμων και να βρει τον πιο αποδοτικό για κάθε περίπτωση πατώντας το **"Start Analysis"**. Έπειτα από ενα μικρό χρονικό διάστημα θα εμφανιστούν οι αποδόσεις των δύο επιλεγμένων αλγορίθμων καθώς και ποιος από τους δύο είχε την καλύτερη απόδοση και το ποσοστό της ακρίβειας του.

### Info tab:

Τέλος εάν ο χρήστης χρειάζεται βοήθεια για τον τρόπο λειτουργίας της εφαρμογής ή θέλει να δει γενικές πληροφορίες για αυτήν μπορεί να επιλέξει την Info_tab. Εδώ προσφέρονται γενικές πληροφορίες της εφαρμογής, ο τρόπος λειτουργίας της και η ομάδα ανάπτυξής της καθώς και ποια tasks ανέλαβε και ολοκλήρωσε κάθε μέλος της.

## Team Members

Η ομάδα ανάπτυξης της εφαρμογής αποτελείται από τον Νικόλα Αναγνωστόπουλο, τον Αχιλλέα Ζερβό και τον Παναγιώτη Μουρελάτο, φοιτητές του Ιονίου Πανεπιστημίου στο 3ο έτος της φοιτησής τους.

## Tasks Completed by each member

- ### Data Frame
  Την ανάπτυξη του Data Frame ανέλαβε και ολοκλήρωσε ο Νικόλας Αναγνωστόπουλος με ΑΜ: inf2021013 

- ### Visualization
  Την ανάπτυξη του Visualization ανέλαβε και ολοκλήρωσε ο Αχιλλέας Ζερβός με ΑΜ: inf2021055
- ### Machine Learning
  Την ανάπτυξη του Machine Learning ανέλαβε και ολοκλήρωσε ο Νικόλας Αναγνωστόπουλος με ΑΜ: inf2021013
- ### Info
  Την ανάπτυξη του Info ανέλαβε και ολοκλήρωσε ο Παναγιώτης Μουρελάτος με ΑΜ: inf2021147

## github profiles (application repo):
#### organization:
  - Ομάδα: [github/TechTeam-inf2021](https://github.com/TechTeam-inf2021/data_analysis_dev_app)
#### members:
  - Παναγιώτης Μουρελάτος: [github/PanMour](https://github.com/PanMour/data_analysis_dev_app)
  - Νικόλας Αναγνωστόπουλος: [github/inf2021013](https://github.com/inf2021013/data_analysis_dev_app)
  - Αχιλλέας Ζερβός: [github/inf2021055](https://github.com/Axileaszervos/data_analysis_dev_app)
""")
      