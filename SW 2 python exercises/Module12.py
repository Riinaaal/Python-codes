# Module 12 assignment 1
import requests

url = "https://api.chucknorris.io/jokes/random"

response = requests.get(url)

str = response.json()
print(str['value'])


