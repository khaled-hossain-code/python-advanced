def addOne(myFunc):
    def addOneInside():
        return myFunc()+1
    return addOneInside

@addOne   #here addOne is the decorator which says pass oldFunc() to addOne function and replace the returned object with oldFunc
def oldFunc():
    return 3

print oldFunc()