import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

# Send a GET request
response = requests.get(url)

# Parsing HTML content with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Finding all book containers
books = soup.find_all('article', class_='product_pod')

# Loop through and extract title and price
for book in books:
    title = book.h3.a['title']
    price = book.find('p', class_='price_color').text
    print(f"{title} - {price}")
