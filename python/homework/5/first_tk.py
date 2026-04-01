import tkinter as tk

def click():
    print("点击按钮")

root = tk.Tk()
root.title("Hello")
root.geometry("800x500")

label = tk.Label(root, text="你好").grid(row=0,column=0)

button = tk.Button(root, text="点我", command=click).grid(row=1,column=1)

root.mainloop()