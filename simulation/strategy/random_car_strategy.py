class BasicStrategy:

    def run(self, city):

        count = 0

        for ride in city.rides:
            city.cars[count].rides.append(ride)

        return city