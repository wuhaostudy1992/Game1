import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Keep making new walks, as long as the program is active
for i in range(1):
    # Make a random walk, and plot the points.
    rw = RandomWalk(50000)
    rw.fill_walk()
    
    #Set the size of the plotting window.
    plt.figure(figsize=(10, 6))
    
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x, rw.y, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=1)
    #plt.scatter(rw.x, rw.y, s=15)
    
    # Emphasize the first and last points.
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x[-1], rw.y[-1], c='red', edgecolors='none', s=100)
    
    # Remove the axes.
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
plt.show()
