# Module 9 assignment 1, 2, 3 & 4
import random
from beautifultable import BeautifulTable


class Car:

    # Define car object
    def __init__(self, reg_num, max_speed):
        self.reg_num = reg_num
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    # Info printout
    def info(self):
        return f'Registration number is {self.reg_num}, maximum speed is {self.max_speed} km/h, current speed is {self.current_speed} km/h, travelled distance is {self.travelled_distance} km'

    # Change car speeds
    def accelerate(self, new_speed):
        calculate = self.current_speed + new_speed
        if 0 < calculate <= self.max_speed:
            self.current_speed = calculate
        elif calculate < 0:
            self.current_speed = 0
        elif calculate > self.max_speed:
            self.current_speed = self.max_speed

    # Calculate distance based on current speed and travelled time in hours
    def drive(self, hours):
        add_distance = self.current_speed * hours
        self.travelled_distance = self.travelled_distance + add_distance


# Assignment 1 input and output
car = Car('ABC-123', 142)
print(car.info())

# Assignment 2 input and output
car.accelerate(+30)
car.accelerate(+70)
car.accelerate(+50)
print(car.current_speed)

car.accelerate(-200)
print(car.current_speed)

# Assignment 3 input and output
car.accelerate(+60)
car.drive(1.5)
print(car.travelled_distance)

# Assignment 4, creating list of 10 car objects
cars = []
i = 1
while i <= 10:
    register = "ABC-" + str(i)
    speed = random.randint(100, 200)
    name = Car(register, speed)
    cars.append(name)
    i = i + 1

# Making cars race
goal_reached = True
while goal_reached:
    for x in cars:
        # Increase/decrease current speed and add driven distance
        speed = random.randint(-10, 15)
        x.accelerate(speed)
        x.drive(1)

        # Check if cars traveled distance has reached the goal of 10 000km, if no it keeps going through cars
        # If distance reached exit loop
        if x.travelled_distance >= 10000:
            goal_reached = False


# Print out information about cars in table form.
table = BeautifulTable()
table.column_headers = ["Registration number", "maximum speed", "travelled distance"]
for x in cars:
    table.append_row([x.reg_num,  x.max_speed,  x.travelled_distance])

print(table)
