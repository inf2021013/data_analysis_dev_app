

'''
    Application main libraries:
'''
import streamlit as st
import pandas as pd
import numpy as np

'''
    machine learning tab:
'''
from sklearn.model_selection import train_test_split # train - test split
from sklearn.metrics import silhouette_score         # silhouette_score
from sklearn.metrics import accuracy_score           # accuracy score

# classifiers
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

# clusters
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import AffinityPropagation

'''
    visualization tab:
'''
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import seaborn as sns

'''
    Importing all tabs:
'''
from Machine_Learning_tab import Machine_Learning_tab
from Info_tab import Info_tab
from Visualization_tab import Visualization_tab
from DataFrame_tab import DataFrame_tab

