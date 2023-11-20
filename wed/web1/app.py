from flask import Flask,url_for,render_template
import random
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    name = "徐國堂"
    dataFrame = get_dataFrame()
    return render_template('index.html',name=name,dataFrame=dataFrame)

def get_dataFrame()->pd.DataFrame:
    data = [['徐國堂',67,92,85],
            ['王XX',78,97,65],
            ['李XX',92, 79, 85]]    
    
    return pd.DataFrame(data,columns=["姓名","國文","英文","數學"])