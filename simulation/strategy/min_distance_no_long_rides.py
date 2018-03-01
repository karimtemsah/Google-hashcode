class MinDistanceNoLongRides:

    def run(self, city):
        city.rides = sorted(city.rides, key=lambda ride: ride.duration)

        ninetieth_percentile = int(0.9 * len(city.rides))
        rides_short = city.rides[:ninetieth_percentile]
        rides_long = city.rides[ninetieth_percentile:]
        
        rides_short = sorted(rides_short, key=lambda ride: ride.earlieststart)
        rides_long = sorted(rides_long, key=lambda ride: ride.earlieststart)

        for ride in rides_short:

            min_distance = city.rows * 2
            car_id = city.cars
            for car in city.cars:
                distance_car_to_ride = abs(car.position[0] - ride.start[0]) + abs(car.position[1] - ride.start[1])
                if distance_car_to_ride < min_distance and car.simulation_step + distance_car_to_ride + ride.duration <= ride.latestend:
                    min_distance = distance_car_to_ride
                    car_id = car.id
            if car_id == city.cars:
                continue
            city.cars[car_id].rides.append(ride)
            city.cars[car_id].simulation_step = city.cars[car_id].simulation_step + ride.duration + min_distance
            city.cars[car_id].position = ride.end

        for ride in rides_long:

            min_distance = city.rows * 2
            car_id = city.cars
            for car in city.cars:
                distance_car_to_ride = abs(car.position[0] - ride.start[0]) + abs(car.position[1] - ride.start[1])
                if distance_car_to_ride < min_distance and car.simulation_step + distance_car_to_ride + ride.duration <= ride.latestend:
                    min_distance = distance_car_to_ride
                    car_id = car.id
            if car_id == city.cars:
                continue
            city.cars[car_id].rides.append(ride)
            city.cars[car_id].simulation_step = city.cars[car_id].simulation_step + ride.duration + min_distance
            city.cars[car_id].position = ride.end

        return city
