#### Class Create
class Person:
    def __init__(self, id, name, phone):
        self.id = id
        self.name = name
        self.phone = phone
    
    def display(self):
        print(f"ID: {self.id} Name: {self.name} Phone: {self.phone}")