import tkinter as tk
from tkinter import messagebox
import math

class TriangleGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("三角形面积")
        self.window.geometry("420x160+400+300")

        tk.Label(self.window,text="边长A").grid(row=0,column=0,padx=8,pady=15)
        tk.Label(self.window,text="边长B").grid(row=0,column=2,padx=8,pady=15)
        tk.Label(self.window,text="边长C").grid(row=0,column=4,padx=8,pady=15)

        self.v1 = tk.StringVar(value="3")
        self.v2 = tk.StringVar(value="4")
        self.v3 = tk.StringVar(value="5")
        self.result = tk.StringVar()

        tk.Entry(self.window,textvariable=self.v1,width=8,justify=tk.RIGHT).grid(row=0,column=1)
        tk.Entry(self.window,textvariable=self.v2,width=8,justify=tk.RIGHT).grid(row=0,column=3)
        tk.Entry(self.window,textvariable=self.v3,width=8,justify=tk.RIGHT).grid(row=0,column=5)

        tk.Button(self)