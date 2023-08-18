import json
import requests
from bs4 import BeautifulSoup

# URL of the webpage you want to scrape
url = 'https://www.stjude.org/treatment/patient-resources/caregiver-resources/medicines/a-z-list-of-medicines.html'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all elements with a specific class that contains the article titles

# Finding by id
s = soup.find('div', class_= 'par-1 parsys')
# Getting the leftbar
leftbar = s.find('ul', class_='list-filter links')
 
# All the li under the above ul
content = leftbar.find_all('li')

medicine_list = []

# find a in li:
for x in content:
    anchor = x.find('a')
    data = anchor.text
    # print(anchor.text)
    cleaned_data = data.strip()
    medicine_list.append(cleaned_data)
 
# print(medicine_list)

json_medicine_list = json.dumps(medicine_list)

print(json_medicine_list)

with open("data.json", "w") as json_medicine_list_json_file:
    json.dump(json_medicine_list, json_medicine_list_json_file)
