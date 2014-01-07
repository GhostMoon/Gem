# User Control Panel 0.1
label firstTimeUser:
    avatarPartner "This will be where you can do most of your activities."
    avatarPartner "There is also a store, where you can buy new items."
    avatarPartner "Why don't you try it out?"
    avatarPartner "You don't have any Gems?"
    avatarPartner "Here. You can have some of mine."
     
    $ Cybele.updateGems(10000)
    avatar "You acquired 10,000 Gems!"
     
    avatarPartner "Now click on the shop's icon to enter the shop."
     
    #!!! TODO implement shop screen
    
label userControlPanel:
    avatar "Today's date is [World.date]."
    avatar "The Weather is [World.weather]."
    avatar "You carry [World.avatar.gems] Gems."
    $ World.avatar.removePartner()
    $ World.avatar.removePartner()
    if World.avatar.partner != None:
        avatar "Your partner's mood is [World.avatar.partner.mood]."
    avatar "What do you want to do?"
    
    return