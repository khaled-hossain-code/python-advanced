"""
Builtin Variables are 
__builtins__: {'ArithmeticError':....}
    viewitems()
__name__: '__main__'
__file__: '/Users/user/Documents/khaled/hello.py'
__doc__: None
__package__: None
"""
import time as t
from os import path

def createFile(dest):
    """
    This function creates a file in given destination,
    filename is based on time 
    """
    date = t.localtime(t.time())
    name = '%d.%d.%d' %(date[2],date[1],date[0])
    fullName = dest + name 

    if not(path.isfile(fullName)):
        f = open(fullName,'w')
        f.write('\n'*30)
        f.close()
    print name
## data[0] = year , data[1]=Month data[2] = date

if __name__ == '__main__':
    destination = '/Users/user/Documents/khaled/'
    createFile(destination)
    raw_input("done!!!")