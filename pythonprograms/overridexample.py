class Geometry:
    def area(self):
        print("area is bounded, but cannot calculated")

class Square(Geometry):
    def area(self):
        #super().area()
        print("Side of Square is area")

class Rectangle(Geometry):
    def area(self):
        print("Product of length and breadth is area")

class Triangle(Geometry):
    def area(self):
        print("Product of half base and height")



if __name__ == "__main__":
    geometry = Geometry()
    geometry.area()

    square = Square()
    square.area()

    rectangle = Rectangle()
    rectangle.area()

    triangle = Triangle()
    triangle.area()

