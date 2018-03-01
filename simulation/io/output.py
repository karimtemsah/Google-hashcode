def write(filename, city):
    with open(filename, 'w') as file:
        for car in city.cars:
            file.write('{}'.format(len(car.rides)))
            for ride in car.rides:
                file.write(' {}'.format(ride.id))
            file.write('\n')