"""
 Start Game:  Help the fox find his hole
 
"""



def gamestart(progress):
    start_text = """
    You're a fox who has been out foraging for food.
    You just found yourself a nice rabbit for dinner,
    but you've ventured out so far to find it!
    Which way did you go? Guess you'll have to find out.
    There's a large group of trees on your left and a swamp on your right.

    """
    forest_text = """
    You run into the forest clearing, you seem safe for now.
    Deeper into the forest, there's a trail of white fluff
    leading towards the mountains. Next to it are
    some peculiar looking mushrooms.
    """
    on_mushrooms = """
    You eat a mushroom, everything becomes colourful
    and the universe around you melts into a big, beautiful
    connected, interweaving painting.
    You felt just dandy! Also a new path opens up.
    """
    almost_home = """
    You take the path that you swear wasn't there before.
    You come across a lizard wizard, but the other path
    next to him is starting to feel familiar.
    """
    home_text = """
    You make it to your fox hole unscathed, rabbit in maw!
    Nice job, now you got dinner for a week.
    """
    global choice
    if progress == 0:
        print(start_text)
        select = input("Choose 't' for trees or 's' for swamp: ")
        if select == "t":
            choice = "tree"
            progress = 1
        elif select == "s":
            choice = "swamp"
        else:
            print("That was not a valid choice")
            
    elif progress == 1:
        print(forest_text)
        select = input("Choose 'f' to follow the fluff or 'm' to eat a mushroom.")
        if select == "f":
            choice = "fluff"
        elif select == "m":
            choice = "mushroom"
            progress = 2
        else:
            print("That was not a valid choice")
            
    elif progress == 2:
        print(on_mushrooms)
        select = input("'f' to follow the fluff, 'm' for another mushroom, or 'p' for the new path.")
        if select == "f":
            choice = "fluff"
        elif select == "m":
            choice = "second mushroom"
        elif select == "p":
            choice = "path"
            progress = 3
        else:
            print("That was not a valid choice")
            
    elif progress == 3:
        print(almost_home)
        select = input("Press 'w' to walk up to the wizard, or 'p' to take the familiar path.")
        if select == "w":
            choice = "wizard"
        elif select == "p":
            choice = "home"
            progress = 4
        else:
            print("That's not a valid choice")
    if progress == 4:
        print(home_text)
        choice = "win"
    
    
"""
    All death sequences/wrong choices
    """
def deathSeq(whichplace):
    deadSwamp = """
    You wander into the swamp, and quickly
    find yourself sinking! You struggle to
    get out but something from underneath the
    water grabs you... you died!
    """
    deadMountain = """
    You follow the trail of white fluff
    near the mountain. As you come to the
    cliffside, a large group of rabbits
    pop out of their hiding places; you're
    surrounded! They take one look at their
    brother, your dinner, dangling from your
    mouth and immediately avenge him.
    You died!
    """
    deadMushroom = """
    You ate a second mushroom.
    As it turns out, you can overdose.
    The sky opens up. For just a second,
    you can see the heavens in all their beauty.
    Then you died.
    """
    deadWizard = """
    You walk up the wizard.
    He zaps the rabbit in your mouth,
    the rabbit comes back to life as
    a grotesque creature.
    He attacks you, you died.
    """

    global lifenumber
    
    if whichplace == "swamp":
        print(deadSwamp)
        
        lifenumber -= 1
        print("You only have %d lives left!" % lifenumber)
        gamestart(0)
    if whichplace == "mountain":
        print(deadMountain)
        
        lifenumber -= 1
        print("You have %d socks" % sockcount)
        gamestart(0)
    if whichplace == "second mushroom":
        print(deadMushroom)
        lifenumber -= 1
        print("You only have %d lives left!" % lifenumber)
        gamestart(0)
    if whichplace == "wizard":
        print(deadWizard)
        lifenumber -= 1
        print("You only have %d lives left!" % lifenumber)
        gamestart(0)
    if whichplace == "fluff":
        print(deadMountain)
        lifenumber -= 1
        print("You only have %d lives left!" % lifenumber)
        gamestart(0)

""" partly open door to hallway
    escape into hallway  choices
    down hallway   or go right
    """
def hallway():
    hallway_text = """
    Hallway:
    You run into the forest clearing, you seem safe for now.
    Deeper into the forest, there's a trail of white fluff
    leading towards the mountains. Next to it are
    some peculiar looking mushrooms.
    """
    print(hallway_text)
    global choice
    select = input(" 'f' for white fluff, or 'm' for mushrooms: ")
    if select == "f":
        choice = "rabbits"
    elif select == "r":
        choice =  "tobathroom"
    else:
        print("That is not a valid choice")
        hallway()
        
    
"""
    go right :  Find bathroom
    choices:  steal toilet paper     or  hole in wall behind sink cabinet
    """

"""
    downhallway: Find workshop
    choices:  Attack snake   or  go under workbench
    """


"""
    Main Game Loop
    """
keepgoing = True
totallives = 5
lifenumber = 5
choice = "start"
sockcount = 0

while keepgoing:
    if choice == "win":
        keepgoing = False
    else:
        print("You chose:", choice)
        if lifenumber > 0 :
            if choice == "start":
                gamestart(0)
            elif choice == "tree":
                gamestart(1)
            elif choice == "mushroom":
                gamestart(2)
            elif choice == "path":
                gamestart(3)
            elif choice == "home":
                gamestart(4)
            elif choice == "swamp" or choice == "fluff" or choice == "second mushroom" or choice == "wizard":
                deathSeq(choice)
            
        else:
             print("Sorry, foxes don't have 9 lives, only 5.")
             keepgoing = False
newMe = input("Type anything to end the script.")
while newMe != "anything":
    newMe = input("I said type anything, not " + newMe + "!")


    

