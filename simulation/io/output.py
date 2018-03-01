def write(filename, city):
    with open(filename, 'w') as file:
        for car in city.cars:
            file.write(car.id)
            for ride in car.rides:
                file.write(ride.id)