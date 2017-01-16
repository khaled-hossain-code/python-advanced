class Mamal(object):
    def drinkMilk(self):
        print "Mamal drink Milk"

class Footballer(object):
    def playFootball(self):
        print "footballer needs to run fast"


class Player(Mamal,Footballer):
    def __init__(self):
        super(Player,self).__init__()
        print "I am a player"
    
    def drinkMilk(self):
        print "Messi drink milk" 

messi = Player()

messi.drinkMilk()
messi.playFootball()