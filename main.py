import streamlit as st
import plotly.express as px
import Backend
import nltk

from Backend import dates_again

dates = Backend.get_date_data()



pos, neg = Backend.getPosNeg(dates)

parse_dates = dates_again()

st.title("Mood Across Days")
st.header('Positivity')
figure_po = px.line(x=parse_dates, y=pos, labels={'x': 'Date', 'y': 'Positivity'})
st.plotly_chart(figure_po)

st.header('Negativity')
figure_ne = px.line(x=parse_dates, y=neg, labels={'x': 'Date', 'y': 'Negativity'})
st.plotly_chart(figure_ne)

