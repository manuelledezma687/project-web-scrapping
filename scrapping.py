import requests
from bs4 import BeautifulSoup

## Example 1
# response = requests.get('https://jsonplaceholder.typicode.com/posts') tambien con post
# print(response.status_code)
# print(response.text)

## Example 2
# response = requests.get('https://jsonplaceholder.typicode.com')
# soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify()) 

## Example 3
# response = requests.get('https://jsonplaceholder.typicode.com')
# soup = BeautifulSoup(response.text, 'html.parser')
# title = soup.find('h1').text
# print(title)


# Extraer todos los enlaces  Example 4
response = requests.get('https://jsonplaceholder.typicode.com')
soup = BeautifulSoup(response.text, 'html.parser')
links = soup.find_all('a')
for link in links:
    print(link.get('href'))
    
# Obtener títulos de artículos Example 5
headlines = soup.find_all('h2', class_='headline')
for headline in headlines:
    print(headline.text.strip())
