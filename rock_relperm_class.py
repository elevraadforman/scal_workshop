import numpy as np
import matplotlib.pyplot as plt


class LET:
    def __init__(self, a, b, Lw, Ew, Tw, Lo, Eo, To):
        
        #define paramters
        self.a = a
        self.b = b
        self.Lo = Lo
        self.Eo = Eo
        self.To = To
        self.Lw = Lw
        self.Ew = Ew
        self.Tw = Tw       

        self.Swir = 0.1
        self.Sorw = 0.3
        self.kOro = 1
        self.kOrw = 0.6

        #make Sw saturation array
        self.Sw = np.linspace(self.Swir, 1-self.Sorw, 50)

        #calculate normalized Sw saturation array
        self.S_w = (self.Sw - self.Swir)/(1- self.Sorw - self.Swir)

        #water rel_perm
        self.krw = self.kOrw*((self.S_w**self.Lw)/((self.S_w**self.Lw)+self.Ew*((1-self.S_w)**self.Tw)))

        #oil rel_perm
        self.kro = self.kOro*(((1- self.S_w)**self.Lo)/(((1-self.S_w)**self.Lo)+self.Eo*(self.S_w**self.To)))

    def plotLET(self):
        #print(f"Plotting LET for a={self.a}, b={self.b}")
        # plot the data
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.plot(self.Sw, self.krw, color='b')
        ax.plot(self.Sw, self.kro, color='r')

        plt.show()

class ObjectA:
    def __init__(self):
        self.LET = None

    def add_LET(self, a, b, Lw, Ew, Tw, Lo, Eo, To):
        self.LET = LET(a, b, Lw, Ew, Tw, Lo, Eo, To)

# Creating an instance of ObjectA
objectA = ObjectA()

# Adding LET to objectA at the same time creating an instance of LET
objectA.add_LET(13, 24, 2, 3, 4, 2, 3, 4)

print(objectA.LET.Swir)

# Calling method plotLET of LET through objectA
objectA.LET.plotLET()