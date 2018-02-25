import matplotlib.pyplot as plt

x = list(range(1001))
y = [n**2 for n in x]

plt.scatter(x, y, c=y, cmap=plt.cm.Blues, edgecolor='none', s=40)
plt.axis([0, 1100, 0, 1100000])
plt.show()
