

def web_page(title,imgb,content):
    import streamlit as st

    st.title(title)

    st.image(imgb)

    st.write(content)

def get_nasa_content(api):
    import requests

    r = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={api}")

    return r.json()

