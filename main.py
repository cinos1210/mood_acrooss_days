import streamlit as st
import plotly.express as px
import nltk


st.title("Mood Across Days")
st.header('Positivity')
figure_po = px.line()
st.plotly_chart(figure_po)

st.header('Negativity')
figure_ne = px.line()
st.plotly_chart(figure_ne)

