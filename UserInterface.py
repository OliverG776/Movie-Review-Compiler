#Imports
import streamlit as st

#Run Command:
#streamlit run UserInterface.py

#Variables:

#Defines columns, essentially partitions the page so we can set assets to certain parts of the page
col1, col2, col3 = st.columns([1, 3, 1])
searchGenre = False
#Sets user's default search to ""
if 'search_key' not in st.session_state:
    st.session_state['search_key'] = ""

#UI Setup
with col2:
    st.title("Search for Reviews:")

search = st.text_input("Search here!")
if search:
    #Changes 'search_key' to str(search), then performs search
    st.session_state['search_key'] = str(search)
    #st.write(search)
    st.switch_page("pages/Search.py")

#Allows the user to choose what category they want to sort by
search_toggle = st.radio(
    "Search by:", ("Film Title", "Genre"), horizontal=True
)

#Testing
#st.write("search is", st.session_state['search_key'])

#Switches what user is searching by
if search_toggle == "Film Title":
    searchGenre = False
else:
    searchGenre = True

#Top films page
with col3:
    if st.button("Top Films"):
        print("Redirecting to top films link")
        st.switch_page("pages/TopFilms.py")