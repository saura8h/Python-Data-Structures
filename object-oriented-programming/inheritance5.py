class Employee:

    raise_amount = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last  = last
        self.pay   = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def email(self):
        return '{}.{}@company.com'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


class Developer(Employee):
    
    raise_amount = 1.10

    def __init__(self, first, last, pay, programming_lang):
        super().__init__(first, last, pay)    
        self.programming_lang = programming_lang


class Manager(Employee):
    """
    Manager will pass in a list of employees under supervision
    """
    def __init__(self, first, last, pay, employees=None):
        # mutable data types should not be passed as default arguments
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)

    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)

    def display_employees(self):
        for employee in self.employees:
            print('-->', employee.fullname())


developer1 = Developer('Saurabh', 'Mishra', 120000, 'Python')
developer2 = Developer('Test', 'User', 100000, 'Java')

manager1 = Manager('Sue', 'Smith', 140000, [developer1])

# isInstance will tell us if an object is an instance of a class
print(isinstance(manager1, Manager))    # returns True
print(isinstance(manager1, Employee))   # returns True
print(isinstance(manager1, Developer))  # returns False

# isSubClass will tell us if a class is a subclass of another
print(issubclass(Manager, Employee))    # returns True
print(issubclass(Developer, Employee))  # returns True
print(issubclass(Developer, Manager))   # returns False
