import requests

url = 'https://open.tophub.today/daily'

response = requests.get(url)
data = response.json()
print(data)