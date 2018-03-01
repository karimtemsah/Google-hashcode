class ImprovedStrategy:

    def run(self, city):
        rides = bsort(city.rides.earlieststart)
        count = 0
        for ride in rides:
            city.cars[count].rides.append(ride)
            count = count+1

        return city



def bsort(nlist):
    for passnum in range(len(nlist)-1,0,-1):
        for i in range(passnum):
            if nlist[i] > nlist[i+1]:
                temp = nlist[i]
                nlist[i] = nlist[i+1]
                nlist[i+1] = temp