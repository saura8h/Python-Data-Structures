class Employee:

	raise_amount = 1.05

	def __init__(self, first, last, pay):
		self.first = first
		self.last  = last
		self.pay   = pay

	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	def email(self):
		'''
		Using self with a class variable will allow it to be overridden by 
		an instance variable. Using self will also allow any subclass to 
		override raise_amount if required. 
		'''
		return '{}.{}@company.com'.format(self.first, self.last)

	def apply_raise(self):
		return int(self.pay * self.raise_amount)

employee1 = Employee('Saurabh', 'Mishra', 120000)
employee2 = Employee('Test', 'User', 100000)

'''
Process of instance variables using class attribute 'raise_amount':

Class variables can be accessed through the class or an instance of the class.
When we try to access an attribute using an instance:
	The attribute will be checked for in the instance's namespace (by: employee1.__dict__) 
	If found, it will be returned. (It can be added in its namespace by: employee1.raise_amount = 1.08)
	If not, the class of the instance varialbe will be checked for the attribute (by: Employee.__dict__)
'''
print(Employee.raise_amount)	# class Employee has attribute 'raise_amount'
print(employee1.raise_amount)	# instance does not have the attribute, but the class it is inheriting from does, which will be used
print(employee1.__dict__)		# checking attributes contained in the employee1 namespace
print(Employee.__dict__)		# checking attributes contained in Employee namespace
employee1.raise_amount = 1.08	# assigning attribute 'raise_amount' to instance variable
print(employee1.raise_amount)	# instance variable has attribute raise_amount; this will override Employee's class variable raise_amount
print(employee2.raise_amount)	# instance variable will use the class variable present in Employee as it is an instance of it

# 9:00