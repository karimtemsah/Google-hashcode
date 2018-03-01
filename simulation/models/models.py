import math

class Ride:
    def __init__(self, id, startrow, startcolumn, endrow, endcolumn, earlieststart, latestend):
        self.id = id
        self.latestend = latestend
        self.earlieststart = earlieststart
        self.start = [startrow, startcolumn]
        self.end = [endrow, endcolumn]
        self.duration = abs(startrow - endrow) + abs(startcolumn - endcolumn)

    def get_nearest_best_car(self, cars):
        best_car = None

        for car in cars:
            if best_car == None:
                best_car = car
                continue

            if car.get_ride_end_time(self) < best_car.get_ride_end_time(self) and \
                    car.get_ride_end_time(self) <= self.latestend:
                best_car = car

        return best_car    


class Car:
    def __init__(self, id):
        self.id = id
        self.rides = []
        self.position = [0, 0]
        self.simulation_step = 0

    def get_distance(self, ride):
        return abs(self.position[0] - ride.start[0]) + abs(self.position[1] - ride.start[1])

    def get_ride_start_time(self, ride):
        return max(self.simulation_step + self.get_distance(ride), ride.earlieststart)
    
    def get_ride_end_time(self, ride):
        return self.get_ride_start_time(ride) + ride.duration

    def get_ride_end_time_with_penalty(self, ride, penalty):
        return self.get_ride_start_time(ride) + math.pow(ride.duration, penalty)

    def get_nearest_best_ride(self, rides):
        best_ride = None

        rides = sorted(rides, key=lambda ride: ride.earlieststart)
        for ride in rides:
            # First loop
            if best_ride == None:
                best_ride = ride
                continue
        
            # Other loops
            if self.get_ride_end_time(ride) < self.get_ride_end_time(best_ride) and \
                    self.get_ride_end_time(ride) <= ride.latestend:
                best_ride = ride

        return best_ride


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
