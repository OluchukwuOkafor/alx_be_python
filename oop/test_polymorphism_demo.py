from polymorphism_demo import Shape, Rectangle, Circle

shapes = [
    Rectangle(10, 5),
    Circle(7)
]

for shape in shapes:
    print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")
