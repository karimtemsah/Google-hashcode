def write(filename, city):
    with open(filename, 'w') as file:
        for car in city.cars:
            file.write('{}'.format(car.id))
            for ride in car.rides:
                file.write('{}'.format(ride.id))