# sort and print
costs = [1, 8, 15, 7, 5, 14, 43, 40]
l = sorted(costs)
print (l)

# A bar plot displaying this sorted distribution of marks
import matplotlib.pyplot as plt
import numpy as np
ind = np.arange(8) # 8 olympics
plt.ylabel('Costs')
plt.title('Olympic Costs')
plt.xticks(ind, ('Los Angeles 1984', 'Sydney 2000', 'Atlanta 1996', 'Seoul 1988',  'Athens 2003',  'Barcelona 1992',
                 'London 2012', 'Beijing 2008'))
plt.tick_params(axis='x', labelsize=5) # avoiding overlap
plt.bar(x=ind, height=l) # sorted
plt.show()