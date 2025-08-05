import requests

flight_url = 'http://127.0.0.1:8000/flights'

def main():
    response = requests.get(flight_url)
    print(response.json())

main()