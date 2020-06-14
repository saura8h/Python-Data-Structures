class Car:
    """
    Simple model for a car.
    """

    def __init__(self, make, model, year):
        """
        Initialize attributes to describe a car.
        """
        self.make  = make
        self.model = model
        self.year  = year
        self.odometer_reading = 0

    def description(self):
        """
        Return a neatly formatted descriptive name.
        """
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name.title()

    def read_odometer(self):
        """
        Show the car's mileage.
        """
        print(f'This car has {self.odometer_reading} miles on it.')

    def update_odometer(self, mileage):
        """
        Modify default attribute of odometer.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """
        Add he given amount of miles to the odometer reading.
        """
        self.odometer_reading += miles


class ElectricCar(Car):
    """
    Represents aspects of a car that are specific to electric vehicles.

    Child class definition should contain the name of the parent class.
    """

    def __init__(self, make, model, year):
        """
        Initialize attributes of parent class.

        The super() function is used to call a method in the parent class
        (from the child class)
        """
        super().__init__(make, model, year)


"""
Apart from __init__(), there are no attributes or methods that are particular
to an electric car.
The electric car has attributes make, model, year, and odometer_reading from
the parent Car class.
"""
my_tesla = ElectricCar('Tesla', 'Model S', 2019)
print(my_tesla.description())

