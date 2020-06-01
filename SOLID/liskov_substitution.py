# env/bin/python3


""" 
The Liskov Substitution Principle - named after Barbara Liskov
extends the open closed principle.
If you have an Interface that takes some base class 
you should be able to put a derived class in there
and everything should work
"""


class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def area(self):
        return self._height * self._width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        self._width = width

    def __str__(self):
        return f"rectangle w: {self.width} h: {self.height}"


def fun_with_rectangles(rectangle: Rectangle):
    width = rectangle.width
    HEIGHT = 10
    rectangle.height = HEIGHT
    expected_area = int(width * HEIGHT)
    print(f"expected area was {expected_area}, calculated area was {rectangle.area}")


if __name__ == "__main__":
    rectangle = Rectangle(3, 4)
    fun_with_rectangles(rectangle)
