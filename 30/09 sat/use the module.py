# main.py

import my_module

# Using functions from the module
message = my_module.greet("Alice")
print(message)

# Using variables from the module
radius = 5
circle = my_module.Circle(radius)
print(f"Circle area with radius {radius}: {circle.area()}")
print(f"Value of PI from the module: {my_module.PI}")
