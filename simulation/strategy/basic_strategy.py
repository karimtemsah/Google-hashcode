class BasicStrategy:

    def run(self, city):

        for ride in city.rides:
            city.cars[0].rides.append(ride)

        return city