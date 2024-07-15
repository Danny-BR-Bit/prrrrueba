import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10,100)
y = np.sin(x)
plt.plot(x,y,"k")
plt.title("F(x) = Sen(x)")
plt.xlabel("X")
plt.ylabel("Sen (x)")
plt.grid()
plt.xlim(0,10)
plt.ylim(-3,3)
plt.savefig("Sen(x).pdf")
plt.show()