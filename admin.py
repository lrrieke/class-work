from user import User

class Admin(User):
    def __init__(self, first_name, last_name, location, age):
        super().__init__(first_name, last_name, location, age)
        self.privileges = Privileges() 

class Privileges():
    def __init__(self, privileges=[]):
        self.privileges = privileges
        
    def show_privileges(self):
        print("\nAdmin privileges: ")
        for privilege in self.privileges: 
        	print("- " + privilege)