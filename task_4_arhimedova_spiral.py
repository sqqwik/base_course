import matplotlib.pyplot as plt
import numpy as np
k = 100
def spiral(k):
    phi = np.arange(0, 8*(np.pi), 0.1)
    r = k * phi
    x = r * np.cos(phi)
    y = r * np.sin(phi)

    plt.plot(x, y, color="r", label="Архимедова спираль")
    plt.xlabel("Coord - x")
    plt.ylabel("Coord - y")
    plt.title("Архимедова спираль")
    plt.legend()
    plt.grid()
    plt.axis('equal')
    
    plt.savefig('fig_10.png')
