#######################匯入模組#######################
from ttkbootstrap import *
import requests  # 用於發送 HTTP 請求
import os
import sys

from PIL import Image, ImageTk  # 載入 PIL 模組中的 Image 和 ImageTk 類別，用於處理圖像

#######################定義常數########################
API_KEY = "892da2f13edf3c7f382637760e72d224"  # 你的 API 金鑰
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"  # 天氣 API 的基本 URL (? 後面會接參數)
UNITS = "metric"  # 使用公制單位 (攝氏度)
LANG = "zh_tw"  # 使用中文語言(繁體中文)
ICON_BASE_URL = (
    "https://openweathermap.org/img/wn/"  # 天氣圖示的基本 URL (後面會接圖示代碼和尺寸)
)

# 全域變數：存儲當前溫度（攝氏度）
current_temp_celsius = 0.0  # 存儲當前溫度的攝氏度值

#######################設定工作目錄########################
# 將當前工作目錄更改為腳本所在的目錄，確保能夠正確地找到相關的文件和資源。
os.chdir(sys.path[0])


#######################定義函數########################
def show_result():
    global current_temp_celsius  # 使用全域變數
    entry_text = entry.get()  # 取得Entry物件中的文字

    if not entry_text.strip():
        print_label.config(text="請輸入城市名稱")
        return

    # 建立完整的 API 請求 URL
    send_url = f"{BASE_URL}appid={API_KEY}&q={entry_text}&units={UNITS}&lang={LANG}"

    try:
        response = requests.get(send_url)  # 發送 GET 請求到 API 並獲取回應
        info = response.json()  # 將回應的 JSON 資料轉換為 Python 字典

        # 處理和顯示天氣資訊
        if not (
            info.get("cod") == 404 or info.get("cod") == "404"
        ):  # 如果 API 回應的狀態碼不是 404 (表示城市找到)，則繼續處理資料
            current_temp_celsius = info["main"]["temp"]  # 獲取當前溫度（攝氏度）
            weather_description = info["weather"][0]["description"]  # 獲取天氣描述
            icon_code = info["weather"][0]["icon"]  # 獲取天氣圖示代碼

            # 根據圖片代碼組合圖標下載網址
            icon_url = f"{ICON_BASE_URL}{icon_code}@2x.png"

            # 下載圖標圖片
            icon_response = requests.get(icon_url)  # 發送 GET 請求下載圖標圖片
            # 若下載成功，就將圖標存於 png 檔案中
            if (
                icon_response.status_code == 200
            ):  # 如果圖標下載成功 (狀態碼 200)，則將圖標保存為 PNG 文件
                with open(
                    f"{icon_code}.png", "wb"
                ) as icon_file:  # 以二進制寫入模式打開文件
                    icon_file.write(icon_response.content)  # 將下載的圖標內容寫入文件

                # 更新天氣圖片
                try:
                    image = Image.open(f"{icon_code}.png")
                    image.thumbnail((100, 100))  # 調整圖片大小
                    weather_photo = ImageTk.PhotoImage(image)
                    weather_label.config(image=weather_photo)
                    weather_label.image = weather_photo
                except Exception as e:
                    print(f"無法載入圖片: {e}")
            else:
                # 如果圖標下載失敗，印出錯誤訊息
                print(f"無法下載圖標，HTTP 狀態碼: {icon_response.status_code}")

            # 根據勾選狀態顯示相應的溫度單位
            update_temperature_display()

            describe_label.config(
                text=f"天氣描述: {weather_description}"
            )  # 更新天氣描述
        else:
            print_label.config(text="城市未找到，請檢查輸入")  # 顯示錯誤訊息
    except Exception as e:
        print_label.config(text=f"錯誤: {str(e)}")
        print(f"API 請求失敗: {e}")


def update_temperature_display():
    """根據溫度單位的選擇更新溫度顯示"""
    global current_temp_celsius
    if check_type.get():
        # True：顯示攝氏度
        print_label.config(text=f"溫度: {current_temp_celsius:.1f}°C")
    else:
        # False：顯示華氏度
        celsius = current_temp_celsius
        fahrenheit = (celsius * 9 / 5) + 32
        print_label.config(text=f"溫度: {fahrenheit:.1f}°F")


def on_switch_change():
    # 當 Checkbutton 的狀態改變時，更新溫度顯示
    update_temperature_display()  # 根據勾選狀態更新溫度顯示


