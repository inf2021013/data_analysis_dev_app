import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split # train - test
from sklearn.linear_model import LogisticRegression  # model
from sklearn.metrics import accuracy_score           # accuracy score
from machine_learning_tab import machine_learning_tab
from info_tab import info_tab