"""
Створити клас особа,  в якому конструктор встановлює ім’я, вік. Використати в цьому класі геттери та сеттери, а також створити метод info, 
який виводить інформацію про ім’я та вік особи. 
А тоді створити клас працівник, який наслідується від класу особи і містить метод details, 
який на вхід отримує параметр про компанію, в якій працює працівник і цей метод 
виводить інформацію про те, що працівник з таким то іменем працює в такій то компанії.
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        self.__age = age

    def info(self):
        print(f"{self.name} have {self.age} years old.")

class Employee(Person):

    def __init__(self, name, age):
        super().__init__(name, age)

    def details(self, company):
        print(f"Employee {self.name} works at {company}")

p1 = Person("Samuel Vimes", 45)
p1.age = 46
p1.info()

emp = Employee("Samuel Vimes", 47)
emp.info()
emp.details("Night watch")