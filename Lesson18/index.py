'''
  學習Canvas
'''

import tkinter as tk
from tkinter import  ttk
from PIL import Image,ImageTk

class Window(tk.Tk):
    def __init__ (self,**kwargs):
        super().__init__(**kwargs)
        self.title("Images")
        self.geometry("300x250")
        self.configure(background='#7B90D2')
                
class MyFrame(tk.Frame)  :
    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)
        self.configure(background='#6E75A4')
        self.img = Image.open("pets.png")
        self.pets =ImageTk.PhotoImage(self.img)
        canvas = tk.Canvas(self,
                           width=48,
                           height = 48
                           )
        canvas.create_image(24,24,image=self.pets,anchor=tk.CENTER)
        canvas.pack()
        self.pack(expand=1,fill='both')
        
        
def main():
    '''
    param:
    使用說明書
    誰要放到誰家的用法
    
    '''
    window = Window()
    myFrame = MyFrame(master=window)
    window.mainloop()
       
if __name__ == "__main__":
    main()
    