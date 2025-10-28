import streamlit as st
#Run Command:
#streamlit run C:\Users\olive_lxjq7tp\PycharmProjects\MovieReview\UserInterface.py
#streamlit run UserInterface.py

col1, col2, col3 = st.columns([1, 3, 1])
searchActor = False

with col2:
    st.title("Search for Reviews:")


#st.write("Hello, Streamlit!")

search = st.text_input("Search here!")
if search:
    st.write(search)
    st.switch_page("pages/Search.py")

search_toggle = st.radio(
    "Search by:", ("Film Title", "Actor"), horizontal=True
)

if search_toggle == "Film Title":
    searchActor = False
else:
    searchActor = True

with col3:
    if st.button("Top Films"):
        print("Redirecting to top films link")
        st.switch_page("pages/TopFilms.py")

        #Test