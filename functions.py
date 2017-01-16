
def func():
    def greet():
        print 'Hello'
    return greet

myFunc = func()

myFunc()