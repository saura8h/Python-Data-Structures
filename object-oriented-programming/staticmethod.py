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
        return int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
    
    @classmethod
    def parse_string(cls, employee_str):
        first, last, pay = employee_str.split('-')
        return cls(first, last, pay)
    
    @staticmethod
    def check_workday(day):
        '''
        Static methods don't pass anything automatically, i.e., neither 
        instance nor class. They behave just like regular functions. 
        We include them in class because they have some logical connection 
        with it.
        A method should be made static if we dont access the instance (self) 
        or the class (cls) variable anywhere within the funtion.
        '''
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

import datetime
date1 = datetime.date(2019, 10, 2)
date2 = datetime.date(2019, 10, 5)
print(Employee.check_workday(date1))    # 2nd October 2019 is a Wednesday
print(Employee.check_workday(date2))    # 5th October 2019 is a Saturday
