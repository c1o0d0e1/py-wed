#######################匯入模組#######################
from ttkbootstrap import *  # pip install ttkbootstrap -U
import sys
import os

#######################設定工作目錄########################
os.chdir(sys.path[0])  # 設定工作目錄為當前腳本所在的目錄


#######################定義函數########################
def show_result():
    entry_text = entry.get()  # 取得Entry物件中的文字
    try:
        result = eval(entry_text)  # 計算Entry物件中的文字，並將結果存儲在result變量中
    except:
        result = "無效的表達式"  # 如果計算過程中出現錯誤，將result設置為"無效的表達式"
    label.config(text=f"計算結果: {result}")  # 更新label的文字，顯示計算結果


#######################建立視窗########################
window = Tk()
window.title("我的第一個視窗")  # 設定視窗的標題

#######################設定字型########################
font_size = 20  # 設定字形大小
window.option_add(
    "*Font", ("Arial", font_size)
)  # 設定全局字型為 Arial，大小為 font_size

#######################設定主題########################
style = Style(theme="darkly")  # 設定主題為 darkly
style.configure(
    "my.TButton", font=("Arial", font_size)
)  # 設定 "my.TButton" 樣式的字形、大小等屬性

#######################建立標籤########################
# 顯示計算結果的Label
label = Label(window, text="計算結果")
label.grid(
    row=2, column=0, columnspan=2, padx=10, pady=10
)  # 使用 grid 佈局管理器，將標籤放在第三行第一列，並且跨越兩列(columnspan=2)，並且設定內邊距(padx=10, pady=10)。

#######################建立按鈕########################
# 顯示計算結果的按鈕
button = Button(
    window, text="顯示計算結果", command=show_result, style="my.TButton"
)  # 設定按鈕樣式
button.grid(
    row=1, column=0, columnspan=2, padx=10, pady=10
)  # 使用 grid 佈局管理器，將按鈕放在第二行第一列，並且跨越兩列(columnspan=2)，並且設定內邊距(padx=10, pady=10)。

#######################建立Entry物件########################
# Entry物件
entry = Entry(window, width=30)  # 創建一個Entry物件，設定寬度為30
entry.grid(
    row=0, column=0, columnspan=2, padx=10, pady=10
)  # 使用 grid 佈局管理器，將Entry物件放在第一行第一列，並且跨越兩列(columnspan=2)，並且設定內邊距(padx=10, pady=10)。
# padx 是水平內邊距，pady 是垂直內邊距，這裡設定為10像素。

#######################運行應用程式########################
window.mainloop()
