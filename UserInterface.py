import streamlit as st
#Run Command:
#streamlit run C:\Users\olive_lxjq7tp\PycharmProjects\MovieReview\UserInterface.py
#streamlit run UserInterface.py

col1, col2, col3 = st.columns([1, 3, 1])
searchActor = False
if 'search_key' not in st.session_state:
    st.session_state['search_key'] = ""

with col2:
    st.title("Search for Reviews:")

search = st.text_input("Search here!")
if search:
    st.session_state['search_key'] = str(search)
    st.write(search)
    st.switch_page("pages/Search.py")

search_toggle = st.radio(
    "Search by:", ("Film Title", "Actor"), horizontal=True
)

st.write("search is", st.session_state['search_key'])

if search_toggle == "Film Title":
    searchActor = False
else:
    searchActor = True

with col3:
    if st.button("Top Films"):
        print("Redirecting to top films link")
        st.switch_page("pages/TopFilms.py")