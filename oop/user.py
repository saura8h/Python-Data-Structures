class User:
    """
    Model for a user.
    """

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name  = last_name
        self.email      = email

    def describe(self):
        """
        Provide user summary.
        """
        details = {
            'first_name': self.first_name,
            'last_name':  self.last_name,
            'email':      self.email
        }
        print(f"Below are the details:")
        print(details['first_name'], details['last_name'], details['email'])

    def greet(self):
        """
        Give a message to the user.
        """
        print(f'Hello {self.first_name}!')


user = User('Saurabh', 'Mishra', 'saurab.mish@gmail.com')
print(f'Hi, my name is {user.first_name}.')
user.greet()
user.describe()

