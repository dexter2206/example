class Employee(object):
    """A class representing employee."""
    
    def __init__(self, name, surname, salary):
        self.name = name
        self.surname = surname
        self.salary = salary
        
    @property
    def full_name(self):
        return self.name + ' ' + self.surname
    
    def calculate_payment(self, hours, bonus):
        """Calculate payment for the employee based on hours worked."""
        return self.salary * hours + bonus
