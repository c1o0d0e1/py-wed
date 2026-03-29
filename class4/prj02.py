#######################匯入模組#######################
from ttkbootstrap import *  # pip install ttkbootstrap -U


#######################定義函數#######################
def text():
    print("Hello World!")


#######################建立(主)視窗########################
# 創建一個主視窗
window = Tk()

# 設定視窗的標題
window.title("我的第一個視窗")

######################設定字形########################
# 設定字形大小
font_size = 20
window.option_add(
    "*Font", ("Arial", font_size)
)  # 設定全局字形為 Arial，大小為 font_size

######################設定主題########################
# 設定主題
style = Style(theme="darkly")  # 設定主題為 darkly
# "my.TButton" 的命名編輯:
# 就像幫東西貼標籤一樣，分成兩個部分，用 (,) 隔開:
#    前部分 "my" 是自定義的標籤，可以隨意命名(big, red)。
#    後部分 "TButton" 是固定寫法， ttk 模組中按鈕的類型，表示這個樣式是用於按鈕的。
# 常見元件的後半段寫法:
#    按鈕 -> TButton
#    標籤 -> TLabel
#    輸入框 -> TEntry
style.configure(
    "my.TButton",
    font=("Arial", font_size),
)  # 設定 "my.TButton" 樣式的字形、大小等屬性

######################建立標籤########################
label = Label(window, text="Hello World!")
label.grid(
    row=0, column=0
)  # 使用 grid 佈局管理器，將標籤放在第一行第一列。 (row 是列，column 是行)

######################建立標籤########################
button = Button(window, text="瀏覽", command=text, style="my.TButton")  # 設定按鈕樣式
button.grid(
    row=0, column=1, sticky="w"
)  # 使用 grid 佈局管理器，將按鈕放在第一行第二列，並且靠左(西)對齊 (sticky="w")。
button2 = Button(window, text="顯示", command=text, style="my.TButton")  # 設定按鈕樣式
button2.grid(
    row=1, column=0, columnspan=2, sticky="Ew"
)  # 使用 grid 佈局管理器，將按鈕放在第二行第一列，並且跨越兩列(columnspan=2)，並且水平(E)和垂直(W)對齊 (sticky="Ew")。

#######################運行應用程式########################
# 開始執行主迴圈，讓視窗保持顯示並等待用戶的操作
window.mainloop()
