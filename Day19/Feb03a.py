import folium

peta = folium.Map(
    location= [-6.3024, 106.6522],
    zoom_start= 18
)

folium.Marker(
    [-6.3024, 106.6522],
    tooltip= "Purwadhika BSD"
).add_to(peta)

peta.save("petapurwa.html")