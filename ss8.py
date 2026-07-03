from fastapi import FastAPI
from pydantic import BaseModel,Field

app = FastAPI()

flights_db = [
    	{"id": 1, "flight_number": "VN-213", "destination": "Da Nang", "available_seats": 45, "status": "scheduled"},
    	{"id": 2, "flight_number": "VJ-122", "destination": "Phu Quoc", "available_seats": 12, "status": "scheduled"}
]

class them(BaseModel):
    flight_number : str
    destination : str
    available_seats : int



@app.get("/flights/{status}")
def get_flights_by_status(status: str):
    filtered_flights = [flight for flight in flights_db if flight["status"] == status]
    return filtered_flights

@app.post("/flights")
def add(c: them):
    id = len(flights_db) + 1
    new_flight = {
        "id": id,
        "flight_number": c.flight_number,
        "destination": c.destination,
        "available_seats": c.available_seats,
        "status": "scheduled"
    }
    flights_db.append(new_flight)
    return new_flight
    

@app.delete("/flights/{flight_id}")
def delete_flight(flight_id: int):
    flight = next((f for f in flights_db if f["id"] == flight_id), None)
    if not flight:
        return {"message": "Flight not found"}
    flights_db.remove(flight)
    return {"message": "Flight deleted successfully"}
