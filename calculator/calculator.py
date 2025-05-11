import tkinter as tk
import math

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            expression = entry.get()
            # 記号をPythonの演算子に変換
            expression = expression.replace("×", "*").replace("÷", "/").replace("^", "**")
            # eval を使用して計算
            result = eval(expression)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    elif text == "√":
        try:
            value = float(entry.get())
            result = math.sqrt(value)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("簡易電卓")
root.geometry("400x500")  # ウィンドウサイズを指定
root.configure(bg="#f0f0f0")  # 背景色を設定

# 入力欄
entry = tk.Entry(root, font=("Arial", 24), justify="right", bd=10, relief=tk.FLAT)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# ボタンのリスト
buttons = [
    "C", "(", ")", "÷",
    "7", "8", "9", "×",
    "4", "5", "6", "-",
    "1", "2", "3", "+",
    "0", ".", "^", "=",
    "√", "", "", ""
]

# ボタンの配置
row, col = 1, 0
for button in buttons:
    if button != "":
        btn = tk.Button(
            root, text=button, font=("Arial", 18), width=5, height=2,
            bg="#ffffff", fg="#000000", relief=tk.GROOVE, activebackground="#d9d9d9"
        )
        btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
        btn.bind("<Button-1>", click)
    col += 1
    if col > 3:
        col = 0
        row += 1

# 行と列のサイズを調整
for i in range(6):  # 行数
    root.grid_rowconfigure(i, weight=1)
for j in range(4):  # 列数
    root.grid_columnconfigure(j, weight=1)

root.mainloop()