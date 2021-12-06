import random
import math

'''
Generate n number of random points
Each point is at least 532 pixels from the previous point
points -> list of tuples in (x, y) format
screen margin of 150 pixels on all sides
allowed x [150, 1130]
allowed y [150, 570]
'''


def generator(n):

    points = [(random.randint(150, 1130), random.randint(150, 570))]

    for i in range(n - 1):
        temp = True
        while temp:
            point = (random.randint(150, 1130), random.randint(150, 570))
            dist = math.sqrt(
                (point[0] - points[-1][0])**2 + (point[1] - points[-1][1])**2)
            if dist > 532:
                points.append(point)
                temp = False

    return points
