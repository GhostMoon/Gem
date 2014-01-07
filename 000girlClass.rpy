# Character Girl Code

init python:
    class Girl(object):
        '''User will be able to control any Girl object.'''
        
        # Properties
        girlDict = {}  # key is String self.name, value is self
        girlList = []
        
        # Constructor
        def __init__(self, name='Name', mood='Neutral', stats=None, partner=None, gems=0, purse=[], affections={}):
            self.name = name
            self.mood = mood
            self.stats = stats
            self.partner = partner
            self.gems = gems
            self.purse = purse
            self.girlDict[self.name] = self
            self.girlList.append(self)
            self.affections = affections
            
        # Partner methods
        def addPartner(self, otherGirl):
            '''otherGirl -> Screen
            Assigns otherGirl to be your current partner.'''
            
            # Check to see if you have a partner and if so, terminate that partnership.
            if self.partner != None:
                self.partner.partner = None
                self.partner = otherGirl
                
            else:
                self.partner = otherGirl
            
            # Check to see if otherGirl has  a partner and if so, terminate that partnership.
            if otherGirl.partner != None:
                otherGirl.partner.partner = None
                otherGirl.partner = self
                
            else:
                otherGirl.partner = self
            return renpy.say(avatar, "You have a new partner! %s!" % (otherGirl.name))
            
        def removePartner(self):
            '''otherGirl -> Screen
            Removes otherGirl from the partnership.'''
            
            if self.partner == None:
                return renpy.say(avatar, "You don't have a partner.")
                
            else:
                renpy.say(avatar, "You are no longer partners with %s." % (self.partner.name))
                self.partner.partner = None
                self.partner = None
                
        # Affection methods
        def createAffection(self):
            '''List -> Keys
            Append every object in List as a key in the affections Dictonary except for self.'''
            
            for girl in self.girlList:
                self.affections[girl] = 10
            self.affections.pop(self)
            
        # Currency methods
        def updateGems(self, factor):
            '''Interger -> None
            Does addition to the amount of gems you have by factor.'''
            self.gems += factor
        
        # Purse methods
        def addToPurse(self, itemObject):
            '''Item -> None
            Adds itemObject to the purse.'''
            self.purse.append(item)
            