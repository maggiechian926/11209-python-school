import dataSource
import tkinter as tk
from tkinter import ttk

class Window (tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
def main():
    window = Window()
    window.title("這是我的首頁")
    label= tk.Label(window,text="hello,tkinter!",font= ('Halvetica','35'))
    label.pack(padx=100,pady=50)
    
    window.mainloop()
    

if __name__ == "__main__":
    main()