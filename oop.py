class BaseClass(object):
    def greet(self,name):
        print "Hello "+name

class InheritingClass(BaseClass):
    pass

khaled = InheritingClass()

khaled.greet("khaled")

#inheritance
class Character(object):
    def __init__(self):
        self.health = 100

class Blacksmith(Character):
    def __init__(self):
        super(Blacksmith,self).__init__()

bs = Blacksmith()
print bs.health