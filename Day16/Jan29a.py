from flask import Flask, render_template, request
import joblib
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/predict", methods= ["POST", "GET"])
def predict():
    if request.method == "POST":
        input = request.form
        prediksi = model.predict(
            [[float(input["SL"]), float(input["SW"]), float(input["PL"]), float(input["PW"])]]
        )
        return render_template("predict.html", data= input, pred= prediksi)

if __name__ == "__main__":
    model = joblib.load("modelJoblib")
    app.run(debug= True)