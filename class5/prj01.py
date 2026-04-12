#######################匯入模組#######################
from ttkbootstrap import *  # pip install ttkbootstrap -U

# ttkbootstrap 包含了 ttk 所有模組的功能(除了 filedialog)，所以不需要再額外匯入 ttk 模組。
import sys
import os
from tkinter import filedialog
from PIL import Image, ImageTk  # pip install Pillow -U


#######################定義函數#######################
def open_file():
    global file_path  # 定義全局變量 file_path，這樣在其他函數中也可以訪問和修改它
    file_path = filedialog.askopenfilename(  # 當函式被發生，會彈出一個文件選擇對話框，讓用戶選擇一個文件。選擇完成後，所選文件的路徑將被存儲在 file_path 變量中。
        initialdir=sys.path[0],  # 設定初始目錄為當前腳本所在的目錄
    )
    label2.config(text=file_path)  # 更新 label2 的文本為選擇的文件路徑


def show_image():
    global file_path
    image = Image.open(file_path)  # 打開圖片檔案
    # 調整圖片大小，讓它適合畫布的尺寸
    # Image.LANCZOS 是一種高品質的重採樣濾鏡，適用於縮小圖片時，可以保持較好的圖像質量。
    # 它會把圖片縮小到指定的尺寸，同時盡量保持圖像的清晰度和細節，減少失真和模糊的情況。
    image = image.resize((canvas.winfo_width(), canvas.winfo_height()), Image.LANCZOS)

    # 轉換成 Tkinter 可用的圖片格式
    photo = ImageTk.PhotoImage(image)
    canvas.create_image(
        0, 0, anchor="nw", image=photo
    )  # 在畫布上顯示圖片，圖片的左上角位置為 (0, 0)
    canvas.image = photo  # 為了防止圖片被垃圾回收機制清除，需要將圖片對象保存在全局變量中，這樣它就不會被回收掉，從而確保圖片能夠


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
label = Label(window, text="選擇檔案")
label.grid(
    row=0, column=0, sticky="E"  # "E" 是東(East)對齊，讓標籤靠右對齊
)  # 使用 grid 佈局管理器，將標籤放在第一行第一列。 (row 是列，column 是行)

label2 = Label(window, text="無")
label2.grid(
    row=0, column=1, sticky="E"
)  # 使用 grid 佈局管理器，將標籤放在第二行第一列，並且跨越兩列(columnspan=2)，並且水平(E)和垂直(W)對齊 (sticky="Ew")。

######################建立按鈕########################
button = Button(
    window, text="瀏覽", command=open_file, style="my.TButton"
)  # 設定按鈕樣式
button.grid(
    row=0, column=2, sticky="w"
)  # 使用 grid 佈局管理器，將按鈕放在第一行第二列，並且靠左(西)對齊 (sticky="w")。
button2 = Button(
    window, text="顯示", command=show_image, style="my.TButton"
)  # 設定按鈕樣式
button2.grid(
    row=1,
    column=0,
    columnspan=3,
    sticky="Ew",  # "EW" 是東(East)和西(West)對齊，讓按鈕水平拉伸填滿整行
)  # 使用 grid 佈局管理器，將按鈕放在第二行第一列，並且跨越兩列(columnspan=2)，並且水平(E)和垂直(W)對齊 (sticky="Ew")。

canvas = Canvas(window, width=600, height=600)
canvas.grid(
    row=2, column=0, columnspan=3
)  # 使用 grid 佈局管理器，將畫布放在第三行第一列，並且跨越三列(columnspan=3)。

#######################運行應用程式########################
# 開始執行主迴圈，讓視窗保持顯示並等待用戶的操作
window.mainloop()
