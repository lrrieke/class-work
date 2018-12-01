class Restaurant():
    """Describe a restaurant's name and type of cuisine"""
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        print(self.restaurant_name.title() + ", " + self.cuisine_type.title())
        
    def open_restaurant(self):
        print(self.restaurant_name.title() + " is now open!")
        
    def read_number_served(self):
        print("Served: " + str(self.number_served) + ".")
        
    def set_number_served(self, customers):
        self.number_served = customers
        
    def increment_number_served(self, diners):
        self.number_served += diners