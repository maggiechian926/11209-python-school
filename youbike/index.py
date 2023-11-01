import tkinter as tk
from tkinter import ttk
from youbikeTreeView import YoubikeTreeView
from tkinter import messagebox
from threading import Timer
import datasource

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        #---------更新資料庫資料-----------------#
        try:
            datasource.updata_sqlite_data()
        except Exception:
            messagebox.showerror("錯誤",'網路不正常\n將關閉應用程式\n請稍後再試')
            self.destroy()           
        search_frame = tk.Frame(self)
        tk.Label(search_frame, text="站點名稱搜索：", font=("arial", 12)).pack(side='left', padx=5, pady=5)
        self.search_entry = tk.Entry(search_frame)
        self.search_entry.pack(side='left', padx=5, pady=5)
        search_button = tk.Button(search_frame, text="搜尋", command=self.perform_search)
        search_button.pack(side='left', padx=5, pady=5)
        search_frame.pack()

        #---------建立介面------------------------
        #print(datasource.lastest_datetime_data())
        topFrame = tk.Frame(self,relief=tk.GROOVE,borderwidth=1)
        tk.Label(topFrame,text="台北市youbike及時資料",font=("arial", 20), bg="#007799", fg='#ffffff',padx=10,pady=10).pack(padx=20,pady=20)
        topFrame.pack(pady=30)

        bottomFrame = tk.Frame(self)
        #---------------建立treeView---------------
        self.youbikeTreeView = YoubikeTreeView(bottomFrame,show="headings",columns=('sna','mday','sarea','ar','tot','sbi','bemp'))
        self.youbikeTreeView.pack(side='left')
        vsb = ttk.Scrollbar(bottomFrame, orient="vertical", command=self.youbikeTreeView.yview)
        vsb.pack(side='left',fill='y')
        self.youbikeTreeView.configure(yscrollcommand=vsb.set)
        bottomFrame.pack(pady=30)
        print(datasource.search_sitename('三'))
        
    def perform_search(self):
            
            query = self.search_entry.get()
            search_result = datasource.search_sitename(query)
            self.youbikeTreeView.update_content(search_result)

        


def main():    
    def update_data(w:Window)->None:
        datasource.updata_sqlite_data()
        #-----------更新treeView資料---------------
        lastest_data = datasource.lastest_datetime_data()
        w.youbikeTreeView.update_content(lastest_data)

        window.after(3*60*1000,update_data,w) #每隔3分鐘
          

    window = Window()
    window.title('台北市youbike2.0')
    #window.geometry('600x300')
    window.resizable(width=False,height=False)
    update_data(window)          
    window.mainloop()

if __name__ == '__main__':
    main()