#######################建立視窗########################
# 建立主視窗
window = Window(themename="minty")  # 創建一個 ttkbootstrap 視窗並設置主題為 "minty"
# 設置窗口標題為 "天氣查詢"
window.title("天氣查詢")  # 設置窗口標題為 "天氣查詢"

#######################設定字形########################
# 設置全域大小
font_style = 20
# 設置全局字體為 Arial，大小為 20
window.option_add("*Font", ("Arial", font_style))

#######################設定主題#######################
# 主題已在 Window 創建時設置為 "minty"

#######################建立變數########################
# BooleanVar 是 Tkinter 中用於存儲布林值的變數類型
check_type = (
    BooleanVar()
)  # 創建一個 BooleanVar 變數 check_type 用於存儲 Checkbutton 的狀態 (選中或未選中)
# 預設為勾選狀態(True) - 表示攝氏度
check_type.set(True)  # 將 check_type 的值設置為 True，表示預設為攝氏度

# 預設圖片 - 等待用戶查詢後才更新
weather_photo = None  # 初始化為 None，稍後由 show_result() 更新

#######################建立標籤########################
# 創建一個 Label 標籤，顯示城市輸入提示
ask_label = Label(window, text="請輸入想搜尋的城市: ")  # 創建一個 Label，顯示輸入提示
# 將標籤放置在指定位置
ask_label.grid(
    row=0, column=0, padx=10, pady=10
)  # 使用 grid 方法將 ask_label 放置在窗口的第一行第一列，並設置內邊距

# 創建一個 Label 標籤，顯示溫度資訊
print_label = Label(window, text="溫度: ?°C")  # 創建一個 Label，顯示溫度
# 將標籤放置在指定位置
print_label.grid(
    row=1, column=1, padx=10, pady=10
)  # 使用 grid 方法將 print_label 放置在窗口的第二行第二列，並設置內邊距

# 創建一個 Label 標籤，顯示天氣圖示
weather_label = Label(window, text="天氣圖標")  # 創建一個 Label，初始顯示文字
# 將標籤放置在指定位置
weather_label.grid(
    row=1, column=0, padx=20, pady=20
)  # 使用 grid 方法將 weather_label 放置在窗口的第二行第一列，並設置內邊距

# 創建一個 Label 標籤，顯示天氣描述
describe_label = Label(window, text="描述: ?")  # 創建一個 Label，初始顯示文字
describe_label.grid(
    row=1, column=3, padx=20, pady=20
)  # 使用 grid 方法將 describe_label 放置在窗口的第二行第四列，並設置內邊距

# 創建一個 Label 標籤，顯示溫度單位選項
check_label = Label(window, text="溫度單位(°C/°F)")  # 創建一個 Label，顯示溫度單位選項
# 將標籤放置在指定位置
check_label.grid(
    row=2, column=1, padx=(50, 0), pady=10
)  # 使用 grid 方法將 check_label 放置在窗口的第三行第二列，並設置內邊距

#######################建立按鈕########################
# 顯示計算結果的按鈕
button = Button(
    window, text="獲得天氣資訊", command=show_result, style="my.TButton"
)  # 設定按鈕樣式
button.grid(
    row=0, column=3, columnspan=2, padx=20, pady=20
)  # 使用 grid 佈局管理器，將按鈕放在第一行第四列，並跨越兩列

#######################建立Entry物件########################
# Entry物件
entry = Entry(window, width=20)  # 創建一個Entry物件，設定寬度為20
entry.grid(
    row=0, column=1, columnspan=2, padx=10, pady=10
)  # 使用 grid 佈局管理器，將Entry物件放在第一行第二列，並跨越兩列
# padx 是水平內邊距，pady 是垂直內邊距，這裡設定為10像素。

#######################建立checkbutton########################
# 將 Checkbutton，會合 check_type 綁在一起
# True：攝氏度(°C)，False：華氏度(°F)
# 勾選時存 True，未勾選時存 False，並在狀態改變時呼叫 on_switch_change
check = Checkbutton(
    window, variable=check_type, onvalue=True, offvalue=False, command=on_switch_change
)  # 創建一個 Checkbutton，綁定 check_type 變數，並在狀態改變時呼叫 on_switch_change
# 將 Checkbutton 放置在指定位置
check.grid(
    row=2, column=1, padx=(0, 250), pady=10
)  # 使用 grid 方法將 check 放置在窗口的第三行第二列

#######################運行應用程式########################
# 啟動主事件循環，讓視窗保持顯示並等待用戶操作
window.mainloop()  # 啟動 Tkinter 的主事件循環，讓窗口保持顯示並等待用戶操作
