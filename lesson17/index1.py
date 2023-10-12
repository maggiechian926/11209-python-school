import dataSource
import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title("鄉鎮人口統計")
        self.configure(background='#A8D8B9')

        topFrame = tk.Frame(self,background='#90B44B')
        label = ttk.Label(topFrame,text="鄉鎮人口統計",font=('Helvetica', '30'))
        label.pack(padx=20,pady=20)
        topFrame.pack()

        bottomFrame = tk.Frame(self,background='#DAC9A6')
        choices = dataSource.cityNames()
        choicesvar = tk.StringVar(value=choices)
        listbox = tk.Listbox(bottomFrame,listvariable=choicesvar,width=13)
        listbox.pack(pady=20)
        bottomFrame.pack(expand=True,fill='x')
        
        listbox.bind("<<ListboxSelect>>",self.user_selected)
        
    def user_selected(self,event):
         print("user selecte")


def main():
    window = Window()    
    window.mainloop()
    

if __name__ == "__main__":
    main()