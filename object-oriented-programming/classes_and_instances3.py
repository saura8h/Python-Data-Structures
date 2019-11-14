class Employee:

	def __init__(self, first, last, pay):
		self.first = first
		self.last  = last
		self.pay   = pay

	# Performing actions
	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	def email(self):
		return '{}.{}@company.com'.format(self.first, self.last)


employee1 = Employee('Saurabh', 'Mishra', 120000)

'''
When a class instance is used to call a (class) method, self doesn't have
to be passed, as this is done automically
'''
print(employee1.fullname())
print(employee1.email())

'''
When a class is used directly to call its method, the class doesn;t know
what instance to run that method with. So we have to pass an instance; 
employee1 or employee2 (which gets passed in as self)
'''
print(Employee.fullname(employee1))
print(Employee.email(employee1))
