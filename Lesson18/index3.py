'''
學習Canvas
'''
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)        
        self.title("Image")
        self.geometry("300x250")
        self.configure(background='#005CAF')

class MyFrame(ttk.LabelFrame):
    def __init__(self,master,title,**kwargs):
        super().__init__(master,text=title,**kwargs)
        #self.configure(background='#9B90C2')
        

        self.pack(expand=1, fill='both')


def main():    
    window = Window()
    myFrame = MyFrame(window,"今天吃咖喱飯！")
    window.mainloop()

if __name__ == "__main__":
    main()