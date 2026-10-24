import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def euclidean_distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


class Vector(Point):
    def __str__(self):
        return f"Vector <{self.x}, {self.y}>"

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)


# Point demonstration
p1 = Point(1, 2)
p2 = Point(4, 6)
p3 = Point(1, 2)

print("--- Point ---")
print("p1:", p1)
print("p2:", p2)
print("p1 == p2:", p1 == p2)
print("p1 == p3:", p1 == p3)
print("p1 == 5:", p1 == 5)
print("distance from p1 to p2:", p1.euclidean_distance(p2))

# Vector demonstration
v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2

print("--- Vector ---")
print("v1:", v1)
print("v2:", v2)
print("v1 == v2:", v1 == v2)
print("v1 == Vector(1, 2):", v1 == Vector(1, 2))
print("v1 + v2:", v3)
print("type of v1 + v2:", type(v3).__name__)
print("distance from v1 to v2 (inherited):", v1.euclidean_distance(v2))
print("v1 is a Point:", isinstance(v1, Point))
