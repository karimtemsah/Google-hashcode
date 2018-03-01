from ..models import Car, City, Ride


class BasicStrategy:

    def run(self, city):

        availible_rides = city.rides
        city.cars = availible_rides
        city.cars[0].rides.append(availible_rides)

        return city