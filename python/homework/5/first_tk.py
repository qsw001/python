import tkinter

class CanvasDemo:
    def __init__(self):
        myWindow = tkinter.TK()
        myWindow.geometry('640x480+400+400')
        myWindow.title("Canvas Demo")

        self.canvas = tkinter.Canvas(myWindow, width = 620, height = 420, bg = "white")
        self.canvas.pack( padx=(10, 10), pady=(10, 10))

        frame = tkinter.Frame(myWindow)
        frame.pack()

        btRectangle = tkinter.Button(frame, text="Rectangle", command=self.displayRect)
        btClear = tkinter.B


# def click():
#     print("点击按钮")

# root = tk.Tk()
# root.title("Hello")
# root.geometry("800x500")

# label = tk.Label(root, text="你好").grid(row=0,column=0)

# button = tk.Button(root, text="点我", command=click).grid(row=1,column=1)

# root.mainloop()