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

	'''
	Decorator are used to alter the functionality of a method. 
	In this case, class is automatically passed as the first argument 
	NOT the instance. 'cls' is the common convention for class 
	argument. 
	'''
	@classmethod
	def set_raise_amount(cls, amount):
		cls.raise_amount = amount


employee1 = Employee('Saurabh', 'Mishra', 120000)
employee2 = Employee('Test', 'User', 100000)

print(Employee.raise_amount)
print(employee1.raise_amount)
print(employee2.raise_amount)

Employee.set_raise_amount(1.07)	# 
'''
Above is the same as Employee.raise_amount = 1.07

Another way to set class methods is by using instances:
	employee1.set_raise_amount(1.07)
	employee2.set_raise_amount(1.07)
This doesn't make much sence and is not used much IRL
'''

print(Employee.raise_amount)
print(employee1.raise_amount)
print(employee2.raise_amount)