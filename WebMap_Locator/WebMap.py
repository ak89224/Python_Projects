import folium
import pandas


data=pandas.read_csv("Volcanoes.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
name=list(data["NAME"])
elev=list(data["ELEV"])

html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

def marker_colour(H):
    if H <= 1500:
        return "green"
    elif H <=2500:
        return "orange"
    else:
        return "red"


map=folium.Map(location=[lat[1],lon[1]],zoom_start=5,tiles='OpenStreetMap')

fgv=folium.FeatureGroup(name="Volcanoes")
for lt, ln, Name, Elev in zip(lat, lon, name, elev):
    iframe = folium.IFrame(html=html % (Name+" volcano", Name, Elev), width=200, height=100)
    fgv.add_child(folium.CircleMarker(location=[lt, ln],radius = 6, popup=folium.Popup(iframe), fill=True,
                                     fill_color = marker_colour(Elev), color='grey', fill_opacity=0.7))


fgp=folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open('world_beautify.json', 'r', encoding='utf-8-sig').read(),
                            style_function=lambda x: dict(fillColor='green' if x['properties']['POP2005'] < 10000000
                            else 'orange' if 10000000 <= x['properties']['POP2005'] <= 20000000 else 'red')))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("WebMap.html")