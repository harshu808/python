# Use map and a lambda function to find the maximum x coordinate (the 0-th coordinate) in a list of points. You will need to apply max to the result of the map


# List of points as tuples (x, y)
points = [(1, 3), (5, 2), (0, 7), (8, 4)]

# Use map and lambda to extract the x-coordinates
x_coordinates = list(map(lambda point: point[0], points))

# Find the maximum x-coordinate using the max function
max_x = max(x_coordinates)

# Display the result
print("List of x-coordinates:", x_coordinates)
print("Maximum x-coordinate:", max_x)
