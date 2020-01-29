from flask import Flask, render_template, send_from_directory
import plotly
import plotly.graph_objects as go
import chart_studio.plotly as csp
import json

app = Flask(__name__)

@app.route("/")
def plot():
    plot = go.Scatter(
        x = [0,1,2,3,4,5,6,7,8,9],
        y = [9,8,7,7,5,4,5,7,7,9]
    )
    graphic = json.dumps([plot], cls=plotly.utils.PlotlyJSONEncoder)
    return render_template("plot.html", plot= graphic)

@app.route("/storage/<path:x>")
def storage(x):
    return send_from_directory("myfile", x)

if __name__ == "__main__":
    app.run(debug= True, port=2020)