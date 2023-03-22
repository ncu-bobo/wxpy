import requests


# 填入你申请的天气 API 的 key
api_key = "fcc4f3d9e7cf1d5b39ca4626ff604359"

# 填入你想查询的城市名
city = "360100"
extensions = 'all'

# 构造 API 请求 URL
url = f"https://restapi.amap.com/v3/weather/weatherInfo?city={city}&key={api_key}&extensions={extensions}"

def getWeatherInfo():
    # 发送 GET 请求并解析返回的 JSON 数据
    response = requests.get(url)
    data = response.json()

    # 获取当天天气信息
    today = data['forecasts'][0]['casts'][0]['date']
    city = data['forecasts'][0]['city']
    weather = data['forecasts'][0]['casts'][0]['dayweather']
    temp = data['forecasts'][0]['casts'][0]['daytemp']
    conditions = []
    conditions.append(today)
    conditions.append(city)
    conditions.append(weather)
    conditions.append(temp)

    return conditions