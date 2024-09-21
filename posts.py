import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts')
print(response.status_code)
print(response.text)

# response = requests.get('https://jsonplaceholder.typicode.com')
# soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify()) 