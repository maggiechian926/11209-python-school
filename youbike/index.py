
import tkinter as tk  
from tkinter import ttk
from tkinter import messagebox
import datasource

class Window(tk.Tk):
    def __init__(self, **kwargs): #自定義 
        super().__init__(**kwargs) #呼叫附類別 
        try:
            datasource.download_youbike_data()
        except Exception as e:
            messagebox.showerror("錯誤",f'{e}\n將關閉應用程式\n請稍後再試') #show 下載失敗的視窗ok
            self.destroy()
            
        
        
def main():
    window = Window()
    window.title('台北市youbike2.0')
    window.geometry('600x300') #設定視窗大小尺寸
    window.resizable(width=False,height=False) #固定視窗尺寸
    window.mainloop() #執行迴圈 
    
if __name__== '__main__':
    main()