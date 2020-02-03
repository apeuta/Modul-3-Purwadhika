from flask import Flask, render_template
import folium

app = Flask(__name__)

@app.route("/")
def home():
    peta = folium.Map(location= [-6.3024, 106.6522],zoom_start= 18)
    folium.Marker([-6.3024, 106.6522],tooltip= "Purwadhika BSD").add_to(peta)
    peta.add_child(folium.LatLngPopup())
    peta.save("templates/petaku.html")
    return render_template("index.html")

@app.route("/map")
def peta():
    return render_template("petaku.html")


if __name__ == "__main__":
    app.run(debug=True)