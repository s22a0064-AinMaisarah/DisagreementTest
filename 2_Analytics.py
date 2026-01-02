
import streamlit as st
import pandas as pd
import numpy as np

st.title("📈 Analytics")

data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["Traffic", "Conversion", "Revenue"]
)

st.line_chart(data)
