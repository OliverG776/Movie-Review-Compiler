import streamlit as st
import os
import csv

# This page will grab the properties of the selected movie using the movie
# title as the key and displays the title(year), genres, rating

# if no key then empty search key
if 'search_key' not in st.session_state:
    st.session_state['search_key'] = ""
    movieTitle = "No Movie Card Here"

if 'movieItems' not in st.session_state:
    st.session_state['movieItems'] = ""
    print("no movie info")

movieTitle = st.session_state['search_key']



