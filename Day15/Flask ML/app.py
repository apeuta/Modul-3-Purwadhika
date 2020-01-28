from flask import Flask
import joblib

app = Flask(__name__)

@app.route("/")
def home():
    return f"Prediksi 1, 1, 1, 1 = {model.predict([[1,1,1,1]])[0]}"

@app.route("/tes")
def tes():
    return f"Prediksi 2, 9, 9, 3 = {model.predict([[2,9,9,3]])[0]}"

if __name__ == "__main__":
    model = joblib.load("modelJoblib")
    app.run(debug= True, port= 2020)