#######################匯入模組#######################
from ttkbootstrap import *

import os
import sys

#######################設定工作目錄########################
# 將當前工作目錄更改為腳本所在的目錄，確保能夠正確地找到相關的文件和資源。
os.chdir(sys.path[0])


#######################定義函數########################
def on_switch_change():
    # 當 Checkbutton 的狀態改變時，更新目前 check_label 的文字
    check_label.config(
        text=str(check_type.get())
    )  # 將 check_type 的值轉換為字符串並更新 check_label 的文字


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
# 預設為勾選狀態(True)
check_type.set(True)  # 將 check_type 的值設置為 True，表示預設為勾選狀態

#######################建立標籤########################
# 創建一個 Label 標籤，顯示 checkbutton 對應的布林值
check_label = Label(window, text="True")  # 創建一個 Label，顯示 check_type 的值
# 將標籤放置在指定位置
check_label.grid(
    row=1, column=2, padx=10, pady=10
)  # 使用 grid 方法將 check_label 放置在窗口的第一行第二列，並設置內邊距

#######################建立checkbutton########################
# 將 Checkbutton，會合 check_type 綁在一起
# 勾選時存 True，未勾選時存 False，並在狀態改變時呼叫 on_switch_change
check = Checkbutton(
    window, variable=check_type, onvalue=True, offvalue=False, command=on_switch_change
)  # 創建一個 Checkbutton，綁定 check_type 變數，並在狀態改變時呼叫 on_switch_change
# 將 Checkbutton 放置在指定位置
check.grid(
    row=1, column=1, padx=10, pady=10
)  # 使用 grid 方法將 check 放置在窗口的第一行第一列，並設置內邊距

#######################運行應用程式########################
# 啟動主事件循環，讓視窗保持顯示並等待用戶操作
window.mainloop()  # 啟動 Tkinter 的主事件循環，讓窗口保持顯示並等待用戶操作
