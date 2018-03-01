class ShortestDistance:

    def run(self, city):
        rides = self.bsort(city.rides)
        count = 0
        counter = 0
        for ride in rides:
            if count < city.fleet_size-1:
                city.cars[counter].rides.append(ride)
                if (count % 3) == 0:
                    counter = counter+1
                count = count+1

        return city

    def bsort(self, nlist):
        for passnum in range(len(nlist)-1,0,-1):
            for i in range(passnum):
                if abs(nlist[i].start[0] - nlist[i].end[0]) > abs(nlist[i+1].start[1] - nlist[i+1].end[1]):
                    temp = nlist[i]
                    nlist[i] = nlist[i+1]
                    nlist[i+1] = temp
        return nlist