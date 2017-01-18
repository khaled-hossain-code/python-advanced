BaseClass = type("BaseClass",(object,),{})
C1 = type("C1",(BaseClass,),{"x":1})
C2 = type("C2",(BaseClass,),{"x":2})

def MyFactory(myBool):
    return C1() if myBool else C2()

m1 = MyFactory(True)
m2 = MyFactory(False)

print m1.x
print m2.x

print type(m1) #m1 is a instance of C1 class
print type(m1.__class__) #its type is 'type'