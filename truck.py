from vehicle import Vehicle

class Truck:

    def __init__(self,vehicle_id,brand,model,year,rent_per_day,max_load_capacity):
        super().__init__(vehicle_id,brand,model,year,rent_per_day)
        self.max_load_capacity = max_load_capacity
        

