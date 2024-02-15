class LET:
    def __init__(self, a, b, Lw, Ew, Tw, Lo, Eo, To):
        self.a = a
        self.b = b
        self.Lo = Lo
        self.Eo = Eo
        self.To = To
        self.Lw = Lw
        self.Ew = Ew
        self.Tw = Tw

    def plotLET(self):
        print(f"Plotting LET for a={self.a}, b={self.b}")

class ObjectA:
    def __init__(self):
        self.LET = None

    def add_LET(self, LET):
        self.LET = LET

    def add_LET(self, a, b):
        self.objectB = ObjectB(a, b)

# Creating an instance of ObjectA
objectA = ObjectA()

# Creating an instance of LET
LET = LET(10, 20)

# Adding LET to objectA
objectA.add_LET(LET)

# Calling method plotLET of LET through objectA
objectA.LET.plotLET()