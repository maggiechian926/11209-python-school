import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datasource
from threading import Timer

class Window(tk.Tk):                       
    def __init__(self, **kwargs):          
        super().__init__(**kwargs)         
        try:
            datasource.update_sqlite_data()
        except Exception as e:                     
            messagebox.showerror("錯誤",f'{e}\n將關閉應用程式\n請稍後再試')
            self.destroy()                 
    

t = None
def main():
    def on_closing():
        print("window關閉")
        if t is not None:
            t.cancel()  # 只有當 t 不為 None 時才嘗試取消計時器
        if window.winfo_exists():  # 檢查視窗是否存在
            window.destroy()

    window = Window()
    window.geometry('600x300')
    window.resizable(width=False, height=False)
    window.protocol("WM_DELETE_WINDOW", on_closing)

    if window.winfo_exists():  # 檢查視窗是否存在，然後再設置視窗標題
        window.title('空氣品質監測站基本資料')

    update_data()
    window.mainloop()




if __name__ == '__main__':
    main()