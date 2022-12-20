from flask import Flask
from datetime import datetime
import os
import plotly.graph_objects as go

app = Flask(__name__)

@app.route('/')

def hello():
    fig = go.Figura(data = [go.Sankey(
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
    fig.update_layout(title_text="TACS Category to Report to Table Diagram Flow", font_size=10)
    fig.show()
    return fig.show()

if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')
