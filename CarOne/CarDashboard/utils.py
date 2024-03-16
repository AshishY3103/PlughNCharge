# import requests
# import googlemaps
# google_maps_api_key = 'AIzaSyDf8agE8Eb4oLKne49uZp7EK8OZ1XHxYt0'  # Replace with your actual API key


# def find_ev_stations(latitude, longitude, google_maps_api_key):
#   """
#   Finds EV charging stations near a given location.

#   Args:
#       latitude: The latitude of the search location.
#       longitude: The longitude of the search location.
#       google_maps_api_key: Your Google Maps API key.

#   Returns:
#       A list of dictionaries containing information about EV charging stations,
#       or an empty list if no stations are found.
#   """
#   url = "https://places.googleapis.com/v1/places:searchText"

#   payload = {
#       "textQuery": "ev charging stations",
#       "openNow": True,
#       "maxResultCount": 10,
#       "locationBias": {
#           "circle": {
#               "center": {
#                   "latitude": latitude,
#                   "longitude": longitude
#               },
#               "radius": 1000
#           }
#       }
#   }
#   headers = {
#       'Content-Type': 'application/json',
#       'X-Goog-Api-Key': google_maps_api_key,
#       'X-Goog-FieldMask': 'places.displayName,places.formattedAddress'
#   }

#   try:
#       response = requests.post(url, headers=headers, json=payload)
#       if response.status_code == 200:
#           data = response.json()
#           return data.get('places', [])
#       else:
#           print(f"Error: {response.status_code}")
#           return []
#   except Exception as e:
#       print(f"Error: {e}")
#       return []

# def get_lat_lng_from_address(address, google_maps_api_key):
#   """
#   Gets latitude and longitude from a given address.

#   Args:
#       address: The address to geocode.
#       google_maps_api_key: Your Google Maps API key.

#   Returns:
#       A tuple containing latitude and longitude, or None if not found.
#   """
#   url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={google_maps_api_key}"
#   try:
#       response = requests.get(url)
#       if response.status_code == 200:
#           data = response.json()
#           results = data.get('results', [])
#           if results:
#               location = results[0].get('geometry', {}).get('location')
#               if location:
#                   return location.get('lat'), location.get('lng')
#           print("No location found for the address.")
#           return None, None
#       else:
#           print(f"Error: {response.status_code}")
#           return None, None
#   except Exception as e:
#       print(f"Error: {e}")
#       return None, None

# def process_ev_station_info(station_info):
#   """
#   Processes EV station information to include location data.

#   Args:
#       station_info: A list of dictionaries containing EV station information.

#   Returns:
#       The modified list of dictionaries with location data added.
#   """
#   for station in station_info:
#       formatted_address = station.get('formattedAddress', '')
#       if formatted_address:
#           lat, lng = get_lat_lng_from_address(formatted_address, google_maps_api_key)
#           if lat is not None and lng is not None:
#               station['location'] = {'latitude': lat, 'longitude': lng}
#           else:
#               print(f"Could not find coordinates for address: {formatted_address}")
#   return station_info
