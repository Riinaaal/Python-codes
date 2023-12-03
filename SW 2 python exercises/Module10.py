# Assignment 1, 2 and 3
class Elevator:

    def __init__(self, bottom, top):
        self.bottom_floor = bottom
        self.top_floor = top
        self.location = bottom

    def go_to_floor(self, where_to):
        if self.location < where_to:
            while self.location != where_to:
                self.floor_up()

        else:
            while self.location != where_to:
                self.floor_down()
        return

    def floor_up(self):
        self.location = self.location + 1
        print(f"Elevator is on floor {self.location}")
        return

    def floor_down(self):
        self.location = self.location - 1
        print(f"Elevator is on floor {self.location}")
        return

class Building:
    def __init__(self, bottom, top, elevators):
        self.bottom_floor = bottom
        self.top_floor = top
        self.number_of_elevators = elevators
        self.elevators = []
        i = 0
        while i < elevators:
            elevator = Elevator(self.bottom_floor, self.top_floor)
            self.elevators.append(elevator)
            i = i + 1

    def run_elevator(self, elevator, destination):
        Elevator.go_to_floor(self.elevators[elevator], destination)

    def get_info(self):
        for x in self.elevators:
            print(x.location)

    def fire_alarm(self):
        for x in self.elevators:
            Elevator.go_to_floor(x, 1)


# Assignment 1 calls to class
h = Elevator(1, 7)
h.go_to_floor(5)

# Assignment 2 calls to class
building = Building(1, 8, 2)
building.run_elevator(1, 6)
building.run_elevator(0, 5)

# Assignment 3 fire alarm
building.fire_alarm()