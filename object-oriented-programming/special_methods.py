'''
Special methods are also called magic methods. They allow built-in behavior 
to be emulated, and operators to be overloaded. These methods have trailing 
and leading double underscores (dunder).
eg: init, repr, str
'''

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def email(self):
        return '{}.{}@company.com'.format(self.first, self.last)

    def __repr__(self):
        '''
        Used for unambiguous object representation, in debuging and logging.
        This method will be used as a fallback if __str__ is not present.
        '''
        return "Employee('{}', '{}')".format(self.first, self.last)

    def __str__(self):
        '''
        Used for readable representation of an object, which is ideally
        displayed to the end-user.
        This method has a higher priority than repr, and will be executed
        first when an object is called in case both dunders are present.
        '''
        return '{} - {}'.format(self.fullname(), self.email())


employee1 = Employee('Saurabh', 'Mishra')
print(employee1)    # preference: default > str > repr

print(repr(employee1))  # same as: print(employee1.__repr__())
print(str(employee1))   # same as: print(employee1.__str__())

print(int.__add__(1, 2))        # print(1+2)
print(str.__add__('a', 'b'))    # print('a' + 'b')

# 7:00      __add__
# 10:45     __len__
