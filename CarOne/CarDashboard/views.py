from django.shortcuts import render
from django.http import HttpResponse
# from .utils import find_ev_stations, process_ev_station_info  # Import your helper functions
import http.client
import json,urllib
from ev_server.models import *
import random

origin_lat = 19.095487
origin_lng = 72.895940 

def user_login(request):
    return render(request,'login.html')

def find_ev_stations_view(request):
    conn = http.client.HTTPSConnection("places.googleapis.com")
    payload = json.dumps({
        "textQuery": "ev charging stations",
        "openNow": True,
        "maxResultCount": 10,
        "locationBias": {
            "circle": {
                "center": {
                    "latitude": origin_lat,
                    "longitude": origin_lng
                },
                "radius": 1000
            }
        }
    })
    headers = {
        'Content-Type': 'application/json',
        'X-Goog-Api-Key': 'AIzaSyDf8agE8Eb4oLKne49uZp7EK8OZ1XHxYt0',  # Replace 'YOUR_API_KEY' with your actual API key
        'X-Goog-FieldMask': 'places.displayName,places.formattedAddress'
    }

    conn.request("POST", "/v1/places:searchText", payload, headers)
    res = conn.getresponse()
    data = res.read().decode("utf-8")
    response_json = json.loads(data)
    # print(response_json)

    if 'candidates' in response_json and len(response_json['candidates']) > 0:
        for candidate in response_json['candidates']:
            if 'geometry' in candidate and 'location' in candidate['geometry']:
                latitude = candidate['geometry']['location']['latitude']
                longitude = candidate['geometry']['location']['longitude']
                print("Latitude:", latitude)
                print("Longitude:", longitude)
    else:
        print("No EV charging stations found.")




    # Function to get coordinates from a formatted address using Google Maps Geocoding API
    
    global coordinates_array
    coordinates_array = []
    global names
    names=[]


    for fa in response_json['places']:
        lat, lng = get_coordinates(fa['formattedAddress'])
        names.append(fa['displayName']['text'])
        if lat is not None and lng is not None:
            coordinates_array.append((lat, lng))



    # print("Coordinates of the addresses:")
    # for coordinates in coordinates_array:
    #     print(coordinates)

    # baseCoordinate = { lat: latitude, lng: longitude }
    global distances
    distances=get_and_print_distances(coordinates_array,origin_lat,origin_lng)
    # print(distance)
    # 'baseCoordinate':baseCoordinate

    return render(request, 'index.html', {'coordinates_array': coordinates_array,'names':names})





def get_coordinates(address):
        conn = http.client.HTTPSConnection("maps.googleapis.com")
        params = {
            'address': address,
            'key': 'AIzaSyDf8agE8Eb4oLKne49uZp7EK8OZ1XHxYt0'  # Replace 'YOUR_GOOGLE_MAPS_API_KEY' with your actual API key
        }
        conn.request("GET", "/maps/api/geocode/json?" + urllib.parse.urlencode(params))
        res = conn.getresponse()
        data = res.read().decode("utf-8")
        response_json = json.loads(data)
        if response_json['status'] == 'OK':
            location = response_json['results'][0]['geometry']['location']
            return location['lat'], location['lng']
        else:
            # print("Error:", response_json['status'])
            return None, None
        




def get_and_print_distances(destinations, origin_lat, origin_lng):
    api_key = 'AIzaSyDf8agE8Eb4oLKne49uZp7EK8OZ1XHxYt0'  # Replace 'YOUR_API_KEY' with your actual API key
    origin = f"{origin_lat},{origin_lng}"
    destinations_string = "|".join([f"{lat},{lng}" for lat, lng in destinations])

    url = f"https://maps.googleapis.com/maps/api/distancematrix/json?origins={origin}&destinations={destinations_string}&travelMode=driving&key={api_key}"

    try:
        conn = http.client.HTTPSConnection("maps.googleapis.com")
        conn.request("GET", url)
        response = conn.getresponse()
        data = response.read().decode("utf-8")
        distance_matrix = json.loads(data)

        distances = []
        if distance_matrix["status"] == "OK":
            for i, element in enumerate(distance_matrix["rows"][0]["elements"]):
                if "distance" in element:
                    distances.append(element["distance"]["text"])
                else:
                    distances.append("N/A")  # Distance not available
        else:
            # print(f"Error: Google Maps API returned status {distance_matrix['status']}")
            distances = ["N/A"] * len(destinations)

        return distances
    except Exception as e:
        # print(f"Error: {e}")
        return ["N/A"] * len(destinations)
    finally:
        conn.close()




