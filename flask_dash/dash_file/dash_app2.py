from dash import Dash, html,dash_table
import pandas as pd
import dash_bootstrap_components as dbc
from . import datasource
import pandas as pd

dash2 = Dash(requests_pathname_prefix="/dash/app2/",external_stylesheets=[dbc.themes.BOOTSTRAP])
dash2.title = "台北市youbike及時資料"
lastest_data = datasource.lastest_datetime_data()
lastest_df = pd.DataFrame(lastest_data,columns=['站點名稱','更新時間','行政區','地址','總數','可借','可還'])

dash2.layout = html.Div(
    [
        dbc.Container([
            html.Div([
                html.Div([
                    html.H1("台北市youbike及時資料")
                ],className="col text-center")
            ],
            className="row",
            style={"paddingTop":'2rem'}),
            html.Div([
                html.Div([
                    dash_table.DataTable(
                        data=lastest_df.to_dict('records'),
                        columns=[{'id':column,'name':column} for column in lastest_df.columns],
                        page_size=20
                    ),
                ],className="col text-center")
            ],
            className="row",
            style={"paddingTop":'2rem'}),
        ])
    ],
    className="container-lg"
    )