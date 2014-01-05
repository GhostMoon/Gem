# Locations are  a place in the World

init python:
    
    class Location(object):
        '''Location is a place in the World.'''
        
        # Properties
        inhabited = []
        
        # Constructor
        def __init__(self, name="Location"):
            self.name = name
            