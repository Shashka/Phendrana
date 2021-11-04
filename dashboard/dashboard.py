import pandas as pd
import dash
import dash_html_components as html


df = pd.read_csv("C:\\Users\\rachid.meraoumia\\Desktop\\drift\\dashboard\\data\\arp_result.csv", index_col=0, parse_dates=False)

print(df)



app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Arp scan Report'),

    html.Div(children='''
        results below.
    '''),

    dash.dash_table.DataTable(
    id='port_scan',
    columns=[{"name": i, "id": i} for i in df.columns],
    data=df.to_dict('records'),
)

])

app.run_server(port=666)
