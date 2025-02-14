import streamlit as st
import requests

api = "3GdGAdzfRcv1LkLoWs9tWEULNjakCvWxr5U7s5N1"
url = "https://api.nasa.gov/planetary/apod?" \
    f"api_key={api}"

response_text = requests.get(url)
text = response_text.json()

image_url = text['hdurl']
response_image = requests.get(image_url)
image = response_image.content

with open("image.jpg", "wb") as file:
    file.write(image)

st.title(text['title'])
st.image("image.jpg")
st.write(text["explanation"])

