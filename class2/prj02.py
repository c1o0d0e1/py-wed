#######################匯入模組#######################
from tkinter import *
import random

# * 是匯入模組中所有的函數、類別和變數，這樣就可以直接使用它們而不需要加上模組名稱作為前綴。
#######################定義函數########################

green = False


def clear_fun():
    # 清除顯示的文字，將標籤的文字設置為空字符串。
    display.config(text="", fg="white", bg="white")


def hi_fun():
    # 顯示"hi singular"， 並任選一種顏色
    fg_color = "#" + "".join(random.choices("0123456789abcdef") for j in range(6))
    """
    比對展開寫法
    fg_color = "#"
    for j in range(6):
        fg_color += random.choice("0123456789abcdef")
    """
    bg_color = "#" + "".join(random.choices("0123456789abcdef") for j in range(6))
    display.config(
        text="hi singular", fg=fg_color, bg=bg_color
    )  # 將標籤的文字設置為"hi singular"，前景顏色和背景顏色分別設置為隨機生成的顏色。


#######################建立視窗########################
# 建立主視窗
windows = Tk()

# 設定視窗標題
windows.title("my first GUI")

# 建立字體, 大小為 20
windows.option_add(
    "*font", "標楷體 20"
)  # 新細明體, 微軟正黑體, 標楷體, 華康少女文字體, 華康娃娃體, 華康儷金黑體, 華康儷金圓體

###########################建立按鈕########################
# 建立一個按鈕，當按鈕被點擊時，會呼叫 hi_fun 函數。
btn1 = Button(windows, text="show Screen", command=hi_fun)
# 將按鈕放置在視窗中，使用 pack()
btn1.pack()
###########################建立標籤########################
# 建立一個標籤，顯示 "" 的文字。(背景為紅色，前景為黑色)
display = Label(windows, text="")
# 將標籤放置在視窗中，使用 pack()
display.pack()
#######################運行應用程式########################
# 執行主視窗的事件循環，讓視窗保持顯示狀態，等待用戶的操作。
windows.mainloop()
