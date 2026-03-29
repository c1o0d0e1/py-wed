#######################匯入模組#######################
from tkinter import *  # pip install ttkbootstrap -U
from PIL import Image, ImageTk
import sys
import os

# * 是匯入模組中所有的函數、類別和變數，這樣就可以直接使用它們而不需要加上模組名稱作為前綴。

#######################設定工作目錄#######################
# 設定工作目錄
os.chdir(sys.path[0])


#######################定義函數#######################
# 定義一個函數，用於移動圓形物件，根據按鍵的不同來決定移動的方向。
def move_circle(event):
    # 取得按下的按鍵
    key = (
        event.keysym
    )  # keysym 是 event 物件的一個屬性，表示按下的按鍵的名稱，例如 "Right"、"Left"、"Up"、"Down"、"w"、"s"、"a"、"d" 等。
    print(key)
    if key == "Right":
        canvas.move(circle, 10, 0)  # 向上移動
    elif key == "Left":
        canvas.move(circle, -10, 0)  # 向下移動
    elif key == "Up":
        canvas.move(circle, 0, -10)  # 向左移動
    elif key == "Down":
        canvas.move(circle, 0, 10)  # 向右移動
    elif key == "w":
        canvas.move(rectangle, 0, -10)  # 向上移動
    elif key == "s":
        canvas.move(rectangle, 0, 10)  # 向下移動
    elif key == "a":
        canvas.move(rectangle, -10, 0)  # 向左移動
    elif key == "d":
        canvas.move(rectangle, 10, 0)  # 向右移動


# 定義一個函式，用來關閉程式。
def exit_fun():
    window.destroy()  # 使用 destroy() 方法來關閉視窗，從而結束程式的運行。


#######################建立(主)視窗########################
# 創建一個主視窗
window = Tk()

# 設定視窗的標題
window.title("我的第一個視窗")

#######################創建按鈕########################
# 建立一個按鈕，用來關閉程式，並將它放置在視窗中。
button = Button(
    window, text="Quit", command=window.destroy
)  # 變數 = Button(視窗, text="按鈕文字", command=按鈕被按下時要執行的函數)
"""
注意!!! 文字不可以寫 ssutdown ，會直接把電腦關機，請小心使用。
"""
button.pack()  # 使用 pack() 方法將按鈕放置在視窗中
#######################創建畫布########################
# 創建一個畫布，指定寬度和高度
canvas = Canvas(window, width=600, height=600, bg="white")
# 將畫布放置在視窗中
canvas.pack()

#######################設定視窗圖片########################
# 設定視窗圖片
window.iconbitmap("crocodile2.png")

#######################載入圖片########################
# [pillow 方式] 使用 Image.open() ，用於打開圖像文件，返回一個 Image 對象。
# 好處:
#     1. 支持更多的圖像格式，如 JPEG、BMP、TIFF 等，而不僅限於 PNG 和 GIF。
#     2. 提供了更多的圖像處理功能，如旋轉、縮放、裁剪等。
#     3. 可在顯示前對圖像進行更多的操作和處理。
image = Image.open("crocodile2.png")
# 將 PIL Image 物件轉換成 Tkinter 可用(顯示)的 PhotoImage 物件
# 注意!!! 需保留 img 的參照，否則圖片會被 Python 的垃圾回收機制回收，導致圖片無法顯示並消失。
img = ImageTk.PhotoImage(image)

#######################顯示圖片########################
# 在畫布上顯示圖片，指定位置為 (300, 300)，並將圖片的中心對齊
my_img = canvas.create_image(300, 300, image=img)

#######################畫圖形########################
# 在畫布上繪製一個圓形，起點為 (250, 150)，終點為 (300, 200)，填充顏色為紅色。
circle = canvas.create_oval(250, 150, 300, 200, fill="red")

# 在畫布上繪製一個矩形，起點為 (220, 400)，終點為 (340, 230)，填充顏色為藍色。
rectangle = canvas.create_rectangle(220, 400, 340, 230, fill="blue")

# 在畫布上繪製一段文字，起點為 (300, 100)，文字為 Crocodile，顏色為黑色，字體為 Arial，大小為 30。
msg = canvas.create_text(300, 100, text="Crocodile", fill="black", font=("Arial", 30))

#######################綁定按鍵事件########################
# 將按鍵事件綁定到主視窗，當按下指定的按鍵時，移動對應的物件。
canvas.bind_all("<Key>", move_circle)
#######################運行應用程式########################
# 開始執行主迴圈，讓視窗保持顯示並等待用戶的操作
window.mainloop()
