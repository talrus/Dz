"""
Створити батьківський клас Figure з методами 
init: ініціалізується колір, 
get_color: повертає колір фігури, 
info: надає інформацію про фігуру та колір,  
від якого наслідуються такі класи як Rectangle, Square, які мають інформацію про ширину, висоту фігури, метод square, який знаходить площу фігури.
"""
class Figure:
    def __init__(self, name, color="red"):
        self.color = color
        self.name = name

    def get_color(self):
        return self.color
    
    def info(self):
        print(f"My color is: {self.color} and I am {self.name}.")

class Rectangle(Figure):
    
    def __init__(self, side_a, side_b, color='red'):
        super().__init__("Rectangle", color)
        self.side_a = side_a
        self.side_b = side_b
    
    def area(self):
        return self.side_a * self.side_b
    
class Square(Figure):
    
    def __init__(self, side, color='red'):
        super().__init__("Square", color)
        self.side = side
    
    def area(self):
        return self.side * self.side

rec = Rectangle(12, 22)
print(rec.area())
rec.info()

square = Square(8, "Blue")
print(square.area())
square.info()