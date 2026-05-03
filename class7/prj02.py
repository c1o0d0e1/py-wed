#######################匯入模組#######################
from ttkbootstrap import *

import os
import sys

from PIL import Image, ImageTk  # 載入 PIL 模組中的 Image 和 ImageTk 類別，用於處理圖像

#######################設定工作目錄########################
# 將當前工作目錄更改為腳本所在的目錄，確保能夠正確地找到相關的文件和資源。
os.chdir(sys.path[0])

#######################建立視窗########################
# 建立主視窗
window = Tk()  # 創建一個 Tkinter 主窗口對象
# 設置窗口標題為 "天氣查詢"
window.title("天氣查詢")  # 設置窗口標題為 "天氣查詢"

#######################讀取圖片########################
# 這張 weather.png 圖片是從 openweathermap API 下載的天氣圖示，請確保這個圖片已經存在於腳本所在的目錄中
image = Image.open("04d.png")  # 使用 PIL 的 Image 模組打開名為 "weather.png" 的圖片文件
# tkinter 不能直接顯示 PIL 的 Image 物件，需要將其轉換為 ImageTk.PhotoImage 物件
weather_photo = ImageTk.PhotoImage(
    image
)  # 將 PIL 的 Image 物件轉換為 Tkinter 可用的 PhotoImage 物件

#######################建立標籤########################
# 創建一個 Label 標籤，顯示天氣圖示
weather_label = Label(
    window, image=weather_photo
)  # 創建一個 Label，並將 weather_photo 圖片設置為其內容
# 將標籤放置在指定位置
weather_label.pack(
    padx=20, pady=20
)  # 使用 pack 方法將 weather_label 放置在窗口中，並設置內邊距
weather_label.image = weather_photo  # 將 weather_photo 物件保存在 weather_label 的 image 屬性中，以防止被垃圾回收

#######################運行應用程式########################
# 啟動 Tkinter 的事件循環，使應用程式開始運行並等待用戶操作
window.mainloop()  # 啟動 Tkinter 的事件循環，使應用程式開始運行
