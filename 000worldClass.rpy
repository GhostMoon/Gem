# A new instance of world is created when a new game begins.

init python:
    import random
    
    class World(object):
        '''A new instance of world is created when a new game begins.'''
        
        # Properties
        
        # avatar is a the Object you currently control
        avatar = None
        
        # listOfLocations should contain Location Objects in the World
        listOfLocations = []
        
        #date is a Natural
        date = 0
        
        # time is a Enumeration
        # Morning, Afternoon, Evening, Midnight
        time = "Morning"
        
        # weather is a Enumeration
        # Rainy, Windy, Cloudy, Sunny
        weather = "Sunny"
        
        # Constructor
        def __init__(self, name="World"):
            self.name = self
            
        # listOfLocations Methods
        #!!
        def shuffleAvatars(self, listOfAvatars, listOfLocations):
            for avatar in listOfAvatars:
                if avatar is World.avatar:
                    pass
                else:
                    pass
                    
        # time Methods
        #!! might be no need to pass time in. Refrence self.time instead?
        def updateTime(self, time):
            ''' time -> time
            Returns the next time.'''
        
            if time == "Morning":
                return "Afternoon"
            
            if time == "Afternoon":
                return "Evening"
                
            if time == "Evening":
                return "Midnight"
                
            if time == "Midnight":
                return "Morning"
                
    # weather Methods
        def updateWeather(self, weather):
            ''' weather -> weather
            Returns the next weather.'''
            
            possible = ["Rainy", "Sunny", "Cloudy", "Windy"]
            
            return random.choice(possible)