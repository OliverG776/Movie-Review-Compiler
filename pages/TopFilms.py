import streamlit as st
import os
import csv
from PriorityQueue import PriorityQueue
from DataInitialization import initializeData
import re

script_directory = os.path.dirname(__file__)
file_directory = os.path.join(script_directory, "movies.csv")

movieMap = initializeData()
topFilms = PriorityQueue()

col1, col2, col3 = st.columns([1, 3, 1])

with col2:
    st.title("Top Films:")

with col3:
    if st.button("Home"):
        print("Redirecting to home page")
        st.switch_page("UserInterface.py")

# with open(file_directory, newline="", encoding="utf-8") as csvfile:
#     reader = csv.reader(csvfile)
#     next(reader)
#     i = 1
#     for row in reader:
#         st.write(str(i) + ". " + row[1])
#         i+=1
i = 1
for key in movieMap.mapContainer:
    if key is not None:
        title, genres, rating, year = key
        topFilms.insert(title, rating)

topThousand = topFilms.getTopThousand()

for film in topThousand:
    st.write(str(i) + ".  " + str(film[0]) + " - " + str(round(film[1], 2)))
    i += 1