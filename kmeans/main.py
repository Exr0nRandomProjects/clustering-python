# test data from https://www.kaggle.com/shrutimechlearn/customer-data
import numpy as np
from matplotlib import pyplot as plt, cm
import pandas as pd

from random import randint
from math import sqrt

ITERATIONS = 10
MEANS = 5

data = None
centers = None

def dist(p1, p2):
    return sqrt(abs(p1[0]-p2[0])**2 + abs(p1[1]-p2[1]))

if __name__ == '__main__':
    # try:
    #     MEANS = int(input("How many clusters? "))
    # except:
    #     pass
    #
    # num_pts = int(input("How many points? "))
    # data = np.zeros((num_pts, 2), dtype=float)
    # for i in range(num_pts):
    #     data[i][0], data[i][1] = map(lambda n: float(n), input("Point? ").strip().split(' '))

    raw_data = pd.read_csv('data/mall_customers.csv')
    data = raw_data.iloc[:, [3, 4]].values  # annual income, spending score

    centers = np.random.permutation(data)[:MEANS]   # TODO sketchy + inefficient random.sample

    # plt.scatter(*data.T, color='blue')              # TODO: "non iterable `data.T` used in an iterating context?"

    group = np.zeros(len(data), dtype=int)
    for it in range(ITERATIONS):
        count = np.zeros(MEANS,      dtype=float)
        sums  = np.zeros((MEANS, 2), dtype=float)
        for i,p in enumerate(data):
            cluster = 0
            # find best cluster
            for j,g in enumerate(centers):
                if dist(p, g) < dist(p, centers[cluster]):      # if g is closer
                    cluster = j
            # remember in cluster data
            count[cluster] += 1
            sums [cluster] += p
            # store what cluster it was in if this is the last iteration
            if (it +1 == ITERATIONS):
                group[i] = cluster
        centers = sums / np.tile(count, (2, 1)).T               # update the centers
        plt.scatter(*centers.T, color=[1-it/ITERATIONS]*3)      # plot iteration on chart

    colors = cm.rainbow(np.linspace(0, 1, MEANS))[group] # https://stackoverflow.com/a/12236808/10372825
    # color = [colors[group[k]] for k in range(len(data))]
    # for k in range(len(data)):
        # print(group[k], colors[group[k]])
    print(colors[group])
    # print(color)
    plt.scatter(*data.T, color=colors)
    plt.show()

