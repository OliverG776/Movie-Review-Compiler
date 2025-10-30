import streamlit as st
import UserInterface
import os
import csv

script_directory = os.path.dirname(__file__)
file_directory = os.path.join(script_directory, "movies.csv")
col1, col2, col3 = st.columns([1, 3, 1])

with col2:
    st.title("Top Films:")


with col3:
    if st.button("Home"):
        print("Redirecting to home page")
        st.switch_page("UserInterface.py")

with open(file_directory, newline="", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    i = 1
    for row in reader:
        st.write(str(i) + ". " + row[1])
        i+=1
