# cget() 取得標籤的屬性值
# display.cget(text="green", fg="black", bg="green")

# random.choice() 從序列中隨機選擇一個元素
# random.choices() 從序列中隨機選擇多個元素，並返回一個列表

# os.chdir() 改變當前工作目錄
# sys.path[0] 返回當前腳本所在的目錄
# os.chdir(sys.path[0]) 將當前工作目錄設置為腳本所在的目錄，這樣就可以確保在執行腳本時能夠正確地找到相關的文件和資源。
# initialdir=sys.path[0] 在 filedialog.askopenfilename() 函數中，initialdir 參數用於指定文件選擇對話框的初始目錄。通過將 initialdir 設置為 sys.path[0]，可以確保文件選擇對話框在打開時會顯示當前腳本所在的目錄，方便用戶快速找到相關的文件。

# filedialog.askopenfilename() 是 tkinter 模組中的一個函數，用於打開一個文件選擇對話框，讓用戶選擇一個文件。當用戶選擇完成後，所選文件的路徑將被返回並存儲在變量中。

# row 是列
# column 是行
# 下列為 row 與 column 的圖示:
"""
    column 0   column 1   column 2
row 0   (0,0)      (0,1)      (0,2)
row 1   (1,0)      (1,1)      (1,2)
row 2   (2,0)      (2,1)      (2,2)
"""

# command 是按鈕被點擊時要執行的函數，假設是 open_file 函數，當按鈕被點擊時會呼叫 open_file 函數來執行相關的操作。

# padx 是水平內邊距，pady 是垂直內邊距，這裡設定為10像素。這樣可以確保按鈕與其他元素之間有適當的空間，提升界面的美觀和可讀性。
# 下列為 padx 與 pady 的圖示:
"""
    padx=10
    |<-- 10px -->|   <-- 10px -->|
    [按鈕]         [其他元素]

    pady=10
    ^             ^
    |             |
    10px          10px
    |             |
    [按鈕]
    [其他元素]
"""

# eval() 函數用於計算字符串中的 Python 表達式，並返回計算結果。這個函數可以用來執行動態生成的代碼，但需要注意安全性問題，因為它會執行任何傳入的字符串。
