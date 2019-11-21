'''
Створити клас машина з атрибутами name,  make, model та методами start та stop, які виводять інформацію про те що автомобіль стартував чи зупинився відповідно.
'''
class Car:

    def __init__(self, name, make, model):
        self.name = name
        self.make = make
        self.model = model
    
    def start(self):
        print("The car have started.")
    
    def stop(self):
        print("The car have stoped.")
    
car1 = Car("Audi", 2008, "A8")
car1.start()
car1.stop()