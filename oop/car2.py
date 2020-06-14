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


my_used_car = Car('Subaru', 'Outback', 2014)
print(my_used_car.description())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()

