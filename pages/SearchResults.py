#Imports
import streamlit as st
from DataInitialization import initializeData
import os
import csv
import re

#Initializing streamlit variables
st.set_page_config(layout="wide")
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
# print(str(genreSearchCheck))

if 'search_key' not in st.session_state:
    st.session_state['search_key'] = ""
    movieTitle = "No search key found"

searchedMovie = st.session_state['search_key']

if 'releaseYear' not in st.session_state:
    st.session_state['releaseYear'] = "N/A"


with col2:
    if genreSearchCheck == True:
        if searchedMovie == "Children":
            st.title("Search Results for Children's Movies:")
        elif searchedMovie == "Miscellaneous":
            st.title("Search Results for " + searchedMovie + " Movies:")
            searchedMovie = "(no genres listed)"
        else:
            st.title("Search Results for " + searchedMovie + " Movies:")
    else:
        st.title("Search Results for " + searchedMovie + ":")

    
with col3:
    if st.button("Home"):
        print("Redirecting to home page")
        st.switch_page("UserInterface.py")


if genreSearchCheck == True:
    cols = st.columns(6)
    print("Search results based on genre")
    # Using genre as key get list of all movies with user specified genre tag
    genreResult = genreCategories[searchedMovie]
    # output each movie as a button
    for i, movie in enumerate(genreResult):
        movieItems = movieMap.__getitem__(movie)
        if movieItems != False:
            movieTitle, genres, avgRating, movieYear = movieItems
            st.session_state['releaseYear'] = str(movieYear)
            # Creates the movie button for linking to the movie card
            buttonText = f"{movieTitle} - {movieYear}"
            
            col = cols[(i%4)+1]
            with col:
                if st.button(buttonText, key = f"{i}"):
                    print("Clicked a movie, redirect to card")
                    st.session_state['movieItems'] = movieItems
                    st.switch_page("pages/MovieCard.py")
    
else: 
    with col2:
        print("Search results based on title")

        partialTitles = []
        searchedMovie = searchedMovie.rstrip()

        for key in movieMap.mapContainer:
            if key is not None:
                title, genres, rating, year = key

                if searchedMovie.lower() in title.lower():
                    movieItems = movieMap.__getitem__(title)
                    partialTitles.append(movieItems)

        # tuple that holds (title, genres, avg rating)
        #movieItems = movieMap.__getitem__(searchedMovie.rstrip())
        #st.session_state['movieItems'] = movieItems
        cols = st.columns(6)
        i = 1
        if partialTitles != []:
            for title in partialTitles:
                movieItems = movieMap.__getitem__(title[0])
                movieTitle, genres, avgRating, movieYear = movieItems

                st.session_state['releaseYear'] = str(movieYear)

                # Creates the movie button for linking to the movie card
                buttonText = f"{movieTitle} - {movieYear}"
                key = i
                if st.button(buttonText, key = key):
                    st.session_state['movieItems'] = movieItems
                    print("Clicked a movie, redirect to card")

                    st.switch_page("pages/MovieCard.py")
                i+=1
        else:
            st.write("No search results found")


    #ISSUE: Film year included as well, we can probably fix it just by identifying when we hit the first (

