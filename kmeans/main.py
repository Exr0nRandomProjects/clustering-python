from random import randint
from sys import argv

ITERATIONS = 10
MEANS = 10

minx=1e9
miny=1e9
maxx=-1e9
maxy=-1e9

data = []
centers = []

if __name__ == '__main__':
    try:
        MEANS = int(input("How many clusters? "))
    except:
        pass

    num_pts = int(input("How many points? "))
    for i in range(num_pts):
        data.append(list(map(lambda n: float(n), input("Point? ").strip().split(' '))))
        # TODO not dry
        minx = min(minx, data[-1][0])
        maxx = max(maxx, data[-1][0])
        miny = min(miny, data[-1][1])
        maxy = max(maxy, data[-1][1])

    for i in range(MEANS):
        centers.append((randint(minx, maxx), randint(miny, maxy)))

    for p in data:
        print(f'{p[0]} {p[1]}')

    for i in range(ITERATIONS):
        pass

