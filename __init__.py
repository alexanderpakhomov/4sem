class vector:

    def __init__(self, coords):
        self.coordinates = coords

    def __add__(self, obj):
        ret = self.coordinates[:]
        for i in range(len(obj.coordinates)):
            try:
                ret[i] += obj.coordinates[i]
            except:
                ret.append(obj.coodinates[i])
        return vector(ret)

    def sub(self, obj):
        for i in range(len(obj.coordinates)):
            try:
                self.coordinates[i] -= obj.coordinates[i]
            except:
                self.coordinates.append(-obj.coordinates[i])

    def print_vector(self):
        string = ''
        for i in range(len(self.coordinates)):
            if not len(string) == 0:
                string += ':'
                string += str(self.coordinates[i])
        print(string)


a = vector([3, 4, 6, 13, 55, 13])
b = vector([3, 1, 2, 3])
a += a

a.print_vector()
b.sub(a)
b.print_vector()