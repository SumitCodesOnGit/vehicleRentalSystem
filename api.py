from fastapi import FastAPI, HTTPException
"""FastAPI is the main class used to create API Application.
HTTPException is used to raise structured HTTP errors like 404,400, etc"""

from pydantic import BaseModel
"""from pydanticwe define data schemas for validating and passing incoming request data"""

from rental_service import RentalService
"""Importing RentalService class i.e business logic. It has all core components."""


# Create FASTAPI App
app = FastAPI()
"""creates an instance of the FastAPI class which we will use to define API routes
It's like a server that listens to HTTP requests and routes them to appropriate functions."""

# Initialize service layer
rentalService = RentalService()
"""allows us to use its method"""

# Define Request Model using Pydantic
class RentRequest(BaseModel):
    customer_id: int
    vehicle_id: int
    rental_days: int
""" This defines a schema for input data when someone wants to rent a vehicle.
BaseModel ensures automatic data validation: customer_id, vehicle_id, and rental_days must be all integers.
if a client sends incorrect data, FastAPI will automatically return a 422 error.
"""

# POST Endpoint: Rent Vehicle
"""This decorates the function below it as a POST endpoint.
When someone sends a POST request to /rent_vehicle, this fucntion will be called."""
@app.post("/rent_vehicle")
async def rent_vehicle(request: RentRequest):
    """This function is declared async.It takes a request object validated by RentRequest Pydantic model"""
    try:
        rentalService.rent_vehicle(
            request.customer_id,
            request.vehicle_id,
            request.rental_days
        )
        return {
            "status": "success",
            "message": "Vehicle rented successfully"
        }
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
    


# GET Endpoint: /available_vehicles
@app.get("/available_vehicles")
async def available_vehicles():
    available = [v. __dict__ for v in rentalService.vehicles if v.is_available]
    return {"vehicles": available}

 
    






