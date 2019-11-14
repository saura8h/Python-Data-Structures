class Employee:

	number_of_employees = 0
	raise_amount = 1.05

	def __init__(self, first, last, pay):
		self.first = first
		self.last  = last
		self.pay   = pay
		'''
		Better than using self because there is no reason to have 
		different number of employees for different instances. 
		It will also prevent instances from overriding this attribute, and 
		there will be a constant class value.
		'''
		Employee.number_of_employees += 1

	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	def email(self):
		return '{}.{}@company.com'.format(self.first, self.last)

	def apply_raise(self):
		return int(self.pay * self.raise_amount)

print(Employee.number_of_employees)

employee1 = Employee('Saurabh', 'Mishra', 120000)
employee2 = Employee('Test', 'User', 100000)

print(Employee.number_of_employees)
