# Create your Contact class here

# Your Contact class should have THREE attributes: first_name, last_name, and phone_number
# These attributes must get their values from the constructor arguments (i.e. in your main.py in the code you're instructed not to modify, a first name, last name, and phone number are all passed IN THAT ORDER to each of the calls to the Contact() constructor)
# You should override the dunder methods for __eq__ (equality), __lt__ (less than), and __gt__ (greater than) so that your search will work!
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
