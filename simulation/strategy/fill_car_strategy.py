class FillCarStrategy:

    def run(self, city):
        
        city.rides = sorted(city.rides, key=lambda ride: ride.earlieststart)

        for car in city.cars:
            while True:
                ride = car.get_nearest_best_ride(city.rides)

                if car.get_ride_end_time(ride) > city.steps:
                    break

                car.rides.append(ride)
                car.simulation_step += car.get_ride_end_time(ride)
                car.position = ride.end

                city.rides.remove(ride)

                if len(city.rides) == 0:
                    break
    
            if len(city.rides) == 0:
                break

        return city