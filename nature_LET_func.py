import matplotlib.pyplot as plt
import numpy as np

L=1
E=43
T=1
swl = 0.1

Pct = 1.2
Pcir = 8

# Generate 20 evenly distributed x values between 0 and 1
sw = np.linspace(swl, 1, 20)

# Calculate xn = (x - 0.1) / (1 - 0.1)
swn = (sw - swl) / (1 - swl)

# Calculate y = 3 * xn
Fc = (1-swn)**L/(
    ((1-swn)**L)+(E*swn**T)
)

Pc = (Pcir - Pct)*Fc + Pct

# Plot the results
plt.plot(sw, Pc)

# Set labels and title
plt.xlabel("Sw")
plt.ylabel("Pc")
plt.title("LET Pc")

# Show the plot
plt.show()
