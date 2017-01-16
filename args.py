def hello(greet):
    print greet


#hello() ##gives an error as hello expects an argument
hello("khaled")
#hello("khaled","Hossain") #gives an error as hello expects 1 argument but 2 passed


#unlimited arguments
def multiArgs(*Args): #getting all elements as an Array name Args
    for arg in Args:
        print arg

list = [1,2,3,4,"hello"]

person = {
    "fName":"khaled",
    "lName":"Hossain"
}

multiArgs(1,2,3,"Hello") #args can be passed separated individually
multiArgs(*list) #passing a list spreading the list


def greeting(greet="hello"):  #giving a default value of a function
    print greet + ' ' + "khaled"

greeting("hola") #calling a function with argument

def dictArgs(**kwargs):
    for item in kwargs.items():
        print item

dictArgs(x=34,y=45) #gets as tuples

## unlimited arguments and unlimited keyArguments
def Func(*args,**kwargs):
    for arg in args:
        print arg
    for item in kwargs.items():
        print item

Func(21,"Hello", x=20,name="khaled")