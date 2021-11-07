import util

NO_NAME_PRINT = True

# Sample class
class Sample(object):

    def __init__(self, name, features, label = None):
        #Assumes features is an array of numbers
        self.name = name
        self.features = features
        self.label = label

    def dimensionality(self):
        return len(self.features)

    def getFeatures(self):
        return self.features[:]

    def getLabel(self):
        return self.label

    def getName(self):
        return self.name

    def distance(self, other):
        return util.minkowskiDist(self.features, other.getFeatures(), 2)

    def __add__(self, other):
        f = []
        for i in range(self.dimensionality()):
            f.append(self.getFeatures()[i] + other.getFeatures()[i])
        return Sample(self.name + '+' + other.name, f)

    def __truediv__(self, n):
        f = []
        for e in self.getFeatures():
            f.append(e/float(n))
        return Sample(self.name + '/' + str(n), f)

    def __sub__(self, other):
        f = []
        for i in range(self.dimensionality()):
            f.append(self.getFeatures()[i] - other.getFeatures()[i])
        return Sample(self.name + '-' + other.name, f)

    def __mul__(self, other):
        f = []
        for i in range(self.dimensionality()):
            f.append(self.getFeatures()[i] * other.getFeatures()[i])
        return Sample(self.name + '*' + other.name, f)

    def power(self, x):
        f = []
        for i in range(self.dimensionality()):
            f.append(self.getFeatures()[i] ** (x))
        return Sample(self.name + '-power(' + str(x) + ')', f)

    def vec_div(self, other):
        f = []
        for i in range(self.dimensionality()):
            f.append(self.getFeatures()[i] / float(other.getFeatures()[i]))
        return Sample(self.name + '/' + other.name, f)

    def __str__(self):
        if NO_NAME_PRINT:
            return str(self.features)
        else:
            return self.name +':'+ str(self.features) + ':' + str(self.label)

if __name__ == "__main__":
    a = Sample('a', [1, 1])
    b = Sample('b', [-1, -1])
    print(a)
    print(b)
    print(a + b)
    print(a - b)
    print(a/2)
