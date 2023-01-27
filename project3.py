########
#import modules
#######
## this game is called "bully"
## you are at a school that is in the shape of a square, with a courtyard in the middle and classrooms and clubs in the hallways.
## the plot of this game is that a guy asks you to do his homework, and you need to go around to the yard and some clubs to eventually figure out that you can print it from the computer lab and pick it up in the printer room. 
## global variables: the hw variable is used to track your progress, so you can't go directly to the printer room. for it to update properly, you need to go to every room required in the correct order. 
########
#define functions
#######
def start():
    print("Welcome! this tall buff dude is having trouble with his homework, and wants to meet with you. you can find him in the \nbathroom.")
    ahallway()

def ahallway():
    print("You are in a hallway")
    move = input("\nWhere would you like to go? Say one of these choices:\n\tyard\n\tbathroom\n\tb hallway\n\tc hallway\n\t")
    if move.lower() == "yard":
        yard()
    elif move.lower() == "bathroom":
        bathroom()
    elif move.lower() == "b hallway":
        bhallway()
    elif move.lower() == "c hallway":
        challway()
    else:
        print("you decide you have no life and go cry in the corner alone")
        ahallway()

def yard():
    print("You are in the yard. you see some guy who's probably on every drug he can get his hands on. you are afraid of him.")
    global hw
    if hw == "yard":
        print("you talk to the guy. he tells you that the lgbtq kids in d hallway might be able to help")
        hw = "lgbtq"
    move = input("\nWhere would you like to go? Say one of these choices:\n\ta hallway\n\tb hallway\n\tc hallway\n\td hallway\n\t")
    if move.lower() == "a hallway":
        ahallway()
    elif move.lower() == "b hallway":
        bhallway()
    elif move.lower() == "c hallway":
        challway()
    elif move.lower() == "d hallway":
        dhallway()
    else:
        yard()


def bathroom():
    global hw
    print("You are in the bathroom. you see a tall buff dude. he walks up to you and says, 'hey man, i really need some help. can you do my math homework for me?")
    step1 = input("do you say yes?")
    if step1.lower() == "yes":
        print("the guy says 'thanks bro. i know i can always count on you. i think someone in the yard can help you out.'")
        hw = "yard"
    elif step1.lower() == "no":
        print("lmao u got beat up")

    move = input("\nWhere would you like to go? Say one of these choices:\n\ta hallway\n")
    if move.lower() == "a hallway":
        ahallway()
    else:
        print("lmao u got beat up")
    

def bhallway():
    print("you are in b hallway. ")
    move = input("where would you like to go? \n\tprinter room\n\ta hallway\n\td hallway\n\tyard\n\t")
    if move.lower() == "printer room":
        printerroom()
    elif move.lower() == "a hallway":
        ahallway()
    elif move.lower() == "d hallway":
        dhallway()
    elif move.lower() == "yard":
        yard()
    else:
        bhallway()

def challway():
    print("you are in c hallway. ")
    move = input("where would you like to go? \n\tcomputer lab\n\ta hallway\n\td hallway\n\tyard\n\t")
    if move.lower() == "computer lab":
        computerlab()
    elif move.lower() == "a hallway":
        ahallway()
    elif move.lower() == "d hallway":
        dhallway()
    elif move.lower() == "yard":
        yard()
    else:
        challway()

def dhallway():
    print("you are in d hallway. ")
    move = input("where would you like to go? \n\tnerd club\n\tlgbtq club\n\tb hallway\n\tc hallway\n\t")
    if move.lower() == "nerd club":
        nerdclub()
    elif move.lower() == "lgbtq club":
        lgbtqclub()
    elif move.lower() == "b hallway":
        bhallway()
    elif move.lower() == "c hallway":
        challway()
    else: 
        dhallway()

def printerroom():
    global hw
    print("you are in the printer room")
    if hw == "printerroom":
        get = input(print("would you like to pickup the homework? yes or no"))
        if get.lower() == "yes":
            print("you pickup the homework and give it to the scary guy and everyone is happy.")
        elif get.lower() == "no":
            print("lmao you got beat up")
    else: 
        move = input("where would you like to go? \n\tb hallway\n\t")
        if move.lower() == "b hallway":
            bhallway()
def lgbtqclub():
    global hw
    print("welcome to lgbtq club! you notice everyone here has purple hair.")
    if hw == "lgbtq":
        print("you talk to some people there and they recommend that you see the nerds in nerd club")
        hw = "nerd"
    move = input("\nWhere would you like to go?\n\td hallway\n\t")
    if move.lower() == "d hallway":
        dhallway()
    else: 
        dhallway()
def nerdclub():
    global hw
    print("welcome to nerd club! everyone in here has glasses.")
    if hw == "nerd":
        print("the guys in nerd club tell you to go to the computer lab to print out the homework.")
        hw = "computer"
    move = input("\nWhere would you like to go?\n\td hallway\n\t")
    if move.lower() == "d hallway":
        dhallway()
    else:
        dhallway()
def computerlab():
    global hw
    print("you are in the computer lab. there are lots of computers.")
    if hw == "computer":
        printe = input("would you like to print the homework? yes or no")
        if printe == "yes":
            print("you have printed the homework. now you can pick it up in the printer room")
            hw = "printerroom"
        elif printe == "no":
            print("lmao u got beat up")
    move = input("\nWhere would you like to go?\n\tc hallway\n\t")
    if move.lower() == "c hallway":
        challway()
    else:
        challway()

    

    


########
#main
#######
#TODO: Add some global variables
hw = "empty" 
start()