import streamlit as st
col1, col2, col3 = st.columns([1, 3, 1])


with col2:
    st.title("Search Results:")

with col3:
    if st.button("Home"):
        print("Redirecting to home page")
        st.switch_page("UserInterface.py")