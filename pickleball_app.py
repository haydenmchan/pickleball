import streamlit
import pandas
import requests
from google.oauth2 import service_account
from gsheetsdb import connect
# requirements.txt
gsheetsdb==0.1.13.1

streamlit.title('Pickleball Tournament Bracket Maker')

streamlit.header('Enter teams here')
playing_pairs = streamlit.text_input('Enter player pairs. Seperate teams with a ","')

streamlit.body('Here are the teams for tonights match')
streamlit.datadframe(playing_pairs)
