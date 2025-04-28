class Customer:

    def __init__(self,customer_id,name,license_number,phone):
        self.customer_id = customer_id
        self.name = name
        self.license_number = license_number
        self.phone = phone


    def __str__(self):
        return f"{self.customer_id}: {self.name} - License: {self.license_number} - Phone: {self.phone}"
    
    


    

        

