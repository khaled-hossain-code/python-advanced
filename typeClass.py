#create a small class on the fly using any existing function and variable
x = 10

def greet(self):
    print "Hello"

#type(name,tuple of baseClass,dict of params)
TypeClass = type("TypeClass",(object,),{"x":x,"greet":greet})

t = TypeClass()

print t.x
print t.greet()
