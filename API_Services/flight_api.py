from fastapi import FastAPI
import requests
from dataclasses import dataclass

@dataclass
class Location:
    longitude: float
    latitude: float
    
    def __post_init__(self):
        self.longitude_min = self.longitude - 0.25
        self.longitude_max = self.longitude + 0.25
        self.latitude_min = self.latitude - 0.25
        self.latitude_max = self.latitude + 0.25

opensky_url = 'https://opensky-network.org/api/states/all'
location_url = 'http://ip-api.com/json/'
app = FastAPI()

@app.get("/flights")
def get_flights():
    location = getLocationData()
    params = {
    'lamin': location.latitude_min,
    'lomin': location.longitude_min,
    'lamax': location.latitude_max,
    'lomax': location.longitude_max
    }
    response = requests.get(opensky_url, params)
    json_response = response.json()
    print(json_response)
    return json_response

def getLocationData():
    response = requests.get(location_url)
    data = response.json()
    location = Location(longitude=data["lon"], latitude=data["lat"])
    return location
