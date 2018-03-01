class EarliestStartStrategy:

    def run(self, city):
        
        city.rides = sorted(city.rides, key=lambda ride: ride.earlieststart)
        next_car = 0

        for ride in city.rides:
            city.cars[next_car].rides.append(ride)
            next_car = (next_car + 1) % city.fleet_size

        return city