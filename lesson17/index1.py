import dataSource
import tkinter as tk
from tkinter import ttk

class Window (tk.Tk):
    def __init__(self, **kwargs):
      super().__init__(**kwargs)
      self.title("這是我的首頁")
      label= tk.Label(self,text="hello,tkinter!",font= ('Halvetica','35'))
      label.pack(padx=100,pady=50)
    
def main():
    window = Window()
    window.mainloop()
    

if __name__ == "__main__":
    main()