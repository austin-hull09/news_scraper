from bs4 import BeautifulSoup
import requests

# Open link and get HTML to text format
link = "https://news.google.com/search?q=montana%20business%20when%3A1d&hl=en-US&gl=US&ceid=US%3Aen"
f = requests.get(link)
page = f.text

# Create bs4 object with site text
soup=BeautifulSoup(page, features="html.parser")

# Prints all headlines from parsed page
a = (soup.find_all("h3"))
for item in a:
    print(item.string)