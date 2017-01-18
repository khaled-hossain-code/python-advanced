import threading, random

def loopAThrough(x):
    
    for i in xrange(100000):
        pass
    
    print "I am ThreadNo: " + str(x)

if __name__ == '__main__':
    numberOfThread = 5
    threadList = []

    print "STARTING........"
    for i in range(numberOfThread):
        t = threading.Thread(target = loopAThrough, args=(i,))
        t.start()
        threadList.append(t)
    
    print "Number of Threads: " + str(threading.activeCount())

    print "FINISH.........."
