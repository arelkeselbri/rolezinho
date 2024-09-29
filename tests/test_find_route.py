

import folium
import requests
import polyline  # Import the polyline decoding library

# Define the coordinates of points A and B
point_a = (-18.917993526793765, -48.282102996879104) # Point do Mercado
point_b = (-18.925101699372778, -48.2912319064304) # Cerv. Benedith

# OSRM URL for route calculation
coordinates = f"{point_a[1]},{point_a[0]};{point_b[1]},{point_b[0]}"
osrm_url = f"http://router.project-osrm.org/route/v1/driving/{coordinates}?overview=full"

# Get the route from OSRM
response = requests.get(osrm_url)
data = response.json()

# Extract the route's geometry (the polyline of the route)
route_geometry = data['routes'][0]['geometry']

# Create a map centered between the two points
map_center = [(point_a[0] + point_b[0]) / 2, (point_a[1] + point_b[1]) / 2]
m = folium.Map(location=map_center, zoom_start=12)

# Add markers for points A and B
folium.Marker(location=point_a, popup="Point A: Point do Mercado").add_to(m)
folium.Marker(location=point_b, popup="Point B: Cerv. Benedith").add_to(m)

# Decode the polyline using the `polyline` package
decoded_route = polyline.decode(route_geometry)

# Plot the route on the map
folium.PolyLine(locations=decoded_route, color="blue", weight=2.5).add_to(m)

# Save the map as an HTML file
m.save("route_map.html")


