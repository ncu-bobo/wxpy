import openpyxl
import requests


# 从xlsx文件中查询城市的code
def getCityCode(city):
    # 打开 Excel 文件
    wb = openpyxl.load_workbook('resource/AMap_adcode_citycode_20210406.xlsx')

    # 选择要操作的工作表（这里选择第一个工作表）
    ws = wb.active

    # 遍历每一行
    for row in ws.iter_rows():
        if row[0].value == city:
            return row[1].value

# 获取天气信息
def getWeatherInfo():
    # 填入你申请的天气 API 的 key
    api_key = "fcc4f3d9e7cf1d5b39ca4626ff604359"

    # 填入你想查询的城市名
    city = getCityCode("景德镇市")
    extensions = 'all'

    # 构造 API 请求 URL
    url = f"https://restapi.amap.com/v3/weather/weatherInfo?city={city}&key={api_key}&extensions={extensions}"

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
