#Imports
import streamlit as st
from DataInitialization import initializeData
import os
import csv
import re

#Initializing streamlit variables
col1, col2, col3 = st.columns([1, 5, 1])
script_directory = os.path.dirname(__file__)
file_directory = os.path.join(script_directory,"movies.csv")

movieMap = initializeData()

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

if movieItems != False and st.session_state['searchGenre'] == False:
    movieTitle, genres, avgRating, movieYear = movieItems
    if movieItems != -1:
        # Creates the movie button for linking to the movie card
        buttonText = f"{movieTitle} - {movieYear}"
        if st.button(buttonText):
            print("Clicked a movie, redirect to card")

            st.switch_page("pages/MovieCard.py")


    with open(file_directory, newline="", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        i = 1
        title = ""
        for row in reader:
            # temp = row[1].split("(")
            # if temp[1][0].isnumeric():
            title = row[1]
            #title = row[1].split("(")
            #title[0] = title[0][:-1]
            match = re.match(r"(.*)\s\((\d{4})\)$",title)
            if match:
                movie_title, movie_year = match.groups()
                #print(movie_title + " - " + str(movie_year))
            else:
                movie_title = title
                movie_year = "Year not found"
                print("Movie Title not found")
            # else:
            #     title = row[1]
            #     lastParenthesis = title.rfind("(")
            #     title = title[:lastParenthesis]

            if movie_title.lower() == st.session_state['search_key'].lower():
                st.session_state['releaseYear'] = movie_year
            #     st.write("Release Year: " + movie_year)
            #     st.write("Genres: " + row[2])
                #Need to check map here to pull out ratings/potentially switch genres to come from map
else:
    st.write("No search results found")

    #ISSUE: Film year included as well, we can probably fix it just by identifying when we hit the first (

with col3:
    if st.button("Home"):
        print("Redirecting to home page")
        st.switch_page("UserInterface.py")
