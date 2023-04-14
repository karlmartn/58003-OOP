class Circle:
    def __init__(self):
        self.radius = float(input("Enter the radius of the circle: "))

    # note: pi = 3.14
    def area(self):
        return self.radius ** 2 * 3.14

    def perimeter(self):
        return 2 * 3.14 * self.radius

    def display(self):
        print("The area of the circle is:", self.area())
        print("The perimeter of the circle is:", self.perimeter())

circle = Circle()
circle.display()