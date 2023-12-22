# app/dash_app.py
from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_table
import pandas as pd
import plotly.express as px

df = pd.read_csv('dash_file/方式.csv')

#這是註解
#
dash1 = Dash(requests_pathname_prefix="/dash/app1/")

dash1.layout = html.Div(
    [
        html.H1("自殺及自傷方式統計"),
        dash_table.DataTable(
            id="suicide-methods-table",
            columns=[
                {"name": "年度", "id": "年度"},
                {"name": "服毒自殺", "id": "以固體或液體物質自殺及自為中毒"},
                {"name": "以氣體自殺", "id": "以氣體及蒸汽自殺及自為中毒"},
                {"name": "窒息式自殺", "id": "吊死、勒死及窒息之自殺及自傷"},
                {"name": "用水自殺", "id": "溺水 (淹死)自殺及自傷"},
                {"name": "吞槍自殺", "id": "鎗砲及爆炸物自殺及自傷"},
                {"name": "切穿工具自殺及自傷", "id": "切穿工具自殺及自傷"},
                {"name": "由高處跳下自殺及自傷", "id": "由高處跳下自殺及自傷"},
                {"name": "其他及未明示之方式自殺及自傷", "id": "其他及未明示之方式自殺及自傷"},
            ],
            data=df.to_dict("records"),
        ),
        # 加入各種自殺方式的年度人數圓餅圖
        html.Div(id="pie-charts-container"),
    ]
)