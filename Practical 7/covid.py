import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("C:/Users/51389/Downloads")
covid_data = pd.read_csv("full_data.csv")
# importing the .csv file works
print(covid_data.iloc[0:1001:100, 2])
# showing the second column from every 100th row from the first 1000 rows

print(covid_data.loc[0:81, "total_cases"])

location_list = []
n = 0
while n <= 7995:
    if covid_data.iloc[n, 1] == "Afghanistan":
        location_list.append(True)
    else:
        location_list.append(False)
    n = n+1
print(covid_data.loc[location_list, "total_cases"])
# total cases for all rows corresponding to Afghanistan

time_list = []
m = 0
while m <= 7995:
    if covid_data.iloc[m, 0] == "2020-03-31":
        time_list.append(True)
    else: time_list.append(False)
    m = m+1
new_data = covid_data.iloc[time_list, 2:4]
print(new_data.describe()) # mean
plt.boxplot(new_data)
plt.title("3-31")
plt.show() # boxplot of 3-31 new_cases and new deaths

world_date = covid_data.iloc[7880:7972, 1]
world_new_cases = covid_data.iloc[7880:7972, 2:4]
plt.plot(world_date, world_new_cases, 'b+')
plt.xticks(world_date.iloc[0:len(world_date):4], rotation=-90)
plt.show() # plot world death and new cases

Algeria_dates = covid_data.iloc[105:192, 0]
Algeria_cases = covid_data.iloc[105:192, 2]
total_case = [covid_data.iloc[105, 2]]
days = 106
while days <= 191:
    case1 = np.array(total_case[days-106])
    case2 = np.array(covid_data.iloc[days, 2])
    case3 = case1+case2
    total_case.append(case3)
    days = days+1
print(case3)
plt.plot(Algeria_dates, total_case)
plt.plot(Algeria_dates, Algeria_cases)
plt.xticks(Algeria_dates.iloc[0:len(Algeria_dates):4], rotation=-90)
plt.legend
plt.show() # plot Algeria cases