from dash import Dash, html, dcc
import os

app = Dash(__name__)

app.layout = html.Div([
    dcc.dropdown(['New York City','Vancouver','Victoria','Calgary','Montreal'],'Victoria')
])

if __name__ == '__main__':
    app.run_server(port=8080,host='0.0.0.0',degub=True)
