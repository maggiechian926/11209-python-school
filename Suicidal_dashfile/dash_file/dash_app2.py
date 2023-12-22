import dash
from dash import html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import dash
import dash_bootstrap_components as dbc
import dash_table
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from dash import Dash, html, dcc, callback, Output, Input
import dash_html_components as html

# 讀取 CSV 文件
df = pd.read_csv('dash_file/方式.csv')

# 初始化 Dash 應用
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# 定義背景顏色與文字
colors = {
    'background': '#86473F',
    'text': '#006284'}

# 生成圓餅圖
def generate_pie_chart(selected_method):
    filtered_df = df[df[selected_method] == 1]  # 根據選擇的按鈕過濾數據
    return dcc.Graph(
        id="suicide-pie-chart",
        figure=go.Figure(
            data=[go.Pie(
                labels=filtered_df["年度"],
                values=filtered_df["以固體或液體物質自殺及自為中毒"],
                marker=dict(colors=px.colors.sequential.YlGn)
            )],
            layout=go.Layout(
                title="圓餅圖",
                width=450,
                height=450,
                margin=dict(l=100, r=20, b=20, t=120),
                showlegend=False,
                paper_bgcolor="rgba(0,0,0,0)",  # 透明背景
                plot_bgcolor="rgba(0,0,0,0)",  # 透明背景
            )
        ).update_layout(title_x=0.58),
        style={"width": "500px", "height": "500px"}
    )

# 生成長條圖
def generate_bar_chart(selected_method):
    filtered_df = df[df[selected_method] == 1]  # 根據選擇的按鈕過濾數據
    return dcc.Graph(
        id="suicide-bar-chart",
        figure=px.bar(
            filtered_df,
            x="年度",
            y="以固體或液體物質自殺及自為中毒",
            title="長條圖",
            color="年度",
            color_discrete_sequence=px.colors.sequential.YlGn,
        ).update_layout(title_x=0.5),
        style={"width": "500px", "height": "500px"}
    )

# 生成折線圖
def generate_line_chart(selected_method):
    filtered_df = df[df[selected_method] == 1]  # 根據選擇的按鈕過濾數據
    method = "以固體或液體物質自殺及自為中毒"
    updated_chart = dcc.Graph(
        id=f"suicide-line-chart-{method}",
        figure={
            "data": [
                go.Scatter(
                    x=filtered_df["年度"],
                    y=filtered_df[method],
                    mode="lines+markers",
                )
            ],
        },
    )
    return updated_chart

# 定義 Dash 應用的布局
app.layout = html.Div(
    dbc.Container([
        html.Div(id='output-container'),
        html.Div([
            dbc.Button("服毒自殺", id="poison", color="primary", className="mx-auto"),
            dbc.Button("氣體自殺", id="gas", color="info", className="mx-auto"),
            dbc.Button("窒息式自殺", id="drown", color="info", className="mx-auto"),
            dbc.Button("用水自殺", id="water", color="info", className="mx-auto"),
            dbc.Button("吞槍自殺", id="gun", color="info", className="mx-auto"),
            dbc.Button("切穿自殺", id="cut", color="info", className="mx-auto"),
            dbc.Button("跳樓自殺", id="hjump", color="info", className="mx-auto"),
            dbc.Button("未明示自殺", id="idon", color="info", className="mx-auto"),
            dbc.Button("首頁", id="home", color="info", className="mx-auto"),
            
            # 其他按鈕類似，請根據實際情況擴展
        ], className="button_box1"),
        html.Div([
            html.Div(generate_pie_chart(selected_method)),
            html.Div(generate_bar_chart(selected_method)),
            html.Div(generate_line_chart(selected_method)),
        ], className='buttom_box'),
    ], fluid=True)
)

# 定義回調函數
@app.callback(
    [Output("output-container", "children"),
     Output("suicide-pie-chart", "children"),
     Output("suicide-bar-chart", "children"),
     Output("suicide-line-chart-以固體或液體物質自殺及自為中毒", "children"),
     
     Output("output-container", "children"),
     Output("suicide-pie-chart", "children"),
     Output("suicide-bar-chart", "children"),
     Output("suicide-line-chart-以氣體及蒸汽自殺及自為中毒", "children"),
     
     Output("output-container", "children"),
     Output("suicide-pie-chart", "children"),
     Output("suicide-bar-chart", "children"),
     Output("suicide-line-chart-吊死、勒死及窒息之自殺及自傷", "children"),
     
     Output("output-container", "children"),
     Output("suicide-pie-chart", "children"),
     Output("suicide-bar-chart", "children"),
     Output("suicide-line-chart-溺水 (淹死)自殺及自傷", "children"),
     
     Output("output-container", "children"),
     Output("suicide-pie-chart", "children"),
     Output("suicide-bar-chart", "children"),
     Output("suicide-line-chart-鎗砲及爆炸物自殺及自傷", "children"),
     
     Output("output-container", "children"),
     Output("suicide-pie-chart", "children"),
     Output("suicide-bar-chart", "children"),
     Output("suicide-line-chart-切穿工具自殺及自傷", "children"),
     
     Output("output-container", "children"),
     Output("suicide-pie-chart", "children"),
     Output("suicide-bar-chart", "children"),
     Output("suicide-line-chart-由高處跳下自殺及自傷", "children"),
     
     Output("output-container", "children"),
     Output("suicide-pie-chart", "children"),
     Output("suicide-bar-chart", "children"),
     Output("suicide-line-chart-其他及未明示之方式自殺及自傷", "children"),
     
    
     ],
    
    
    [Input("poison", "n_clicks"),
     Input("gas", "n_clicks"),
     Input("drown", "n_clicks"),
     Input("water", "n_clicks"),
     Input("gun", "n_clicks"),
     Input("cut", "n_clicks"),
     Input("hjump", "n_clicks"),
     Input("idon", "n_clicks"),
     Input("home", "n_clicks"),]
     # 其他按鈕類似，請根據實際情況擴展
)
def update_output(n_clicks_poison, n_clicks_gas, n_clicks_drown, n_clicks_water, n_clicks_gun, n_clicks_cut, n_clicks_hjump, n_clicks_idon, n_clicks_home):
    selected_method = None  # 或者您可以設置為默認的方法

    
    
    ctx = dash.callback_context
    button_id = "poison"
    
    if not ctx.triggered_id:
        button_id = "poison"  # 預設為第一個按鈕
    else:
        button_id = ctx.triggered_id.split(".")

    if button_id == "poison":
        selected_method = "服毒自殺"
    elif button_id == "gas":
        selected_method = "氣體自殺"
    # 其他按鈕類似，請根據實際情況擴展

    return (
    f"You clicked the {button_id} button!", 
    generate_pie_chart(selected_method), 
    generate_bar_chart(selected_method), 
    generate_line_chart(selected_method)
    )


# 啟動應用
if __name__ == "__main__":
    app.run_server(debug=True)
