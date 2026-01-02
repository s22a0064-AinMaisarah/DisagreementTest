
import streamlit as st

st.title("📊 Overview")

st.metric("Users", 1200, "+8%")
st.metric("Sales", "RM 32,000", "+5%")
st.metric("Visits", 5400, "-2%")

st.bar_chart({
    "Jan": 100,
    "Feb": 200,
    "Mar": 150,
    "Apr": 300
})
