import matplotlib.pyplot as plt
import csv

x = ['Arsenal', 'Liverpool', 'Manchester United', 'Newcastle', 'Liverpool']
y = []

with open('football_plot.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        y.append(int(row[4]))

plt.scatter(x,y)

plt.xlabel('Teams')
plt.ylabel('Number of Wins')
plt.title('Number of Wins by Team')
plt.show()