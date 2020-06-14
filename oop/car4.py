class Car:
    """
    Simple model for a car.
    """

    def __init__(self, make, model, year):
        """
        Initialize attributes to describe a car.
        These attributes are general and apply to all cars.
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
        Add the given amount of miles to the odometer reading.
        """
        self.odometer_reading += miles

    def engine(self):
        """
        Describe force required to move the car.
        """
        print('Gasoline engine is used to provide force to the car')


class ElectricCar(Car):
    """
    Represents aspects of a car that are specific to electric vehicles.
    """

    def __init__(self, make, model, year):
        """
        Initialize attributes of parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery_size = 75

    def describe_battery(self):
        """
        Show battery size.
        """
        print(f'This car has a battery capacity of {self.battery_size}-kWh')

    def engine(self):
        """
        Describe force required to move an electric car.

        This is polymorphism, in which method of the parent class is
        overridden by the child class.
        """
        print('An electric motor is used to provide force to move an eletric car')

my_tesla = ElectricCar('Tesla', 'Model S', 2019)
print(my_tesla.description())
my_tesla.describe_battery()
my_tesla.engine()

