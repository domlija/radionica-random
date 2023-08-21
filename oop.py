import math

#abstraktna klasa 
class Shape():
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return self.color + ' Shape'

    def calculate_area(self):
        raise Exception('Undefined method')

    def __lt__(self, other):
        if not isinstance(other, Shape):
            raise Exception('Type error')

        return self.calculate_area() < other.calculate_area()
    
        

class Rectangle(Shape):
    def __init__(self, color, a, b):
        super().__init__(color)
        self.a = a 
        self.b = b

    def calculate_area(self):
        return self.a * self.b

    def __str__(self):
        return self.color + ' ' + self.__class__.__name__

    def __eq__(self, o):
        if not isinstance(o, Rectangle):
            return False 
        
        if self.color == o.color and \
            self.a == o.a and \
            self.b == o.b:
            return True

        return False

    def __hash__(self) -> int:
        return hash((self.color, self.a, self.b))
        

    

class Circle(Shape):
    def __init__(self, color, r):
        super().__init__(color)
        self.r = r 

    def calculate_area(self):
        return self.r ** 2 * math.pi 

    def __str__(self):
        return self.color + ' Circle'

class Square(Rectangle):
    def __init__(self, color, a):
        super().__init__(color, a, a)
    


r1 = Rectangle('red', 2, 3)
r2 = Rectangle('red', 2, 1)

d1 = {r1: "plavo",r2: "crveno"}
print(d1[r1])

