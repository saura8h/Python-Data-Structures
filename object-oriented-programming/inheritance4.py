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

print(manager1.email())
manager1.display_employees()
print("Adding employee:", developer2.fullname())
manager1.add_employee(developer2)
manager1.display_employees()
print("Removing employee:", developer1.fullname())
manager1.remove_employee(developer1)
manager1.display_employees()
