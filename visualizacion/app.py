import streamlit as st
import requests
import pandas as pd
from config import API_URL  # <--- importamos

st.title("Dashboard")

data = requests.get(API_URL).json()
df = pd.DataFrame(data)

st.dataframe(df)
st.write(df["salario"].mean())
