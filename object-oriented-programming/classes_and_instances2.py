class Employee:

	def __init__(self, first, last, pay):
		''' 
		Initialize method is similar to a coinstructor.
		'self' is always the first argument received by all regular methods 
		in a class. This argument is named 'self' per general convention.
		The other arguments that we want to accept can be named appropriately.
		'''
		self.first = first	# setting instance variables automatically
		self.last  = last   # similar to instance_variable.class_name = value
		self.pay   = pay
		self.email = first + '.' + last + '@company.com'

'''
The below lines will run the init method automatically, where
employeeN will be passed as self, followed by setting class attributes
first, lay, and pay respectively
'''
employee1 = Employee('Saurabh', 'Mishra', 120000)
employee2 = Employee('Test', 'User', 100000)

print(employee1.email)
print(employee2.email)