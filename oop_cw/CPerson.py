"""
Створити клас особа,  в якому конструктор встановлює ім’я, а метод info виводить повідомлення “Hello, my name is {ім’я конкретного екземпляра класу}”, 
а також створити клас автомобіль,  в якому конструктор встановлює ім’я, а метод move виводить повідомлення 
{ім’я конкретного екземпляра класу}  moves at the speed {speed(цей параметр метод moveотримує як вхідний)} km / h
"""
class Person:
    def __init__(self, name):
        self.name = name

    def info(self):
        print(f"Hello my name is {self.name}")

class Car:
    def __init__(self, name):
        self.name = name
    
    def move(self, speed):
        print(f"{self.name} moves at speed {speed} km / h")

person1 = Person("Tomas")
person1.info()

car1 = Car("Toyota")
car1.move(160)
