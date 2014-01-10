###==========###
# Images 

# Images for avatar Character Object
image Cybele = "data/images/systemBlue.png"
image Tara = "data/images/systemGreen.png"

# Images for avatar's partner Character Object

# Side Images
image side Cybele = "data/images/systemBlue.png"
image side Cybele Happy = "data/images/systemRed.png"

image side Tara = "data/images/systemGreen.png"

image side Avatar = ConditionSwitch("World.avatar.name == 'Tara' ", "Tara",
    "True", "Cybele")

image side AvatarPartner = ConditionSwitch("World.avatar.partner.name == 'Tara' ", "Tara",
    "True", "Cybele")

###==========###

#Character Objects
define avatar = Character(World.avatar.name, image="Avatar", window_left_padding=150)
define avatarPartner = Character(World.avatar.name, image="AvatarPartner", window_left_padding=150)
define cybele = Character(Cybele.name, image="Cybele", window_left_padding=150)
define tara = Character(Tara.name, image="Tara", window_left_padding=150)

###==========###

label start:
    show screen attackScreen
    #show screen volume_controls
    cybele "So this is Crete.\nWhat a intresting place..."
    python:
        z = World.avatar.affections.values()
        t = Tara.affections.values()
        
    cybele "[z]"
    tara "Hello there!"
    cybele "Hello?"
    tara "Hi my name is Tara.\nNice to meet you. [t]"
    cybele "Nice to meet you to. My name is Cybele."
    tara "Would you like a tour of Crete Cybele?"
    cybele Happy "Absolutely!"
    tara "After the tour we can play in the tournament."
    tara "Okay. First let's team up."
    python:
        Cybele.addPartner(Tara)
    tara "Okay. My new partner is [Tara.partner.name]."
    
    jump firstTimeUser