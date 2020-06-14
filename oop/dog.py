class Dog:
    """
    A simple attempt to model a dog.
    """

    def __init__(self, name, age):
        """
        Initialize name and age attributes.

        This method will be called when an instance of this class is created.
        When this method is called, it will pass the self (first) argument.
        Keyword self is a reference to a class instance, and gives the
        individual instance access to attributes and methods in the class.

        Attributes in the init method will have self prefixed to its name.
        This will make it available to every method in the class, and they
        can also be accessed using an instance of the class.

        For a method to be associated with a class instance it has to contain
        the self keyword.
        """
        self.name = name
        self.age  = age

    def sit(self):
        """
        Simulate sitting in response to a command.
        """
        print(f'{self.name} is now sitting.')

    def roll_over(self):
        """
        Simulate rolling over in response to a command.
        """
        print(f'{self.name} rolled over!')


my_dog = Dog('Willie', 6)    # instance of class
my_dog.sit()
my_dog.roll_over()

print(f"My dog's name is {my_dog.name}.")
print(f'My dog is {my_dog.age} years old.')

print()

your_dog = Dog('Lucy', 5)    # another instance of class
your_dog.sit()
your_dog.roll_over()

print(f"Your dog's name is {your_dog.name}.")
print(f'Your dog is {your_dog.age} years old.')

