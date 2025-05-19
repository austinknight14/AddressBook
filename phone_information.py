class Contact():    
    def __init__ (self, first_name, last_name, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
    def __str__(self):
        return f"{self.first_name}{self.last_name}{self.phone_number}"
    def __lt__(self, other):
        return self.first_name < other.first_name
    def __gt__(self, other):
        return self.first_name > other.first_name
    def __eq__(self, other):
        return (self.first_name == other.first_name and 
                self.last_name == other.last_name)
