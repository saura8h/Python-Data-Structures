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
        self.odometer_reading = 0    # default value for attribute

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

        Good practice to modify attribute in a class method, not using
        objects (outside class) like: my_new_car.odometer_reading = 23.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")


my_new_car = Car('Audi', 'A4', 2019)
print(my_new_car.description())
my_new_car.read_odometer()

my_new_car.update_odometer(23)
my_new_car.read_odometer()

