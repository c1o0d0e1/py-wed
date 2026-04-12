#######################匯入模組#######################
import requests  # 載入 requests 套件 (用來發送請求) 內鍵 json 模組 (用來處理 json 格式資料)

#######################定義常數########################
API_KEY = "892da2f13edf3c7f382637760e72d224"  # 你的 API 金鑰
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"  # 天氣 API 的基本 URL
UNITS = "metric"  # 使用公制單位 (攝氏度)
LANG = "zh_tw"  # 使用中文語言(繁體中文)

#######################建立視窗########################

#######################運行應用程式########################
city_name = input("請輸入城市名稱: ")  # 從使用者輸入城市名稱

# 建立完整的 API 請求 URL
send_url = f"{BASE_URL}&appid={API_KEY}q={city_name}&units={UNITS}&lang={LANG}"

print(f"發送請求到: {send_url}")  # 印出發送請求的 URL (方便除錯)
response = requests.get(send_url)  # 發送 GET 請求到 API 並獲取回應
Info = response.json()  # 將回應的 JSON 資料轉換為 Python 字典
