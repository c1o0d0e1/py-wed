#######################匯入模組#######################
import requests  # 載入 requests 套件 (用來發送請求) 內鍵 json 模組 (用來處理 json 格式資料)
import os
import sys

#######################定義常數########################
API_KEY = "892da2f13edf3c7f382637760e72d224"  # 你的 API 金鑰
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"  # 天氣 API 的基本 URL (? 後面會接參數)
UNITS = "metric"  # 使用公制單位 (攝氏度)
LANG = "zh_tw"  # 使用中文語言(繁體中文)

LANG = "zh_tw"  # 使用中文語言(繁體中文)
ICON_BASE_URL = (
    "https://openweathermap.org/img/wn/"  # 天氣圖示的基本 URL (後面會接圖示代碼和尺寸)
)
#######################建立視窗########################

#######################運行應用程式########################
os.chdir(
    sys.path[0]
)  # 將當前工作目錄更改為腳本所在的目錄，確保能夠正確地找到相關的文件和資源。
city_name = input("請輸入城市名稱: ")  # 從使用者輸入城市名稱

# 建立完整的 API 請求 URL
send_url = f"{BASE_URL}appid={API_KEY}&q={city_name}&units={UNITS}&lang={LANG}"

print(f"發送請求到: {send_url}")  # 印出發送請求的 URL (方便除錯)
response = requests.get(send_url)  # 發送 GET 請求到 API 並獲取回應
info = response.json()  # 將回應的 JSON 資料轉換為 Python 字典

# 處理和顯是天氣資訊
if not (
    info.get("cod") == 404
):  # 如果 API 回應的狀態碼不是 404 (表示城市找到)，則繼續處理資料
    current_temperature = info["main"]["temp"]  # 獲取當前溫度
    weather_description = info["weather"][0]["description"]  # 獲取天氣描述
    icon_code = info["weather"][0]["icon"]  # 獲取天氣圖示代碼
    print(f"城市: {city_name}")  # 印出城市名稱
    print(f"溫度: {current_temperature}°C")  # 印出當前溫度
    print(f"天氣描述: {weather_description}")  # 印出天氣描述
    print(f"描述: {weather_description}")  # 印出天氣描述

    # 根據圖片代碼組合圖標下載網址
    icon_url = f"{ICON_BASE_URL}{icon_code}@2x.png"

    # 下載圖標圖片
    icon_response = requests.get(icon_url)  # 發送 GET 請求下載圖標圖片
    print(f"下載圖標: {icon_url}")  # 印出下載圖標的 URL (方便除錯)

    # 若下載成功，就將圖標存於 png 檔案中
    if (
        icon_response.status_code == 200
    ):  # 如果圖標下載成功 (狀態碼 200)，則將圖標保存為 PNG 文件
        with open(f"{icon_code}.png", "wb") as icon_file:  # 以二進制寫入模式打開文件
            icon_file.write(icon_response.content)  # 將下載的圖標內容寫入文件
        print(f"圖標已保存為: {icon_code}.png(weather.png)")  # 印出圖標已保存的訊息
    else:
        # 如果圖標下載失敗，印出錯誤訊息
        print(f"無法下載圖標，HTTP 狀態碼: {icon_response.status_code}")
else:
    print(
        "城市未找到，請檢查輸入的城市名稱是否正確。"
    )  # 如果 API 回應的狀態碼是 404，印出錯誤訊息
