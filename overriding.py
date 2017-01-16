class BaseClass(object):
    def __init__(self):
        self.x = 10
        self.y = 10
    
    def run(self):
        print "BaseClass Running"
    def test(self):
        print "I am base class"

#subClass is inheriting from BaseClass
class SubClass(BaseClass):
    def __init__(self):
        super(SubClass,self).__init__()
        self.x = 20
    
    def test(self):
        print "I am in SubClass"

obj = SubClass()

print obj.x  #overriding variable
print obj.y  #inheriting from baseclass

obj.test()  #overriding baseclass function
obj.run()   #inheriting baseclass function

#lets find out from a base class which classes are inherted
print BaseClass.__subclasses__()
