import streamlit
import pandas
import requests

stramlit.title('Pickleball Tournament Bracket Maker')

streamlit.header('Enter teams here')
playing_pars = streamlit.text_input('Enter player pairs')
