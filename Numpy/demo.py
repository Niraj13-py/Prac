import requests
from bs4 import BeautifulSoup
import pandas as pd

# Target URL
url = "https://books.toscrape.com/"
response = requests.get(url)

# Check for successful request
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    books = soup.find_all('article', class_='product_pod')

    # Prepare list of dictionaries
    data = []
    for book in books:
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text
        data.append({'Title': title, 'Price': price})

    # Convert to DataFrame
    df = pd.DataFrame(data)

    # Export to Excel
    df.to_excel('books.xlsx', index=False)
    print(" Data exported to books.xlsx")
else:
    print(" Failed to retrieve data")
