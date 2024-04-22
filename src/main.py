import streamlit as st
from utils.pages_switch import switch_page
from database import pgconfig




def main():
    home_title = "Neuroface"
    home_introduction = "Welcome to Neuroface!"


    st.title(home_title)

    st.write(home_introduction)

    col1, col2, col3 = st.columns(3)
    with col1: 
        if st.button("Upload photo"):
            switch_page('photo')
    with col2: 
        if st.button("Stream"):
            switch_page('stream')
    with col3: 
        if st.button("Delete photo"):
            switch_page('del_photo')
    

if __name__ == '__main__':
    main()