'''
Your task is to complete this Class, the Person class has been created. 
You must fill in the Constructor method to accept a name as string and an age as number, complete the get Info property and get
Info method/Info getter which should return
'''
class Person:
    def __init__(self, name, age):
        self.name = str(name)
        self.age = int(age)
        
    @property
    def info(self):
        return "{}s age is {}".format(self.name, self.age)