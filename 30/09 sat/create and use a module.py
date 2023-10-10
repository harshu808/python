# my_module.py

def greet(name):
    return f"Hello, {name}!"


PI = 3.14159


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return PI * self.radius ** 2
