class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, programming_lang):
        super().__init__(first, last, pay)
        self.programming_lang = programming_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
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


developer1 = Developer('Corey', 'Schafer', 50000, 'Python')
developer2 = Developer('Test', 'Employee', 60000, 'Java')

manager1 = Manager('Sue', 'Smith', 90000, [developer1])

print(manager1.email)

manager1.add_employee(developer2)
# manager1.remove_employee(developer2)

manager1.display_employees()
