class Some:
    def __init__(self, value='anka'):
        self.name = value
    
    def getname(self):
        return self._name
    

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value
    

s = Some('sad')
#s = 'jjjj'
print(s.getname())
