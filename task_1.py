import matplotlib.pyplot as plt 

x = [1,1,5,5,1]
y = [1,5,5,1,1]
plt.plot(x, y, color="r", marker="o", ms="5")
plt.plot(x,y)
plt.axis("equal")

plt.savefig("fig_5.png") 