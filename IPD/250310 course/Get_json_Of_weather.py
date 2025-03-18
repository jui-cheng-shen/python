import requests
import json
import pandas as pd

# 發送 API 請求
url = 'https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-D0047-079?Authorization=CWA-046FA46C-A9B8-403A-BD23-B3615A511C7E&format=JSON'
response = requests.get(url)

# 檢查 API 回應狀態
if response.status_code != 200:
    print(f"錯誤：API 請求失敗，狀態碼 {response.status_code}")
    print(response.text)
    exit()

# 解析 JSON 數據
data = json.loads(response.text)
location_data = data["records"]["location"]

# 存儲結果的列表
weather_list = []

# 目標天氣元素
target_elements = ["Wx", "PoP", "MinT", "MaxT", "CI"]

# 解析每個地點的天氣資訊
for location in location_data:
    location_name = location["locationName"]
    weather_dict = {}

    # 解析天氣元素
    for element in location["weatherElement"]:
        if element["elementName"] not in target_elements:
            continue  # 只處理目標元素
        element_name = element["elementName"]

        for time_data in element["time"]:
            start_time = time_data["startTime"]
            end_time = time_data["endTime"]
            parameter_value = time_data["parameter"]["parameterName"]

            # 使用 startTime 作為鍵，避免索引誤差
            if start_time not in weather_dict:
                weather_dict[start_time] = {
                    "locationName": location_name,
                    "startTime": start_time,
                    "endTime": end_time
                }

            # 添加天氣元素數據
            weather_dict[start_time][element_name] = parameter_value

    # 將整理好的數據添加到列表中
    weather_list.extend(weather_dict.values())

# 轉換為 DataFrame
df = pd.DataFrame(weather_list)

# 重新命名欄位
df.rename(columns={
    "Wx": "天氣",
    "PoP": "降雨機率(%)",
    "MinT": "最低溫(°C)",
    "MaxT": "最高溫(°C)",
    "CI": "舒適度"
}, inplace=True)

# 轉換數值類型
df["降雨機率(%)"] = pd.to_numeric(df["降雨機率(%)"], errors="coerce")
df["最低溫(°C)"] = pd.to_numeric(df["最低溫(°C)"], errors="coerce")
df["最高溫(°C)"] = pd.to_numeric(df["最高溫(°C)"], errors="coerce")

# 指定欄位順序
df = df[["locationName", "startTime", "endTime", "天氣", "降雨機率(%)", "最低溫(°C)", "最高溫(°C)", "舒適度"]]

# 顯示 DataFrame
print("原始 JSON 回應：")
print(response.text)
print("\n整理後的 DataFrame：")
print(df)

# 可選：將 DataFrame 儲存為 CSV
# df.to_csv("weather_data.csv", index=False, encoding="utf-8-sig")