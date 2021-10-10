import streamlit as st
import pandas as pd
import numpy as np
import string
import streamlit_analytics

df = pd.read_csv('ipaivocab.csv')
df=df.dropna()
st.title("Yuman Dictionary")
st.subheader("URL: ipai.wiki")
st.write("Free online dictionary for Yuman languages, mostly Mesa Grande Ipai. Compiled from textbooks, dictionaries, etc. using digital humanities methods and Python.")
st.write("1,393 words/phrases indexed. Python tutorial I wrote on using Optical Character Recognition to extract Ipai words from photos of paper dictionaries: https://link.andrewgao.dev/ocr")
st.write("Note: limited entries for Mojave, Cocopa, Yavapai, and Jamul Tiipay.")
streamlit_analytics.start_tracking()

st.write("Demo: Keep the default settings and try searching 'fish'. Hit Enter key to search. You may need to scroll down the page.")
initlang = st.radio("Which language would you like to search from?",['English','Mesa Grande Ipai','Mojave','Cocopa','Yavapai','Jamul Tiipay'])
targlang = st.radio("Which language would you like to search for?",['Mesa Grande Ipai','Mojave','Cocopa','Yavapai','Jamul Tiipay','English'])

query=st.text_input("Enter word")
if len(query) != 0:
    st.write("Missing word? Submit an entry here: https://forms.gle/ZxQpzD1eMXsC7n2Z6")
    st.table(df[df[str(initlang)].str.contains(query)][[str(initlang),str(targlang)]])
st.write("Vocab sourced from The Global Lexicostatistical Database, native-languages.org, A Grammar of Diegueno: the Mesa Grande Dialect, Dictionary of Mesa Grande Diegueno, and learniipayaa.weebly.com.")
st.write("Pronunciation Guide (all credit to learniipayaa.weebly.com): https://link.andrewgao.dev/speakipai")

streamlit_analytics.stop_tracking()
