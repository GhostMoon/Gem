# House Class

init python:
    
    class House(object):
        '''Can change Suit, Girl, or send Gifts at House only!'''
        
        # Constructor
        def __init__(self, name='Home'):
            self.name = name
            
        # Methods
        
        def shower(self, girlObject):
            '''girlObject -> Screen
            plays the shower scene for the given girlObject.'''
            
            ### show screen
            pass
            
        def changeGirl(self, avatar, listOfGirls):
            '''Change avatar to a new Girl in the listOfGirls.'''
            
            # show a screen with girls sprites.
            # allow player to click on one.
            # update avatar to be new Girl.
            newGirl = ''
            renpy.say(self.name, "You need to pick a Girl.")
            
            avatar.getListOfGirls()
            
            
        def sleep(self, timeFunction):
            '''Time -> Time
            Advances time by factor.'''
            time = timeFunction
            return time
            
        def sendGift(self, listOfGirls, gift):
            '''Send a Gift to any Girl in the listOfGirls.'''
            
            pass
            
        def changeSuit(self, girlObject, purseObject):
            '''Changes your suit to one in your purse.'''
            
            pass
            