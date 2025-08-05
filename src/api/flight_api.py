
from src.api.dataclasses.location import Location
from src.api.dataclasses.plane import Plane
from dataclasses import asdict
from fastapi import FastAPI
import requests
import json

opensky_url = 'https://opensky-network.org/api'
state_path = '/states/all'
aircraft_path = '/metadata/aircraft/icao'
location_url = 'http://ip-api.com/json/'
app = FastAPI()

@app.get("/flights")
def get_flights():
    planes = []
    location = getLocationData()
    location_params = setLocationParams(location)
    flights_response = requests.get(opensky_url + state_path, location_params)
    flights_json = flights_response.json()
    for message in flights_json['states']:
        icao24 = message[0]
        response = requests.get(opensky_url + aircraft_path + f'/{icao24}')
        json_response = response.json()
        plane = Plane(tailNumber=json_response["registration"], make=json_response["manufacturerName"], model=json_response["model"], owner=json_response["owner"])
        planes.append(plane)
    return [asdict(p) for p in planes]

def getLocationData():
    response = requests.get(location_url)
    data = response.json()
    location = Location(longitude=data["lon"], latitude=data["lat"])
    return location

def setLocationParams(location):
    return {
    'lamin': location.latitude_min,
    'lomin': location.longitude_min,
    'lamax': location.latitude_max,
    'lomax': location.longitude_max
    }