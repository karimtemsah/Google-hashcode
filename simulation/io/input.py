from ..models.models import City, Ride

def read(filename):
    rides = []

    with open(filename, 'r') as file:
        i = 0
        for line in file.readlines():
            l = line.rstrip('\n').split(" ")
            l = list(map(int, l))
            if i == 0:
                city = City(l[0], l[1], l[2], l[3], l[4], l[5])
            else:
                rides.append(Ride(i-1, l[0], l[1], l[2], l[3], l[4], l[5]))
            i += 1
        city.rides = rides
        return city


