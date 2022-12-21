import dash
import dash_core_components as dcc
import dash_html_components as html
import os

workers = int(os.environ.get('GUNICORN_PROCESS', '3'))
threads = int(os.environ.get('GUNICORN_THREADS', '1'))

forwarded_allow_ips = '*'
secure_schema_headers = { 'X-Forwarded-Proto': 'https' }

app = dash.Dash()
application = app.server

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framwork for Python.
    '''),

    dcc.Graph(
        id='TACS PTT Reports',
        data : [go.Sankey(
                 # Define nodes                                  
                 node = dict(
                 pad = 15,
                 thickness = 15,
                 line = dict(color = "black", width = 0.5),
                 label = ["HOG Application","HOG Multiple","HOG Provincial","HOG ESIT",
                          "PTD Account","PTD Application",
                          "GIP Amount",
                          "tblACaseAll","tblAccount",
                          "Audit","Case","Registration","Return",
                          "tblBC_CseHOGRegular"],
                 color=  ["rgba(31, 119, 180, 0.8)","rgba(255, 127, 14, 0.8)","rgba(44, 160, 44, 0.8)","rgba(214, 39, 40, 0.8)",
                          "rgba(227, 119, 194, 0.8)","rgba(188, 189, 34, 0.8)",
                          "rgba(23, 190, 207, 0.8)",
                          "gray","gray","blue","blue","blue","blue","gray"]),
                 link = dict(source = [0,1,3,4,5,0,1,2,4,6,9,9,9,10,10,11,12,0,3],
                             target = [7,7,7,7,7,8,8,8,8,8,1,2,5,0,3,4,6,13,13],
                             value =  [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                             color =  ["rgba(31, 119, 180, 0.8)",
                                       "rgba(255, 127, 14, 0.8)",
                                       "rgba(214, 39, 40, 0.8)",
                                       "rgba(227, 119, 194, 0.8)",
                                       "rgba(188, 189, 34, 0.8)",
                                       "rgba(31, 119, 180, 0.8)",
                                       "rgba(255, 127, 14, 0.8)",
                                       "rgba(44, 160, 44, 0.8)",
                                       "rgba(227, 119, 194, 0.8)",
                                       "rgba(23, 190, 207, 0.8)",
                                       "rgba(255, 127, 14, 0.8)",
                                       "rgba(44, 160, 44, 0.8)",
                                       "rgba(188, 189, 34, 0.8)",
                                       "rgba(31, 119, 180, 0.8)",
                                       "rgba(214, 39, 40, 0.8)",
                                       "rgba(227, 119, 194, 0.8)",
                                       "rgba(23, 190, 207, 0.8)",
                                       "rgba(31, 119, 180, 0.8)",
                                       "rgba(214, 39, 40, 0.8)"
                  ]))])
app.css.append_css({"external_url:"https://codepen.io/chriddyp/pen/bWLwgP.css"})


if __name__ == '__main__':
    app.run_server(port=8080,host='0.0.0.0',degub=True)