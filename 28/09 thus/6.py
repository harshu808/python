# Use reduce to find the lower left corner (minimum x and minimum y value) for a list of point locations

from functools import reduce

# List of points as tuples (x, y)
points = [(3, 5), (1, 8), (6, 2), (2, 4)]

# Define a function to find the lower left corner for two points


def find_lower_left_corner(point1, point2):
    min_x = min(point1[0], point2[0])
    min_y = min(point1[1], point2[1])
    return (min_x, min_y)


# Use reduce to find the overall lower left corner
lower_left_corner = reduce(find_lower_left_corner, points)

# Display the result
print("List of Points:", points)
print("Lower Left Corner:", lower_left_corner)
