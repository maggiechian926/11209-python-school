
import tkinter as tk  
from tkinter import ttk


class Window(tk.Tk):
    def __init__(self, **kwargs): #自定義 
        super().__init__(**kwargs) #呼叫附類別
        
def main():
    window = Window()
    window.title('台北市youbike2.0')
    window.geometry('600x300') #設定視窗大小尺寸
    window.resizable(width=False,height=False) #固定視窗尺寸
    window.mainloop() #執行迴圈 
    
if __name__== '__main__':
    main()