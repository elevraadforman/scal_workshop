import numpy as np
import matplotlib.pyplot as plt


class LET:
    def __init__(self, Lw, Ew, Tw, Lo, Eo, To, rock_type):
        
        #define paramters
        self.Lo =  Lo
        self.Eo =  Eo
        self.To =  To
        self.Lw =  Lw
        self.Ew =  Ew
        self.Tw =  Tw  
        self.rock_type = rock_type     

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

        ax.set_title(self.rock_type)

        plt.show()





class Rock:
    """
    A class representing a rock-type.

    Attributes(properties):
    -----------
    rock_type: string
        the type of rock 
    
    porosity: float

    permeability: int
    """

    def __init__(self, rock_type: str, porosity: float, permeability: int):
        self.LET = None
        self.rock_type = rock_type
        self.porosity = porosity
        self.permeability = permeability
        print('A new object of class Rock is created')

    def print_properties(self):
        """
        A method to print the properties of a rock.
        """
        print(f"Rock type: {self.rock_type}, Porosity: {self.porosity}, Permeability: {self.permeability}mD")

    def add_LET(self, Lw, Ew, Tw, Lo, Eo, To):
        self.LET = LET( Lw, Ew, Tw, Lo, Eo, To, self.rock_type)


# Creating an instances of rock
Berea = Rock("sandstone", 0.21, 400)
#Austin_chalk= Rock("chalk", 0.38, 50)
#Bachalau_carbonate = Rock("carbonate", 0.29, 1000)



# Adding LET to instance of Rock at the same time creating an instance of LET
Berea.add_LET(2, 3, 4, 2, 3, 4)



print(Berea.LET.Swir)

Berea.print_properties()

# Calling method plotLET of LET through objectA
Berea.LET.plotLET()
