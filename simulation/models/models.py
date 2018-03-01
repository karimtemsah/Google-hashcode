class Ride:
    def __init__(self, id, startrow, startcolumn, endrow, endcolumn, earlieststart, latestend):
        self.id = id
        self.latestend = latestend
        self.earlieststart = earlieststart
        self.start = [startrow, startcolumn]
        self.end = [endrow, endcolumn]
        self.duration = abs(startrow - endrow) + abs(startcolumn - endcolumn)


class Car:
    def __init__(self, id):
        self.id = id
        self.rides = []
        self.position = [0, 0]


class City:
    def __init__(self, rows, columns, fleet_size, amount_rides, bonus, steps):
        self.rows = rows
        self.columns = columns
        self.fleet_size = fleet_size
        self.amount_rides = amount_rides
        self.bonus = bonus
        self.steps = steps
        self.cars = [Car(i) for i in range(fleet_size)]
        self.rides = []
