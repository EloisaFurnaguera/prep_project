import sys
import random

print("----------Welcome to the Joke Game----------")
print()
print('Pick a number from the list to choose a game or press E" to exit or "H" to comeback to main menue')
print("1: Joke of the day")
print("2: Feeling lucky")
print("3: Knock knocks okes")
print("4: Random Joke")
print()

#------------------------------------------------------------------------------------
#Random joke game

jokes = {'A':['Today at the bank, an old lady asked me to help check her balance.', 'So I pushed her over.'], 'B':['I told my girlfriend she drew her eyebrows too high.', 'She seemed surprised.'], 'C':['I am so good at sleeping.','I can do it with my eyes closed.'], 'D':['Why is Peter Pan always flying?','He neverlands.']}


def joke_random():
    print("You have chosen the Random Joke game")
    print("We give you a setup and you have to pick the right punchline")
    #Ask the user to start the game and bringing a randome setup from the dict and stops if "E" by using sys.exit() and goes back to start menue by pressing "h"
    while True:
        user_joke = input('Press "Enter" to play or "E" to stop > ')  
        print()
        if user_joke.upper() == "E":
            sys.exit()
        elif user_joke.upper() == "H":
            start_nemu()
        user_joke = random_setup = random.choice(list(jokes))
        random_setup = jokes[user_joke][0]
        print("Joke setup:", random_setup.upper())
        print()
        print("Only one of these punch lines will work") 
        #print list of puchlines
        for key in jokes:
            print(key,":",jokes[key][1])
            
        #ask the user to choose from the puch, it loops until the right awnser is given and exits if "e" and "h" to go back to start menue
        while True:
            print()
            user_punch = input("Which punch line works for the setup? > ") 
            print() 
            user_punch = user_punch.upper()
            if user_punch == user_joke:
                print("Yay! That is right! the joke goes:")
                print(jokes[user_joke][0].upper(), jokes[user_joke][1].upper())
                print()
                print("You are funny!")
                break
            elif user_punch == "E":    
                print("Bye")
                break
            elif user_punch.upper() == "H":
                  start_nemu()  
            else:
                print("That is not right")    
 
#joke_random()

#------------------------------------------------------------------------------------

#Knock jokes: where they user jusk clicks and gets a random punchline

Knocks = ["Adore", "Amanda", "Amish"]

def knock_jokes():
    print( "You have chosen the Knocks Jokes Game")
    print("Let's have some fun whith some silly Knock, Knock jokes")
    print('if you had too much fun already press "E" to exit or "H" to retur to home')
    print()
 
    #A loop asking the user fo do a Knock Knock joke 
    while True:
        print("Knock, knock.")
        user1 = input("and you say? > ")
        user1 = user1.lower() 

        if user1 == "e":
            print ("Bye")
            sys.exit()
        elif user1 == "h":
            start_nemu()  
        
        # I used "in" in sted of "==" because we are using a list to chose from
        # elif user1 in ["who is there?", "who is there", "who's there?", "who's there","who?", "who"]:
        elif "who" in user1:
            random_knock = random.choice(Knocks)
            print(random_knock)
        #if the right user input the joke prints else it keeps looping  
            while True:

                user2 = input("and you say? > ")
                if user2 in ["adore who?","adore who"]:
                    print ("Adore is between us. Open up!")
                    print()
                    break

                elif user2 in ["amanda who?","amanda who"]:
                    print ("A man da fix your sink!") 
                    print()
                    break 

                elif user2 in ["amish who?","amish who"]:
                    print ("You're not a shoe!") 
                    print()
                    break
                elif user2 in ["H", "h"]:
                    start_nemu()

                else:
                    print("that is no right")    
        else:
            print ("Try angin")                
        
#knock_jokes()

#-----------------------------------------------------------------------------------
#Feeling lucky: the user picks a randon setup and a random punch line

lucky_setups = ["Did you hear about the restaurant on the moon?","What do you call a fake noodle?", "How many apples grow on a tree?","Want to hear a joke about paper?","Why did the coffee file a police report?","Dad, did you get a haircut?"]

lucky_puchlines = ["Great food, no atmosphere.","An Impasta.","All of them.","Nevermind it's tearable.", "It got mugged.", "No I got them all cut."]

def feeling_lucky ():
    print ("You have chosen the Feeling Lucky Game")
    print ()
    print ("Let's get crazy and play with random set ups and punch lines  > ")
    while True:
        user3 = input ('Press "Enter" to play or "H" for Home or "E" to exit > ')
        if user3.upper() == "H":
            start_nemu()
        print()
    #gets a random setup and a random puchline    
        random_setup = random.choice(lucky_setups)
        random_punch  = random.choice(lucky_puchlines)
        print (random_setup, random_punch)
        print()
    #Loop to continue with a random made up joke or go to main menu or exit
        user_liked = input("Was that a good joke? Y or N > ")
        print ()
        user_liked = user_liked.lower()
        if user_liked in ["y", "yes"]:
            print("Yay! You are a comedian")
        elif user_liked in ["n", "no"]:
            print("Oh no! do you what to try again?") 
        elif user_liked == "e":  
            sys.exit() 
        elif user_liked == "h":
            start_nemu()
        else:
            print("I dont understand. Try aging")    


#feeling_lucky ()

#-------------------------------------------------------------------------------------
#Joke of the day: Where the user gets a random full joke

day_jokes = ["How does a penguin build its house? Igloos it together.", "Dad, did you get a haircut? No I got them all cut.", "What do you call a Mexican who has lost his car? Carlos.", "Dad, can you put my shoes on? No, I don't think they'll fit me.", "Why did the scarecrow win an award? Because he was outstanding in his field.", "Why don't skeletons ever go trick or treating? Because they have no body to go with.", "Ill call you later. Don't call me later, call me Dad."]

def joke_of_the_day ():
    print('You have chosen: "Joke of the day"')
    print()
        #The user gets a random joke after pressing "enter" and it loops to main menue if "n"
    while True:
        input ('Press "Enter" and laugh! whith the joke of the day > ')
        joke = random.choice(day_jokes)
        print()
        print(joke.upper())
        print()
        user_input1 = input("Do you want another one? >")
        user_input1 = user_input1.upper() 
        print()
        if user_input1 == "N":
            start_nemu ()
        elif user_input1 == "E":
            print("Bye") 
            sys.exit()  
        elif user_input1 == "H":
            start_nemu()
        elif user_input1 != "Y":
            print("I dont understand.")
        

#------------------------------------------------------------------------------------
#Start nemu



def start_nemu ():
    while True:
        user_pick = input ("------------ What do you want to play now? > ")
        print()
        user_pick = user_pick.lower()
            
        if user_pick == "e":
            print("Bye")
            break
        if user_pick in ["n", "no"]:
            print("Bye")
            break
        elif user_pick =="1":
            joke_of_the_day()
        elif user_pick == "2":
            feeling_lucky ()
        elif user_pick == "3":
            knock_jokes()
        elif user_pick == "4":
            joke_random()
        else:
            print("I didn't understand. ")   

start_nemu()