class Employee:

	'''
    Class variables are shared among and same for all class instances.
	Data which is shared among all employees; good idea for a class variable. 
    '''
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
		'''
		Class variables can only be accessed through the class itself or 
		an instance of the class.
		'''
		return int(self.pay * self.raise_amount)	# access through instance
		# return int(self.pay * Employee.raise_amount)	# access through class


employee1 = Employee('Saurabh', 'Mishra', 120000)
employee2 = Employee('Test', 'User', 100000)

print(employee1.pay)
print(employee1.apply_raise())
