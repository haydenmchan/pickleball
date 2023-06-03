# streamlit_app.py

import pandas as pd
import streamlit as st

# Read in data from the Google Sheet.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def load_data(sheets_url):
    csv_url = sheets_url.replace("/edit#gid=", "/export?format=csv&gid=")
    return pd.read_csv(csv_url)

df = load_data(st.secrets["public_gsheets_url"])

st.title('Pickleball Tournament Bracket Maker')

playdate = st.text_input('Enter the date of the game (X/X)')

st.header("Let's enter the teams playing tonight")
st.text_input('Enter teams here. Press enter after each pair')

st.text("Here are the teams for tonights match")
