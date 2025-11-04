#Imports
import streamlit as st

#Run Command:
#streamlit run UserInterface.py

#Variables:

#Defines columns, essentially partitions the page so we can set assets to certain parts of the page
showSidebarNavigation = False
col1, col2, col3 = st.columns([1, 3, 1])
#Sets user's default search to ""
if 'search_key' not in st.session_state:
    st.session_state['search_key'] = ""

if 'searchGenre' not in st.session_state:
    st.session_state['searchGenre'] = False

# Allows the user to choose what category they want to sort by
search_toggle = st.radio(
    "Search by:", ("Film Title", "Genre"), horizontal=True
)

# #Switches what user is searching by
if search_toggle == "Genre":
    st.session_state['searchGenre'] = True
else:
    st.session_state['searchGenre'] = False

#UI Setup
with col2:
    st.title("Search for Reviews:")

if st.session_state['searchGenre'] == False:
    search = st.text_input("Search here!")
    if search:
        print("Test 2")
        #Changes 'search_key' to str(search), then performs search
        st.session_state['search_key'] = str(search)
        #st.write(search)
        st.switch_page("pages/SearchResults.py")
else:
    search = st.selectbox(
        "Which genre?",
        ("", "Action", "Adventure", "Animation", "Children's", "Comedy", "Crime", "Documentary", "Drama", "Fantasy", "Film-Noir", "Horror", "Musical", "Mystery",
         "Romance", "Sci-Fi", "Thriller", "War", "Western", "No genre")
    )
    if search != "":
        st.session_state['search_key'] = str(search)
        st.switch_page("pages/SearchResults.py")



#Top films page
with col3:
    if st.button("Top Films"):
        print("Redirecting to top films link")
        st.switch_page("pages/TopFilms.py")