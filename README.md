## What plane is above me?
Ever ask yourself this question? I do, at least once a day. Fear not—the days of checking the radar app are over! This API will automatically display what planes are above you at any given moment.

## How to use it
Currently, this can only be used locally. You can run it with [uvicorn](https://www.uvicorn.org/):

```bash
uvicorn API_Services.flight_api:app --reload
```

## How to call the app locally
Make a GET request to `http://localhost:8000/flights`. It will return all planes currently around you within a 0.25 longitude/latitude radius. The response will be a JSON array in the format:

```json
[
  {
    "tailNumber": "N12345",
    "make": "Boeing",
    "model": "737",
    "owner": "Delta Airlines"
  }
]
```