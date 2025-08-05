import requests
        
def getFlightData():
    flight_url = 'http://127.0.0.1:8000/flights'
    response = requests.get(flight_url)


getFlightData()