from vehicle import Vehicle

class Car:

    def __init__(self, vehicle_id, brand, model, year, rent_per_day, num_doors):
        super().__init__(vehicle_id,brand,model,year,rent_per_day)
        self.num_doors = num_doors
        

