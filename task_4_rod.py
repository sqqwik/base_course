import matplotlib.pyplot as plt
import numpy as np
k = 10
def spiral(k):
    phi = np.arange(0.01, 8*(np.pi), 0.1)
    r = k / np.sqrt(phi)
    x = r * np.cos(phi)
    y = r * np.sin(phi)

    plt.plot(x, y, label="жезл", color="y")
    plt.xlabel("Coord - x")
    plt.ylabel("Coord - y")
    plt.title("жезл")
    plt.legend()
    plt.grid()
    plt.axis('equal')
    
    plt.savefig('fig_11.png')

