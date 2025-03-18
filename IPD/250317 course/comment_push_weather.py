from flask import Flask  # 從 Flask 套件匯入 Flask 類別，用於建立 Flask 應用程式
import requests  # 匯入 requests 套件，用於發送 HTTP 請求
from urllib.parse import quote  # 從 urllib.parse 匯入 quote 函數，用於 URL 編碼

app = Flask(__name__)  # 建立一個 Flask 應用程式實例

# 中央氣象局 API 設定
API_KEY = "CWA-98AC7687-ABC4-469F-9655-75E86294278A"  # 請替換為從 CWA 申請的授權碼
CITY = "臺南市"  # 查詢的城市名稱
# 組合 API 請求的基本 URL，包含授權碼和城市名稱
BASE_URL = f"https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization={API_KEY}&locationName={quote(CITY)}"

@app.route("/")  # 定義根路徑的路由
def home():
    try:
        # 發送 HTTP 請求
        response = requests.get(BASE_URL)  # 向 API 發送 GET 請求
        response.raise_for_status()  # 如果狀態碼不是 200，拋出異常

        data = response.json()  # 將回應轉換為 JSON 格式
        location_data = data.get("records", {}).get("location", [])  # 獲取天氣資料中的 location 資料

        if not location_data:  # 如果沒有找到 location 資料
            return "錯誤：未找到該城市的天氣資料"  # 返回錯誤訊息

        ret = ""  # 儲存輸出結果
        for location in location_data:  # 遍歷每個 location
            location_name = location.get("locationName")  # 獲取 location 名稱
            for element in location.get("weatherElement", []):  # 遍歷每個 weatherElement
                if element["elementName"] == "PoP":  # 如果元素名稱是 "PoP"（降雨機率）
                    for time_slot in element.get("time", []):  # 遍歷每個時間段
                        start_time = time_slot["startTime"]  # 獲取開始時間
                        end_time = time_slot["endTime"]  # 獲取結束時間
                        # 確保正確獲取降雨機率（可能需要調整為 parameterValue）
                        pop_value = time_slot["parameter"]["parameterName"]  # 獲取降雨機率值
                        ret += f"{start_time} 至 {end_time} 的降雨機率為：{pop_value}%<br>\n"  # 將結果加入輸出字串

        if not ret:  # 如果沒有找到降雨機率資料
            return "錯誤：未找到降雨機率資料"  # 返回錯誤訊息
        return ret  # 返回結果

    except requests.exceptions.RequestException as e:  # 捕捉請求異常
        return f"API 請求錯誤：{str(e)}"  # 返回請求錯誤訊息
    except KeyError as e:  # 捕捉 KeyError 異常
        return f"資料解析錯誤：缺少預期的鍵 {str(e)}"  # 返回資料解析錯誤訊息
    except Exception as e:  # 捕捉其他異常
        return f"發生未知錯誤：{str(e)}"  # 返回未知錯誤訊息

if __name__ == "__main__":  # 如果這個模組是被直接執行
    print(f"啟動伺服器，查詢城市：{CITY}")  # 在控制台輸出啟動訊息
    app.run(host="0.0.0.0", port=5000, debug=True)  # 啟動 Flask 伺服器，監聽所有 IP 地址的 5000 埠，並啟用除錯模式