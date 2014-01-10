# Init Objects

#Character Objects
init python:
    World = World()
    
    Cybele = Girl("Cybele")
    Tara = Girl("Tara")
    Hecate = Girl("Hecate")
    Iris = Girl("Iris")
    
    # World.avatar should depend on who player picks on thier first game.
    World.avatar = Cybele
    
    #World.createGlobalAffection(World.avatar.girlList, World.avatar.createAffection())