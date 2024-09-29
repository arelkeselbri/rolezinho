import requests

# Define the coordinates of points A and B
point_a = (40.748817, -73.985428)  # New York (Empire State Building)
point_b = (48.858844, 2.294351)    # Paris (Eiffel Tower)

# Format the coordinates for the OSRM API (longitude,latitude)
coordinates = f"{point_a[1]},{point_a[0]};{point_b[1]},{point_b[0]}"

# OSRM API endpoint (change the profile to 'driving', 'cycling', or 'walking')
osrm_url = f"http://router.project-osrm.org/route/v1/driving/{coordinates}?overview=false"

# Send request to OSRM API
response = requests.get(osrm_url)

# Parse the response
if response.status_code == 200:
    data = response.json()
    # Extract the distance (in meters)
    distance_meters = data['routes'][0]['distance']
    distance_km = distance_meters / 1000  # Convert to kilometers
    print(f"The shortest driving distance from A to B is {distance_km:.2f} kilometers")
else:
    print("Error:", response.status_code)

