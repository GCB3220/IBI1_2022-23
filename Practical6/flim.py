# create dictionary and print it
flim = {'comdey': 73, 'action': 42, 'romance': 38, 'fantasy': 28, 'science-fiction': 22,
        'horror': 19, 'crime': 18, 'documentary': 12, 'history': 8, 'war': 7}
print(flim)


# draw a pie chart
import matplotlib.pyplot as plt
explode = [0, 0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3]
plt.pie(list(flim.values()), # size
        explode=explode, labels=list(flim.keys()), # use dictionary
        autopct='%1.1f%%', pctdistance=0.7, shadow=False, startangle=90)
plt.show()


