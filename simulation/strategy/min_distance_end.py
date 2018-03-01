import math

class MinDistanceEnd:

    def run(self, city):
        penalty = 2
        city.rides = sorted(city.rides, key=lambda ride: ride.earlieststart)

        for ride in city.rides:

            min_penalty_time = math.pow(city.steps, penalty)
            car_id = city.cars

            for car in city.cars:

                end_time = car.get_ride_end_time(ride)
                penalty_time = car.get_ride_end_time_with_penalty(ride, penalty)
                
                if penalty_time < min_penalty_time and end_time <= ride.latestend:
                    min_penalty_time = penalty_time
                    car_id = car.id

            if car_id == city.cars:
                continue

            city.cars[car_id].rides.append(ride)
            city.cars[car_id].simulation_step = city.cars[car_id].get_ride_end_time(ride)
            city.cars[car_id].position = ride.end

        return city
