from flask import Flask
import requests
import json

app = Flask(__name__)


API_KEY = "CWA-98AC7687-ABC4-469F-9655-75E86294278A"  # 替換成你的授權碼
CITY = "臺南市"
BASE_URL = f"https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization={API_KEY}&locationName={CITY}"

@app.route("/")
def home():
    try:
        response = requests.get(BASE_URL)

        if response.status_code != 200:
            return f"錯誤：無法獲取天氣資料，狀態碼：{response.status_code}"

        data = response.json()
        location_data = data.get("records", {}).get("location", [])

        if not location_data:
            return "錯誤：未找到該城市的天氣資料"

        ret = ""  # 儲存輸出結果
        for location in location_data:
            for element in location.get("weatherElement", []):
                if element["elementName"] == "PoP":
                    for time_slot in element.get("time", []):
                        start_time = time_slot["startTime"]
                        end_time = time_slot["endTime"]
                        pop_value = time_slot["parameter"]["parameterName"]
                        ret += f"{start_time} 至 {end_time} 的降雨機率為：{pop_value}%<br>\n"

        return ret

    except Exception as e:
        return f"發生錯誤：{str(e)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)




'''from flask import Flask
import requests

app = Flask(__name__)

# OpenWeatherMap API 設定
API_KEY = "CWA-046FA46C-A9B8-403A-BD23-B3615A511C7E"  # 替換為你的 API 鍵
CITY = "Taipei"  # 你想查詢的城市，例如台北
BASE_URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

@app.route("/")
def get_weather():
    try:
        # 發送請求到 OpenWeatherMap API
        response = requests.get(BASE_URL)
        data = response.json()

        # 檢查是否有錯誤
        if data["cod"] != "200":
            return f"錯誤：無法獲取 {CITY} 的天氣資料，錯誤訊息：{data['message']}"

        # 提取天氣預報資料（這裡取第一個時間點）
        forecast = data["list"][0]  # 第一個預報時間點
        timestamp = forecast["dt_txt"]  # 時間
        temp = forecast["main"]["temp"]  # 溫度（攝氏）
        weather_desc = forecast["weather"][0]["description"]  # 天氣描述

        # 檢查是否有降雨機率（pop = probability of precipitation）
        rain_prob = forecast.get("pop", 0) * 100  # 降雨機率（轉為百分比）

        # 格式化輸出
        result = f"{timestamp} 的天氣預報：<br>"
        result += f"溫度：{temp}°C<br>"
        result += f"天氣狀況：{weather_desc}<br>"
        result += f"降雨機率：{rain_prob}%"

        return result

    except Exception as e:
        return f"發生錯誤：{str(e)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)'''
