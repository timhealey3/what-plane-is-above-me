from fastapi import FastAPI

app = FastAPI()

@app.get("/flights")
def get_flights():
    print("retrieving flights")
