class EarliestStartNoLongRidesStrategy:

    def run(self, city):

        # Remove all totally long rides
        city.rides = sorted(city.rides, key=lambda ride: ride.duration)

        # 0.78 - 5.303.569 points
        # 0.76 - 5.345.358 points
        # 0.75 - 5.371.796 points
        # 0.74 - 5.382.173 points
        # 0.73 - 5.318.844 points
        # 0.7  - 5.193.304 points
        # 0.6  - 4.299.974 points

        ninetieth_percentile = int(0.74 * len(city.rides))
        rides_short = city.rides[:ninetieth_percentile]
        rides_long = city.rides[ninetieth_percentile:]
        
        rides_short = sorted(rides_short, key=lambda ride: ride.earlieststart)
        rides_long = sorted(rides_long, key=lambda ride: ride.earlieststart)
        next_car = 0

        for ride in rides_short:
            city.cars[next_car].rides.append(ride)
            next_car = (next_car + 1) % city.fleet_size

        for ride in rides_long:
            city.cars[next_car].rides.append(ride)
            next_car = (next_car + 1) % city.fleet_size

        return city