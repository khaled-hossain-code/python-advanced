from abc import ABCMeta, abstractmethod #abc means abstract base class

class BaseClass(object):
    __metaclass__ = ABCMeta  #this means that it is a abstract class because Abstract base Class Meta is assigned

    @abstractmethod #here decorating abstractmethod
    def greet(self):
        print "Hello From base class"

class InClass(BaseClass):
    def greet(self):
        print "Hello from in class or subclass"

x = InClass()
#y = BaseClass() this line will generate error, can't instantiate abstract class

x.greet()