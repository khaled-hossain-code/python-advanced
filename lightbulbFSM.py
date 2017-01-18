from random import randint
from time import clock

State = type("State",(object,),{})

##---------------------------------------------------
class LightOn(State):#inherited from State class because its a state
    def Execute(self):
        print "Light is On"

class LightOff(State):#inherited from state class coz its a state
    def Execute(self):
        print "Light is Off"

##------------------------------------------------

