```python
import streamlit as st
from streamlit_chat import message
from google_auth_oauthlib.flow import InstalledAppFlow
from bs4 import BeautifulSoup
import requests
import re

# Define the BARD API's endpoint and parameters
bard_endpoint = "https://generativelanguage.googleapis.com/v1beta2/models/text-bison-001:generateText?key={{API_KEY}}"
bard_params = {
    "prompt": {
        "text": "Find the lowest price for [product name] in Guatemala.",
        "model_parameters": {
            "temperature": 0.7
        }
    }
}

# Set up Streamlit components
st.title("Lowest Price Finder")
product_name = st.text_input("Product Name:")
st.write("Searching...")

# Use BARD API to find the product's lowest price in Guatemala
response = requests.post(bard_endpoint, json=bard_params)
result = response.json()
price_response = result["candidates"][0]["output"]

# Extract the price from the BARD response
price = re.findall(r"Q(\d+)", price_response)[0]

# Use BeautifulSoup to scrape the product's price from a popular Guatemalan e-commerce site
url = "https://www.mercadolibre.com.gt/ofertas"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36"}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Find the product's price on the website
product_price = soup.find("span", class_="price-tag-amount").text.strip()

# Compare the BARD and website prices and display the lowest one
if int(price) < int(product_price):
    message("Lowest price found: Q{}".format(price))
else:
    message("Lowest price found on Mercado Libre: {}".format(product_price))
```
