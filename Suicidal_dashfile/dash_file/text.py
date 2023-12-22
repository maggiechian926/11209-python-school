import dash
import dash_bootstrap_components as dbc
import dash_table
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from dash import Dash, html, dcc, callback, Output, Input
import dash_html_components as html





df = pd.read_csv('dash_file/方式.csv')
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])


def generate_pie_chart():
    return dcc.Graph(
        id="suicide-pie-chart",
        figure=go.Figure(
            data=[go.Pie(
                labels=df["年度"],
                values=df["以固體或液體物質自殺及自為中毒"],
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

# Function to generate bar chart
def generate_bar_chart():
    return dcc.Graph(
        id="suicide-bar-chart",
        figure=px.bar(
            df,
            x="年度",
            y="以固體或液體物質自殺及自為中毒",
            title="長條圖",
            color="年度",
            color_discrete_sequence=px.colors.sequential.YlGn,
        ).update_layout(title_x=0.5),
        style={"width": "500px", "height": "500px"}
    )

# Function to generate line charts
def generate_line_chart():
    method = "以固體或液體物質自殺及自為中毒"
    updated_chart = dcc.Graph(
        id=f"suicide-line-chart-{method}",
        figure={
            "data": [
                go.Scatter(
                    x=df["年度"],
                    y=df[method],
                    mode="lines+markers",
                )
            ],
        },
    )
    return updated_chart


dash1 = Dash(requests_pathname_prefix="/dash/app1/")


dash1.layout = html.Div (
    
        html.H1("自殺及自傷方式統計",style=     
             {'textAlign':'center'}),
            html.Div([
                html.Div([
        dbc.Button("服毒自殺", color="primary", className="me-1"),
        dbc.Button("氣體自殺", color="secondary", className="me-1"),
        dbc.Button("窒息式自殺", color="success", className="me-1"),
        dbc.Button("用水自殺", color="warning", className="me-1"),
        dbc.Button("吞槍自殺", color="danger", className="me-1"),
        dbc.Button("切穿自殺", color="info", className="me-1"),
        dbc.Button("跳樓自殺", color="light", className="me-1"),
        dbc.Button("未明示自殺", color="dark", className="me-1"),  
            ],className="button_box1")],className='buttom_box'),
        
      
        
         dbc.Container([
            html.Div(generate_pie_chart()),
            html.Div(generate_bar_chart()),
            html.Div(generate_line_chart()),
        #定義dash的格局，html.H1代表1级標题，也就是大標题；里面的html.Div代表一个分割塊
            #html.Div(children='When the going gets tough, the tough get going..', style={
        #'textAlign': 'center',
       # 'color': colors['text']
    
    #}),
    #表格數據
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
            
            
            
    #表格顏色佈局        
    #style_as_list_view=True,
    #style_cell={'padding': '5px'},
    #style_header={
        #'background':'#86473F',
        #'backgroundColor': '#787D7B',
        #'fontWeight': 'bold'},
    
    #設置為左對齊['年度', '服毒自殺']
    style_cell_conditional=[
        {
            'if': {'column_id': c},
            'textAlign': 'left'
        } for c in ['年度', '服毒自殺']
    ],
        data=df.to_dict("records"),
            
        ),
        ], fluid=True),
)


if __name__ == "__main__":
    app.run_server()
