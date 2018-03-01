from random import randint


class RandomCarStrategy:

    def run(self, city):

        for ride in city.rides:
            car_number = randint(0, city.fleet_size+1)
            city.cars[car_number].rides.append(ride)

        return city