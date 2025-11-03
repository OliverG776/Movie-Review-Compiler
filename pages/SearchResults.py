#Imports
import streamlit as st
import os
import csv

#Initializing streamlit variables
col1, col2, col3 = st.columns([1, 3, 1])
script_directory = os.path.dirname(__file__)
file_directory = os.path.join(script_directory,"movies.csv")


with col2:
    st.title("Search Results for " + st.session_state['search_key'] + ":")

with open(file_directory, newline="", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    i = 1
    title = ""
    for row in reader:
        # temp = row[1].split("(")
        # if temp[1][0].isnumeric():
        title = row[1].split("(")
        title[0] = title[0][:-1]
        # else:
        #     title = row[1]
        #     lastParenthesis = title.rfind("(")
        #     title = title[:lastParenthesis]

        if title[0].lower() == st.session_state['search_key'].lower():
            st.write(title[0])
            st.write("Genres: " + row[2])
            #Need to check map here to pull out ratings/potentially switch genres to come from map

#ISSUE: Film year included as well, we can probably fix it just by identifying when we hit the first (

with col3:
    if st.button("Home"):
        print("Redirecting to home page")
        st.switch_page("UserInterface.py")
