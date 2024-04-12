
# application libraries:
import streamlit as st
import pandas as pd
import numpy as np

# for machine learning tab
from sklearn.model_selection import train_test_split # train - test
from sklearn.linear_model import LogisticRegression  # model
from sklearn.metrics import accuracy_score           # accuracy score

# for data visualization tab


# import the 4 tabs
from Machine_Learning_tab import Machine_Learning_tab
from Info_tab import Info_tab
from Visualization_tab import Visualization_tab
from DataFrame_tab import DataFrame_tab