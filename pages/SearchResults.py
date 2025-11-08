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

#Initializing session state variables
if 'search_key' not in st.session_state:
    st.session_state['search_key'] = ""
    movieTitle = "No search key found"

searchedMovie = st.session_state['search_key']

if 'releaseYear' not in st.session_state:
    st.session_state['releaseYear'] = "N/A"

#Initializing title for search results page
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


#Home button implementation
with col3:
    if st.button("Home"):
        print("Redirecting to home page")
        st.switch_page("UserInterface.py")

#Cases for searching by genre and searching by title
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

        #Initialize a list with all titles that contain the user's search
        partialTitles = []
        #Remove any blank space left at the end of the user's search
        searchedMovie = searchedMovie.rstrip()

        #Iteration through every title in movieMap
        for key in movieMap.mapContainer:
            if key is not None:
                title, genres, rating, year = key

                #If the user's search is contained in a known title, title is added to list of possible search results
                if searchedMovie.lower() in title.lower():
                    movieItems = movieMap.__getitem__(title)
                    partialTitles.append(movieItems)


        cols = st.columns(6)
        #Initialized to give every button a unique key, prevents streamlit errors
        i = 1
        #Check to make sure there are possible search results
        if partialTitles != []:
            for title in partialTitles:
                #Pulls information for every title contained in partialTitles and gives it a unique button
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
                #Updates key for next title
                i+=1
        else:
            #Case for no movies found
            st.write("No search results found")



