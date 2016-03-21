class vector():
    
    def __init__(self, x):
        self.x = x

    def __add__(self, b):
        c = vector(range(0,len(self.x)))
        for i in range(0, len(self.x)):
            c.x[i] = self.x[i] + b.x[i]
        return c

    def __sub__(self, b):
        d = vector(range(0,len(self.x)))
        for i in range(0, len(self.x)):
            d.x[i] = self.x[i] - b.x[i]
        return d

    def scalar(self, b):
        c = 0
        for i in range(0,len(self.x)):
            c = c + self.x[i] * b.x[i]
        return c

k1 = input()
a = vector(k1)
k2 = input()
b = vector(k2)
c = a.scalar(b)
print "summa =", (a+b).x
print "raznost =", (a-b).x
print "skalarnoe =", c