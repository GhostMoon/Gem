# Item class

init python:
    class Item(object):
        '''Item has a name, price, and a description.'''
        
        # Constructor
        def __init__(self, name='Name', price=0, desc='None'):
            self.name = name
            self.price = price
            self.desc = desc