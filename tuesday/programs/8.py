# Write a Python program to calculate the distance between the points (x1, y1) and (x2, y2).

import math


def sq(x1, x2, y1, y2):
    dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return dist


x1, x2 = 2, 4
y1, y2 = 4, 6
d = sq(x1, x2, y1, y2)
print(d)
