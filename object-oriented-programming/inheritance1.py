class Employee:

    number_of_employees = 0
    raise_amount = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last  = last
        self.pay   = pay
        Employee.number_of_employees += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def email(self):
        return '{}.{}@company.com'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    

class Developer(Employee):
    '''
    It allows us to inherit attributes and methods from a parent class. 
    This lets us create subclasses having all the functionality of the 
    parent class, and override functionality to the subclas without 
    affecting the parent class.
    '''
    pass


developer1 = Employee('Saurabh', 'Mishra', 110000)
developer2 = Employee('Test', 'User', 100000)

'''
When the developer class gets instantiated, attributes (like init method) 
are checked in that class. If they are found, it is returned, and if not, 
the attributes are checked for in the upeer level of class inheritance in 
this case - Employee. 
'''
print(developer1.email())
print(developer2.email())

'''
This chain of walking up the inhertance ladder is called the method 
resolution order.
Object class is the parent class of all classes, i.e., all classes inherit 
from it.
'''
print(help(Developer))
