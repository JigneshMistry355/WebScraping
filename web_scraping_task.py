import streamlit as st
import requests
from bs4 import BeautifulSoup

st.title("Web Scraping Task by Jignesh Mistry")

# url = "https://webscraper.io/test-sites/tables" # test site

url = st.text_input("Enter URL here")

task = []
if url:
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            for t in soup.find_all('title'):
                task.append(t.get_text(strip=True))
        else:
            st.write("Something went wrong, Check your url or try again")
            st.markdown(
                f"Some Error occured : <span style='font-weight:bold; color:orange;'>Something went wrong, Check your url or try again</span>",
                unsafe_allow_html=True
            )
    except requests.exceptions.RequestException as e:
        st.markdown(
            f"Some Error occured : <span style='font-weight:bold; color:red;'>Unable to connect to the url. Check URL or try again</span>",
            unsafe_allow_html=True
        )
    
else:
    st.write("Please enter URL in the text input box")

if len(task) != 0:
    st.markdown(
        f"Title of the above website : <span style='font-weight:bold; color:blue;'>{task[0]}</span>",
        unsafe_allow_html=True
    )