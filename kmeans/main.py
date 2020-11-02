from random import randint

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
        data.append(float(input("x? ")), float(input("y? ")))
        # TODO not dry
        minx = min(minx, data[-1][0])
        maxx = max(maxx, data[-1][0])
        miny = min(miny, data[-1][1])
        maxy = max(maxy, data[-1][1])

    for i in range(MEANS):
        centers.append(randint(minx, maxx), randint(miny, maxy))

    for i in range(ITERATIONS):
        pass

