import streamlit as st
import pandas as pd
import numpy as np
import string
import streamlit_analytics

df = pd.read_csv('ipaivocab.csv')
df=df.dropna()
st.image("ipai.wiki.png",width=400)
st.title("Mesa Grande Ipai Dictionary")
st.write("Vocab sourced from The Global Lexicostatistical Database, native-languages.org, A Grammar of Diegueno: the Mesa Grande Dialect, Dictionary of Mesa Grande Diegueno, and learniipayaa.weebly.com.")
st.write("Currenly 1393 words and phrases indexed.")
st.write("Pronunciation Guide: https://link.andrewgao.dev/speakipai")
streamlit_analytics.start_tracking()

lang = st.radio("Which language would you like to search with?",['English','Ipai'])
if(lang=='English'):
    query1 = st.text_input('Search English word')
    if len(query1) != 0:
        st.table(df[df['english'].str.contains(query1)])
elif(lang=='Ipai'):
    query2 = st.text_input('Search Ipai word')
    if len(query2) != 0:
        st.table(df[df['ipai'].str.contains(query2)])
streamlit_analytics.stop_tracking()
