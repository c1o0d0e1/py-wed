#######################匯入模組#######################
from tkinter import *


# * 是匯入模組中所有的函數、類別和變數，這樣就可以直接使用它們而不需要加上模組名稱作為前綴。
#######################定義函數########################

green = False


def clear_fun():
    # 清除顯示的文字，將標籤的文字設置為空字符串。
    display.config(text="", fg="white", bg="white")


def hi_fun():
    global green
    green = not (green)
    print("hi, welcome to my first GUI")
    if green:
        clear_fun()
        display.config(text="green", fg="black", bg="green")
    else:
        clear_fun()
        display.config(text="red", fg="black", bg="red")


#######################建立視窗########################
# 建立主視窗
windows = Tk()
# 設定視窗標題
windows.title("my first GUI")
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
