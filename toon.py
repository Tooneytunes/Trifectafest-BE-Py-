def functie3():
    print("Hallo")

import requests, os, bs4, lxml
import re
from bs4 import BeautifulSoup

# Read from recipe URL List
with open('weburls.txt', 'r') as f:
    web_urls = f.readlines()

if os.path.exists("output.txt"):
    os.remove("output.txt")
else:
    print("File is not present in system, making file")

with open('output.txt', 'a', encoding='utf-8') as f:
    for idx, url in enumerate(web_urls):
        # Content
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        for items in soup.find_all('h3', class_='ev3page-title'):
            pattern = r'>\s*(.*?)\s*</a>'
            match = re.findall(pattern, str(soup))
            break

        print(match[0])

        # Append to the file
        # f.write(f"Scraped from: {url}\nName: \nCatagory: \nCosts ({len()}): \nAverage cost: €")
        # print(f"Stamp: has been added")
        
        # ev3page < Pagina-items
        # ev3page-title < Titel
        # ev3page-week < Weekdag
        # ev3page-venue < Plek
        # ev3page-day < Dag
        # ev3page-month < Maand
        # ev3page-year < Jaar
        # ev3page-hour < Uren