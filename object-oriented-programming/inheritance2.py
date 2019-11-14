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
    raise_amount = 1.10


developer1 = Employee('Saurabh', 'Mishra', 100000)
developer2 = Developer('Test', 'User', 100000)

print(developer1.pay)
developer1.apply_raise()
print(developer1.pay)

print(developer2.pay)
developer2.apply_raise()    # will override Employee's apply_raise attribute
print(developer2.pay)
