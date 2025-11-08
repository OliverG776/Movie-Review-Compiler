#Imports
import streamlit as st
from DataInitialization import initializeData
import os
import csv
import re

#Initializing streamlit variables
col1, col2, col3 = st.columns([1, 3, 1])
script_directory = os.path.dirname(__file__)
file_directory = os.path.join(script_directory,"movies.csv")

# Initialize Data into movieMap (contains all movies with their information)
movieMap = initializeData()
genreCategories = st.session_state['genreCategories']
# print(genreCategories)
print(genreCategories["Action"])

# check for genreSearchCheck 
# if true search_key will be genre type
# else search_key will be title
genreSearchCheck = st.session_state['searchGenre']
print(str(genreSearchCheck))

if 'search_key' not in st.session_state:
    st.session_state['search_key'] = ""
    movieTitle = "No search key found"

searchedMovie = st.session_state['search_key']

if 'releaseYear' not in st.session_state:
    st.session_state['releaseYear'] = "N/A"


with col2:
    st.title("Search Results for " + searchedMovie + ":")

# tuple that holds (title, genres, avg rating)
movieItems = movieMap.__getitem__(searchedMovie)

st.session_state['movieItems'] = movieItems
if genreSearchCheck == True:
    print()
else: 
    if movieItems != False:
        movieTitle, genres, avgRating, movieYear = movieItems
        if movieItems != -1:
            st.session_state['releaseYear'] = str(movieYear)
            # Creates the movie button for linking to the movie card
            buttonText = f"{movieTitle} - {movieYear}"
            if st.button(buttonText):
                print("Clicked a movie, redirect to card")

                st.switch_page("pages/MovieCard.py")
    else:
        st.write("No search results found")


    #ISSUE: Film year included as well, we can probably fix it just by identifying when we hit the first (



with col3:
    if st.button("Home"):
        print("Redirecting to home page")
        st.switch_page("UserInterface.py")
