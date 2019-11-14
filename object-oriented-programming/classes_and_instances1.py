class Employee:
	pass

employee1 = Employee()    # unique instance of class Employee
employee2 = Employee()    # both will have different memory locations


# Instance variables contain data unique to each instance
employee1.first  = 'Saurabh'
employee1.last   = 'Mishra'
employee1.email  = 'saurabh.mishra@company.com'
employee1.pay    = 120000

employee2.first  = 'Test'
employee2.last   = 'User'
employee2.email  = 'test.user@company.com'
employee2.pay    = 100000

print(employee1.email)
print(employee2.email)

print('{} {}'.format(employee1.first, employee1.last))	# using placehoders for values

'''
Manually creating an instance variable in case of each employee will have 
a lot of code and possibly mistakes as well
'''
