#Imports
import streamlit as st
import os
import csv
from PriorityQueue import PriorityQueue
from DataInitialization import initializeData

#Initializing script to read
script_directory = os.path.dirname(__file__)
file_directory = os.path.join(script_directory, "movies.csv")

#Initializing movie map + list of top films
movieMap = initializeData()
topFilms = PriorityQueue()

#Initializing streamlit variables
st.set_page_config(layout = "centered")
col1, col2, col3 = st.columns([1, 3, 1])

#Title of page printed to screen
with col2:
    st.title("Top Films:")

#Home button initialized
with col3:
    if st.button("Home"):
        print("Redirecting to home page")
        st.switch_page("UserInterface.py")

#i represents film ranking
i = 1

#For every valid film, add to topFilms
for key in movieMap.mapContainer:
    if key is not None:
        title, genres, rating, year = key
        topFilms.insert(title, rating)

#Grab top 1000 films based on ranking
topThousand = topFilms.getTopThousand()

#Print every film in topThousand to screen
for film in topThousand:
    st.write(str(i) + ".  " + str(film[0]) + " - " + str(round(film[1], 2)))
    i += 1
