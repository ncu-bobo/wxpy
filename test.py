import requests

API_KEY = '5c474e6f27cfba8944344efe3fc76c72'
type = 'guoji'

url = f'http://v.juhe.cn/toutiao/index?type={type}&key={API_KEY}'

response = requests.get(url)
data = response.json()
news = []
for i in data['result']['data']:
    news.append(i['title']+i['url'])

print(news)