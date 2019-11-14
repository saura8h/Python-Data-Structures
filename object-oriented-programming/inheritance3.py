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


# Initiating subclass with more information than the parent class can handle
# eg: programming language
class Developer(Employee):
    
    raise_amount = 1.10

    def __init__(self, first, last, pay, programming_lang):
        # will let Employee handle first, last, and pay attributes
        super().__init__(first, last, pay)    
        # Above is the same as: Employee.__init__(self, first, last, pay)

        # additional attribute will be handled by Developer 
        self.programming_lang = programming_lang


developer1 = Developer('Saurabh', 'Mishra', 120000, 'Python')

print(developer1.email())
print(developer1.programming_lang)
