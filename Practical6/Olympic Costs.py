costs = [1, 8, 15, 7, 5, 14, 43, 40]
l = sorted(costs)
print (l) # sort and print




import numpy as np
import matplotlib.pyplot as plt
ind = np.arange(8) # 8 olympics
plt.ylabel('Costs')
plt.title('Olympic Costs')
plt.xticks(ind, ('Los Angeles 1984', 'Seoul 1988', 'Barcelona 1992', 'Atlanta 1996', 'Sydney 2000',
           'Athens 2003', 'Beijing 2008', 'London 2012'))
plt.tick_params(axis='x', labelsize=5) # avoiding overlap
plt.bar(x=ind, height=costs)
plt.show()
