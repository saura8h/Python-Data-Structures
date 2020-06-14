class Restaurant:
    """
    Simple model for a restaurant.
    """

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe(self):
        """
        Give restaurant information.
        """
        print(f"The restaurant's name is {self.name} and it's speciality is {self.cuisine_type} food.")

    def is_open(self):
        """
        Indicate whether the restaurant is open or closed.
        """
        print('The restaurant is open!')


restaurant1 = Restaurant('Punjab Grill', 'Indian')

print(f'The restaurant {restaurant1.name} has very good food.')
print(f'{restaurant1.cuisine_type} food is very tasty!')
restaurant1.describe()
restaurant1.is_open()

print()

restaurant2 = Restaurant('Mainland China', 'Chinese')

print(f'The restaurant {restaurant2.name} also has very good food.')
print(f'{restaurant2.cuisine_type} food is also very tasty!')
restaurant2.describe()
restaurant2.is_open()

