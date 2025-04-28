from vehicle import Vehicle

class Bike:

    def __init__(self, vehicle_id, brand, model, year, rent_per_day, bike_type):
        super().__init__(vehicle_id,brand,model,year,rent_per_day)
        self.bike_type = bike_type
        

