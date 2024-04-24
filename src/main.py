import streamlit as st
from utils.pages_switch import switch_page
from database import pgconfig



st.set_page_config(
     page_title="Smart Eye",
     initial_sidebar_state="expanded",
     layout="centered"

 )
def main():

    st.image('theme/logo.png')

    col1, col2, col3, col4 = st.columns([1,1,1,1])
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