from random import randint
import numpy as np
from math import sqrt

ITERATIONS = 10
MEANS = 10

minx=1e9
miny=1e9
maxx=-1e9
maxy=-1e9

data = None
centers = None

def dist(p1, p2):
    return sqrt(abs(p1[0]-p2[0])**2 + abs(p1[1]-p2[1]))

if __name__ == '__main__':
    try:
        MEANS = int(input("How many clusters? "))
    except:
        pass

    num_pts = int(input("How many points? "))
    data = np.zeros((num_pts, 2), dtype=float)
    for i in range(num_pts):
        data[i][0], data[i][1] = map(lambda n: float(n), input("Point? ").strip().split(' '))
        # TODO not dry
        minx = min(minx, data[i][0])
        maxx = max(maxx, data[i][0])
        miny = min(miny, data[i][1])
        maxy = max(maxy, data[i][1])

    # centers = np.zeros((MEANS, 2))
    # for i in range(MEANS):
    #     centers[i] = [randint(minx, maxx), randint(miny, maxy)]

    # centers = np.array(np.random.choice(data, MEANS, replace=False))    # why does it have to be 1d bruh

    centers = np.random.permutation(data)[:MEANS]    # TODO sketchy + inefficient random.sample

    print(data)
    print(centers)
    print("\n\n\n")

    for it in range(ITERATIONS):
        count = np.zeros(MEANS,      dtype=float)
        sums  = np.zeros((MEANS, 2), dtype=float)
        # cluster = np.zeros(num_pts)
        for p in data:
            cluster = 0
            # find best cluster
            for i,g in enumerate(centers):
                if dist(p, g) < dist(p, centers[cluster]):      # if g is closer
                    cluster = i
            # remember in cluster data
            count[cluster] += 1
            sums [cluster] += p
    sums /= np.tile(count, (2, 1)).T
    print(sums)


