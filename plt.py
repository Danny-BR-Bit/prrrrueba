import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10,100)
y = np.sin(x)
plt.plot(x,y,"k--", label = "Sen(x)", linewidth = 3)
plt.title("F(x) = Sen(x)")
plt.xlabel("X")
plt.ylabel("Sen (x)")
plt.grid()
plt.xlim(0,10)
plt.ylim(-3,3)
plt.legend()
plt.suptitle("Graphics")
plt.show()