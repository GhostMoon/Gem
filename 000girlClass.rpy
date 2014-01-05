# Character Girl Code
init python:
    class Girl(object):
        '''Player will be able to play as any Girl.
        Girls shares currency and purse attributes.'''
        
        # Properties
        listOfGirls = {}  # key is String self.name, value is self
        #gems = 0
        purse = []
        
        # Constructor
        def __init__(self, name='Name', mood='Neutral', stats=None, partner=None, gems=0):
            self.name = name
            self.mood = mood
            self.stats = stats
            self.partner = partner
            self.gems = gems
            self.listOfGirls[self.name] = self
            
        # Partner methods
        def addPartner(self, otherGirl):
            '''otherGirl -> Function
            Assigns otherGirl to be your current partner.'''
            
            self.partner = otherGirl
            otherGirl.partner = self
            return renpy.say(avatar, "You have a new partner! %s!" % (otherGirl.name))
            
        def removePartner(self, otherGirl):
            '''otherGirl -> Function
            Removes otherGirl from the partnership.'''
            self.Partner = None
            return renpy.say(avatar, "You are no longer partners with her.")
            
        # Currency methods
        def updateGems(self, factor):
            '''Interger -> None
            Does addition to the amount of gems you have by factor.'''
            self.gems += factor
        
        # Purse methods
        def addToPurse(self, itemObject):
            '''Item -> None
            Adds itemObject to the purse.'''
            purse.append(item)
            
        def getListOfGirls(self):
            '''Dictonary -> Keys(String)
            Displays all Girls in the game.'''
            v = self.listOfGirls.keys()
            return renpy.say(avatar, v)
            
    