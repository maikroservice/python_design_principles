# OCP = open for extension, closed for modification
# after you have written and tested a class you should not change it
# only extend it! -> class should be extendable but we should _not_ change! it

from enum import Enum


class Color(Enum):
    BLACK = 0
    WHITE = 1
    RED = 2
    GREEN = 3
    BLUE = 4
    YELLOW = 5


class Size(Enum):
    SMALL = 0
    MEDIUM = 1
    LARGE = 3
    XLARGE = 4


class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size


class ProductFilter:
    def filter_by_color(self, products, color):
        for p in products:
            if p.color == color:
                yield p

    def filter_by_size(self, products, size):
        for p in products:
            if p.size == size:
                yield p


class Specification:
    # specification -> enterprise pattern

    def is_satisfied(self, item):
        pass

        def __and__(self, other):
            """
            overloads the `and` operator so that we can use it 
            more easily with AndSpecifications
            
            """
            return AndSpecification(self, other)


class Filter:
    def filter(self, items, spec):
        pass


class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color


class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item


class AndSpecification(Specification):
    """
    combinator - combines other structures in this case filters
    """

    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):
        return all(map(lambda spec: spec.is_satisfied(item), self.args))


if __name__ == "__main__":
    pear = Product("Pear", Color.GREEN, Size.SMALL)
    car = Product("Ford", Color.BLUE, Size.XLARGE)
    mouse = Product("HyperX Pulsefire Surge", Color.BLACK, Size.SMALL)
    crate_of_pears = Product("Crate of pears", Color.GREEN, Size.MEDIUM)
    car2 = Product("Citröen", Color.BLUE, Size.XLARGE)
    shrub = Product("Shrub", Color.GREEN, Size.MEDIUM)

    products = [pear, car, mouse, crate_of_pears, car2, shrub]

    product_filter = ProductFilter()
    print("looking for blue products:")
    for product in product_filter.filter_by_color(products, Color.BLUE):
        print(f"- {product.name} is blue.")

    print("Blue Products in accordance with the Specification principle")
    better_filter = BetterFilter()
    blue = ColorSpecification(Color.BLUE)
    for product in better_filter.filter(products, blue):
        print(f" - {product.name} is blue.")

    print("Small product Specification:")
    small = SizeSpecification(Size.SMALL)
    for small_product in better_filter.filter(products, small):
        print(f" - {small_product.name} is small.")

    print(f"use combinator for multiple filter:")
    medium = SizeSpecification(Size.MEDIUM)
    green = ColorSpecification(Color.GREEN)

    # medium_green = AndSpecification(medium, green)

    # we can now use the overloaded `and` to filter easier
    medium_green_and = green and medium
    for product in better_filter.filter(products, medium_green_and):
        print(f" - {product.name} is green and medium sized.")
