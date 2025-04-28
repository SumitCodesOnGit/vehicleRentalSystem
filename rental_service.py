from file_handlder import FileHandler
from payment import Payment 

class RentalService:


    def __init__(self):
        """load vehicles and customers from saved files (if any), else initialize empty list"""
        self.vehicles = FileHandler.load_data("vehicles.pkl") or []
        self.customers = FileHandler.load_data("customers.pkl") or []


    def add_vehicles(self,vehicle):
        """Add a new vehicle to a list"""
        self.vehicles.append(vehicle)
        self.save_data()


    def add_customer(self, customer):
        """Add a new customer to the list"""
        self.customers.append(customer)
        self.save_data()


    def display_available_vehicles(self):
        """Display all available vehicles"""
        print("\n Available Vehicles: ")
        available = False
        for vehicle in self.vehicles:
            if vehicle.is_available:
                print(vehicle)
                available = True
        if not available:
            print("No vehicles available at the moment")


    def rent_vehicle(self, customer_id, vehicle_id, rental_days):
        """Rent a vehicle to a customer after payment"""
        customer = self.find_customer(customer_id)
        vehicle = self.find_vehicle(vehicle_id)
        if customer and vehicle:
            if vehicle.is_available:
                total_rent = rental_days * vehicle.rent_per_day
                payment = Payment(total_rent)
                print(f"\n Total Rent: $ {total_rent}")
                method = input("Enter Payment Method (Cash/Card):").strip().lower()
                if method == "cash":
                    payment.pay_cash()
                elif method == "card":
                    card_number = input("Enter 16-digit Card Number: ")
                    payment.pay_card(card_number)
                else:
                    print("Invalid payment method")
                    return 
                vehicle.is_available = False
                print(f"\n {customer.name} rented {vehicle.brand} {vehicle.model} for {rental_days} days")
            else:
                print("\n Vehicle is not available")
        else:
            print("\n Invalid Customer ID or Vehicle ID")



    def return_vehicle(self, vehicle_id):
        """Mark a rented vehicle as returned"""
        vehicle = self.find_vehicle(vehicle_id)
        if vehicle and not vehicle.is_available:
            vehicle.is_available = True
            print(f"\n {vehicle.brand} {vehicle.model} has been returned successfully.")
            self.save_data()
        else:
            print("\n Invalid Vehicle ID or vehicle is already available.")


    def find_vehicle(self, vehicle_id):
        """Find and return a vehicle by its ID"""
        for vehicle in self.vehicles:
            if vehicle.vehicle_id == vehicle_id:
                return vehicle
        return None
    
    def find_customer(self, customer_id):
        """Find and return a customer by its ID"""
        for customer in self.customers:
            if customer.customer_id == customer_id:
                return customer
        return None
    

    def save_data(self):
        """Save the vehicles and customer list to the files"""
        FileHandler.save_data(self.vehicles,"vehicles.pkl")
        FileHandler.save_data(self.customers,"customers.pkl")


    

                



    
 




