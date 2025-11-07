import streamlit as st
import os
import csv

# This page will grab the properties of the selected movie using the movie
# title as the key and displays the title, genres, rating, release year

col1, col2, col3 = st.columns([1, 3, 1])

# if no key then empty search key
if 'search_key' not in st.session_state:
    st.session_state['search_key'] = ""
    movieTitle = "No Movie Card Here"

if 'movieItems' not in st.session_state:
    st.session_state['movieItems'] = ""
    print("no movie info")

if 'releaseYear' not in st.session_state:
    st.session_state['releaseYear'] = ""
    releaseYear = "No Release Year Here"

movieTitle = st.session_state['search_key']
movieTitle, genres, avgRating, movieYear = st.session_state['movieItems']
releaseYear = st.session_state['releaseYear']

with col2:
    st.title(str(movieTitle))

st.write("Genres: " + ", ".join(genres))
st.write("Average rating: " + str(round(avgRating,1)) + "/5")
st.write("Release year: " + str(releaseYear))

with col3:
    if st.button("Home"):
        print("Redirecting to home page")
        st.switch_page("UserInterface.py")

with col1:
    if st.button("Back"):
        print("Redirecting back to search results")
        st.switch_page("pages/SearchResults.py")
