class User():
    
    def __init__(self, first_name, last_name, location, age):
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.age = age
        self.login_attempts = 0
        
    def describe_user(self):
        print(self.first_name.title() + " " + self.last_name.title() + ", " + self.location.title() + ", " + str(self.age))
    
    def greet_user(self):
        print("Hello " + self.first_name.title() + " " + self.last_name.title() + "!")
        
    def read_login_attempts(self):
        print("Login attempts: " + str(self.login_attempts))
        
    def increment_login_attempts(self):
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        self.login_attempts = 0

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