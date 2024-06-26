"""This module helps to load the data."""

# Import necessary modules.
import pandas as pd
import streamlit as st

# Load the dataset.
@st.cache_data()
def load_data(): 
    # read the dataset.
    df = pd.read_csv("/workspaces/price_prediction/final_data.csv")