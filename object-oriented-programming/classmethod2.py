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
		'''
		Using class methods as alternative constructors, i.e., class methods can 
		be used to provide multiple ways of creating objects
		eg: parsing string before creating new employees (data received may be - separated)
		'''
		first, last, pay = employee_str.split('-')
		return cls(first, last, pay)

employee_str1 = "John-Doe-70000"
employee_str2 = "Steve-Smith-80000"

new_employee1 = Employee.parse_string(employee_str1)
new_employee2 = Employee.parse_string(employee_str2)

print(new_employee2.first)
print(new_employee2.last)
print(new_employee2.email())
print(new_employee2.pay)
