from random import randint
t = ["rock","paper","scissors"]#create a list of play options
computer = t[randint(0,2)]#assign a random play to the computer
player = False#set player to False
while player == False:
#set player to True
    player = input("rock,paper,scissors?")
    if player == computer:
        print("Tie!")
    elif player=="rock":
        if computer=="paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player=="paper":
        if computer=="scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player=="scissors":
        if computer=="rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")
    #player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0,2)]

