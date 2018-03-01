class EarliestStartBestCarStrategy:

    def run(self, city):
        
        city.rides = sorted(city.rides, key=lambda ride: ride.earlieststart)

        for ride in city.rides:
            car = ride.get_nearest_best_car(city.cars)
            car.rides.append(ride)

            car.simulation_step += car.get_ride_end_time(ride)
            car.position = ride.end

        return city