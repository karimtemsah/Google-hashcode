class ClosestRideNextStrategy:

    def run(self, city):
        city.rides = sorted(city.rides, key=lambda ride: ride.start)
        next_car = 0

        for ride in city.rides:

            distance_car_to_ride = abs(city.cars[next_car].position[0] - ride.start[0]) + abs(city.cars[next_car].position[1] - ride.start[1])

            if city.cars[next_car].simulation_step <= ride.latestend-ride.duration and ride.earlieststart > city.cars[next_car].simulation_step + distance_car_to_ride:
                city.cars[next_car].rides.append(ride)
                city.cars[next_car].simulation_step = city.cars[next_car].simulation_step + ride.duration + distance_car_to_ride
                city.cars[next_car].position = ride.end
                next_car = (next_car + 1) % city.fleet_size

        return city
