import streamlit as st
import os
import csv

col1, col2, col3 = st.columns([1, 3, 1])
script_directory = os.path.dirname(__file__)
file_directory = os.path.join(script_directory, "movies.csv")


with col2:
    st.title("Search Results for " + st.session_state['search_key'] + ":")

with open(file_directory, newline="", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    i = 1
    for row in reader:
        if row[1] == st.session_state['search_key']:
            st.write(row[1])

#ISSUE: Need film year included as well, we can probably fix it just by identifying when we hit the first (

with col3:
    if st.button("Home"):
        print("Redirecting to home page")
        st.switch_page("UserInterface.py")