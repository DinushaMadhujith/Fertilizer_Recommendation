import streamlit as st
from home import show_home  # Import the home module
from prediction import show_prediction  # Import the prediction module

# Set up session state to remember the page
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'Home'  # Default to "Home" on the first load

def main():
    st.sidebar.title("Navigation")
    menu = ["Home", "Prediction"]
    choice = st.sidebar.selectbox("Choose a page", menu)

    # Update session state based on the user's choice
    if choice != st.session_state.current_page:
        st.session_state.current_page = choice

    # Display the selected page
    if st.session_state.current_page == "Home":
        show_home()
    elif st.session_state.current_page == "Prediction":
        show_prediction()

if __name__ == "__main__":
    main()
