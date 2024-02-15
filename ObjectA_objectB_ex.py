class ObjectB:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def plotLET(self):
        print(f"Plotting LET for a={self.a}, b={self.b}")

class ObjectA:
    def __init__(self):
        self.objectB = None

    def add_objectB(self, a, b):
        self.objectB = ObjectB(a, b)

# Creating an instance of ObjectA
objectA = ObjectA()

# Adding objectB to objectA by creating an instance of ObjectB
objectA.add_objectB(10, 20)

# Calling method plotLET of objectB through objectA
objectA.objectB.plotLET()
