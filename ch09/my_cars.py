# from car import Car,ElectricCar
# import car
# from car import *

# from car import Car
# from electric_car import ElectricCar

from car import Car
from electric_car import ElectricCar as EC

my_mustang = Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())

my_leaf = EC('nissa','leaf', 2024)
print(my_leaf.get_descriptive_name())

# my_mustang = car.Car('ford', 'mustang', 2024)
# print(my_mustang.get_descriptive_name())

# my_leaf = car.ElectricCar('nissa','leaf', 2024)
# print(my_leaf.get_descriptive_name())