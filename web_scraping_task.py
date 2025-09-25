import streamlit as st
import requests
from bs4 import BeautifulSoup

# url = "https://webscraper.io/test-sites/tables"
url = st.text_input("Enter URL here")
st.title("Web Scraping Task by Jignesh Mistry")
task = []
if url:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    
    for t in soup.find_all('title'):
        task.append(t.get_text(strip=True))

    
else:
    st.write("Please enter URL in the text input box")

if len(task) != 0:
        st.markdown(
        f"Title of the above website : <span style='font-weight:bold; color:blue;'>{task[0]}</span>",
        unsafe_allow_html=True
    )