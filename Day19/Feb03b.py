from flask import Flask
import folium

app = Flask(__name__)

@app.route("/")
def home():
    peta = folium.Map(location= [-6.3024, 106.6522],zoom_start= 18)
    folium.Marker([-6.3024, 106.6522],tooltip= "Purwadhika BSD").add_to(peta)
    return peta._repr_html_()

if __name__ == "__main__":
    app.run(debug=True)