def display_connectors(request):
    # Retrieve all connectors from the database
    connectors = Connector.objects.all()

    # Get connectors of the same type
    user_charger_type = 'Type 1'  # Example charger type, replace with actual user input
    same_type_connectors = get_same_type_connectors(user_charger_type)

    # Sort connectors by current status and distance
    user_location = (origin_lat,origin_lng)  # Define user location coordinates
    sorted_connectors = sort_connectors_by_status_and_distance(same_type_connectors, user_location)

    # Pass the connectors and sorted_connectors variables to the template
    context = {
        'connectors': same_type_connectors,
        'sorted_connectors': sorted_connectors,
    }

    # Render the template with the provided context
    return render(request, 'TableSorted.html', context)

def get_same_type_connectors(user_charger_type):
    # Retrieve connectors whose charger type matches the user's charger type
    connectors = Connector.objects.filter(connector_type__name=user_charger_type)
    
    return connectors

def sort_connectors_by_status_and_distance(connectors,user_location):
    # Create dictionaries to store connectors based on status
    available_connectors = []
    occupied_connectors = []
    maintenance_connectors = []

    # Categorize connectors based on status
    for connector in connectors:
        if connector.current_status == 'Available':
            available_connectors.append(connector)
        elif connector.current_status == 'Occupied':
            occupied_connectors.append(connector)
        elif connector.current_status == 'Under Management':
            maintenance_connectors.append(connector)

    # Sort connectors within each status category by distance
    available_connectors.sort(key=lambda connector: connector.charging_station.distance if connector.charging_station.distance is not None else float('inf'))
    occupied_connectors.sort(key=lambda connector: connector.charging_station.distance if connector.charging_station.distance is not None else float('inf'))
    maintenance_connectors.sort(key=lambda connector: connector.charging_station.distance if connector.charging_station.distance is not None else float('inf'))
    sorted_connectors = available_connectors + occupied_connectors + maintenance_connectors

    
    return sorted_connectors

dummy_names= []
def get_connectors(request):
    for i in range(0,len(names)):
        dummy_names.append(names[i])
    insert_data(dummy_names,coordinates_array,distances)
    connectors = Connector.objects.all()
    
    # print(dummy_names)
    same_type_connetors = get_same_type_connectors('Type 2')
    sorted_connecters = sort_connectors_by_status_and_distance(same_type_connetors,(19.089980,73.676327))
    
    context = {
        'connectors': connectors,
        'same_type_connetors' : same_type_connetors,
        'sorted_connecters' : sorted_connecters,
    }

    return render(request, 'TableSorted.html',context)

def insert_data(names,coordinates_array,distances):
    delete_all_records()
    for i in range(len(distances)):
        # Split the string by space to separate the value and unit
        value, unit = distances[i].split(" ")

        # Convert the value to a float and remove "km" from it
        value_without_unit = float(value)

        # Update the distances array with the processed value
        distances[i] = value_without_unit

    latitudes = []
    longitudes = []
    for lat , lng in coordinates_array:
        latitudes.append(lat) 
        longitudes.append(lng)

    for name,latitude,longitude,distance in zip(names, latitudes, longitudes, distances):
        # Added
        station = ChargingStation.objects.create(
                name=name,
                latitude=latitude,
                longitude=longitude,
                pricing=10,
                balance= (random.randint(5,10))*10,
                distance=distance
            )

            # Add connectors
        connector_types = ConnectorType.objects.all()
        for _ in range(2):  # Add 2 connectors for each station
            connector_type = random.choice(connector_types) # Example range for max charging power
            current_status = random.choice(['Available', 'Occupied', 'Under Management'])
            Connector.objects.create(
                charging_station=station,
                connector_type=connector_type,
                current_status=current_status
            )

def delete_all_records():
    # Delete all records from the table
    ChargingStation.objects.all().delete()
    Connector.objects.all().delete()
