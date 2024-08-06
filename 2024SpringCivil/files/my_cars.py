from car import Car
from electric_car import ElectricCar

my_beetle = Car("volkswagen", "my_beetle", 2020)
print(my_beetle.getDescriptiveName())

my_tesla = ElectricCar("tesla", "model s", 2020)
print(my_tesla.getDescriptiveName())
