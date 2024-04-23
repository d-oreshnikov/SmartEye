import streamlit as st
from utils.pages_switch import switch_page
from database import pgconfig




def main():

    st.image('theme/logo.png')

    col1, col2, col3, col4 = st.columns(4)
    with col1: 
        if st.button("Upload photo"):
            switch_page('upload_photo')
    with col2: 
        if st.button("Stream camera"):
            switch_page('stream_camera')
    with col3: 
        if st.button("Stream video"):
            switch_page('stream_video')
    with col4: 
        if st.button("Delete photo"):
            switch_page('delete_photo')
    

if __name__ == '__main__':
    main()