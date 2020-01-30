from flask import Flask, render_template, request, send_from_directory
from werkzeug.utils import secure_filename
import os
app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = "./storage"

@app.route("/")
def beranda():
    return render_template("beranda.html")

#route upload file
@app.route("/upload", methods=["POST", "GET"])
def upload():
    if request.method == "POST":
        f = request.files["file"]
        print (f)
        fname = secure_filename(f.filename)
        f.save(os.path.join(app.config["UPLOAD_FOLDER"], fname))
        return render_template("success.html", img="http://127.0.0.1:5000/myfile/" + fname)

@app.route("/myfile/<path:path>")
def staticFile(path):
    return send_from_directory("storage", path)

if __name__ == "__main__":
    app.run(debug= True)