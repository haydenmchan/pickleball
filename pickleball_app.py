import streamlit
import pandas
import requests
import gspread

streamlit.title('Pickleball Tournament Bracket Maker')

streamlit.header('Enter teams here')
playing_pairs = streamlit.text_input('Enter player pairs. Seperate teams with a ","')

streamlit.body('Here are the teams for tonights match')
streamlit.datadframe(playing_pairs)
