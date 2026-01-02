
import streamlit as st
import pandas as pd

st.title("🗂 Data Table")

df = pd.DataFrame({
    "Name": ["Ain", "Ali", "Sara", "Adam"],
    "Score": [85, 90, 78, 92]
})

st.dataframe(df)
