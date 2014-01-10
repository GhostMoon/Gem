# Gem Screen code v0.1

screen attackScreen:
    add "sideBG.png"
    frame:
        pos(10, 0)
        #Position properties
        
        vbox: # vbox arguments
            #text "Choose attack\nmethod:"
            
            imagebutton idle "systemPurple.png" hover "systemRed.png" action ShowMenu('save')
            textbutton "Attack 1" action None
            textbutton "Attack2" action None
            textbutton "CPanel" action Jump ("userControlPanel")