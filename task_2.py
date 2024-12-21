import matplotlib.pyplot as plt 
import numpy as np 
N = float()
def hyperbola_graph(min, max, N):
    x  = np.linspace(0, max, N)
    y = 1/x
    plt.plot(x, y, label="hyperbola", color="b")
    x = np.linspace(0, max, N)

    x = np.linspace(min, 0, N)
    y = 1/x 
    plt.plot(x, y, color='y')

    plt.xlabel("Coord  x")
    plt.ylabel("Coord  y")
    plt.title("hyperbola graph")
    plt.legend()
    plt.grid()

    plt.savefig('fig_6.png')

hyperbola_graph(-10,10,100)