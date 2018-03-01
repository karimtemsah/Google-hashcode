class Ride:
    def __init__(self, duration, startrow, startcolumn, endrow, endcolumn, earlieststart, latestend):
        self.latestend = latestend
        self.earlieststart = earlieststart
        self.start = [startrow, startcolumn]
        self.end = [endrow, endcolumn]
        self.duration = duration


class Car:
    def __init__(self, id):
        self.id = id
        self.rides = []


class City:
    def __index__(self, rows, columns, fleet_size, amount_rides, bonus, steps):
        self.rows = rows
        self.columns = columns
        self.fleet_size = fleet_size
        self.amount_rides = amount_rides
        self.bonus = bonus
        self.steps = steps
        self.cars = [Car(i) for i in range(fleet_size)]
