class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery:

    def __init__(self, battery_size=40):
        self.battery_size = battery_size
    
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kwh battery.")

    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range == 225
        print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        # self.battery_size = 40
        self.battery = Battery()
    
    # def describe_battery(self):
    #     print(f"This car has a {self.battery_size}-kwh battery.")

    def fill_gas_tank(self):
        print("This car doesn't have a gas tank!")

# my_new_car = Car('audi', 'a4', 2024)
# print(my_new_car.get_descriptive_name())
# my_new_car.odometer_reading = 23
# my_new_car.update_odometer(23)
# my_new_car.update_odometer(23_500)
# my_new_car.read_odometer()

# my_new_car.increment_odometer(100)
# my_new_car.read_odometer()
        