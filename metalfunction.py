#File: Final Project Function 3
#Author: Daniel Kruze
#Date: Nov 24 2021

#AUTHOR'S NOTE: All these functions, while similar in design, have different varaibles with shorthand for each function to enforce functionality.
#This shorthand pertains to each variable being either a loop or a question, with a number on the end to denote the question (in sequence per function) and a letter at the front to represent genre.
#For instance, in the "pop" function, the variable for the first question would be "pq1," short for "Pop Question Number 1," and so on.
#The hip-hop function is an exception, with two letters at the beginning, "hh," for consistency.
#Each function consists of questions and loops 1-5, with the exception of the metal function which is 1-6.

from sys import exit

def assist():
    print(" For this generator, you will first select the music genre you're interested in for today.\n This will provide you with a brief quiz of 5 or 6 questions concerning that genre, and based on your answers you will be provided an estimated taste assessment.\n For each quiz, please provide for an answer the number associated with the answer choice you want to select.\n From this menu, you may quit at any time (quit, stop, or end) and run the program again by typing 'main()' into the command line and pressing the ENTER key.\n When you are finished, if you would like to see another genre, simply type 'main()' into the command line and hit the ENTER key.\n Happy quizzing!\n")
    
def death():
    exit()

def metalfunction():
    score = 1
    mq1 = str(input(" Since you like metal music, which subgenre do you most identify with?\n 1) Death\n 2) Black\n 3) Thrash\n 4) Doom\n 5) Progressive\n 6) Alt\n"))
    mloop1 = True
    while mloop1:
        if mq1 == "2" or mq1 == "5":
            score += 1
            mloop1 = False
        elif mq1 == "1" or mq1 == "3":
            score += 3
            mloop1 = False
        elif mq1 == "4" or mq1 == "6":
            score += 2
            mloop1 = False
        elif mq1.lower() == "end" or mq1.lower() == "stop" or mq1.lower() == "quit":
            death()
            break
        elif mq1.lower() == "help":
            assist()
            mq1 = str(input("Please select an answer.\n")) 
        else:
            mq1 = str(input("Please pick from the options provided.\n"))
    mq2 = str(input(" Who is the best frontman on this list?\n 1) Bruce Dickinson\n 2) Peter Steele\n 3) Dave Mustaine\n 4) Tom Angelripper\n 5) Quorthon\n 6) Dave Brockie\n"))
    mloop2 = True
    while mloop2:
        if mq2 == "3" or mq2 == "1":
            score += 2
            mloop2 = False
        elif mq2 == "2" or mq2 == "4":
            score += 3
            mloop2 = False
        elif mq2 == "5":
            score += 1
            mloop2 = False
        elif mq2 == "6":
            score += 4
            mloop2 = False
        elif mq2.lower() == "end" or mq2.lower() == "stop" or mq2.lower() == "quit":
            death()
            break
        elif mq2.lower() == "help":
            assist()
            mq2 = str(input("Please select an answer.\n")) 
        else:
            mq2 = str(input("Please pick from the options provided.\n"))
    mq3 = str(input(" Who invented Death Metal?\n 1) Death\n 2) Slayer\n 3) Master\n 4) Napalm Death\n 5) Deicide\n 6) Kreator\n"))
    mloop3 = True
    while mloop3:
        if mq3 == "1" or mq3 == "2":
            score += 2
            mloop3 = False
        elif mq3 == "4" or mq3 == "3":
            score += 3
            mloop3 = False
        elif mq3 == "5" or mq3 == "6":
            score += 1
            mloop3 = False
        elif mq3.lower() == "end" or mq3.lower() == "stop" or mq3.lower() == "quit":
            death()
            break
        elif mq3.lower() == "help":
            assist()
            mq3 = str(input("Please select an answer.\n")) 
        else:
            mq3 = str(input("Please pick from the options provided.\n"))
    mq4 = str(input(" Which of these do you consider the most essential listening?\n 1) Metallica\n 2) Sepultura\n 3) Bolt Thrower\n 4) Black Sabbath\n 5) Pantera\n 6) Mayhem\n"))
    mloop4 = True
    while mloop4:
        if mq4 == "3" or mq4 == "1":
            score += 2
            mloop4 = False
        elif mq4 == "4" or mq4 == "5":
            score += 3
            mloop4 = False
        elif mq4 == "2" or mq4 == "6":
            score += 1
            mloop4 = False
        elif mq4.lower() == "end" or mq4.lower() == "stop" or mq4.lower() == "quit":
            death()
            break
        elif mq4.lower() == "help":
            assist()
            mq4 = str(input("Please select an answer.\n")) 
        else:
            mq4 = str(input("Please pick from the options provided.\n"))
    mq5 = str(input(" Who do you think is the most underrated?\n 1) Cynic\n 2) Bell Witch\n 3) Blood Incantation\n 4) Malevolent Creation\n 5) Entombed\n 6) Primitive Man\n"))
    mloop5 = True
    while mloop5:
        if mq5 == "4" or mq5 == "5":
            score += 3
            mloop5 = False
        elif mq5 == "1" or mq5 == "6" or mq5 == "2" or mq5 == "3":
            score += 2
            mloop5 = False
        elif mq5.lower() == "end" or mq5.lower() == "stop" or mq5.lower() == "quit":
            death()
            break
        elif mq5.lower() == "help":
            assist()
            mq5 = str(input("Please select an answer.\n")) 
        else:
            mq5 = str(input("Please pick from the options provided.\n"))
    mq6 = str(input(" Which of these bands do you think is the most consistently good?\n 1) Testament\n 2) TOOL\n 3) Cannibal Corpse\n 4) Evile\n 5) Sodom\n 6) Ministry\n"))
    mloop6 = True
    while mloop6:
        if mq6 == "1" or mq6 == "4":
            score += 3
            mloop6 = False
        elif mq6 == "2" or mq6 == "3" or mq6 == "5":
            score += 2
            mloop6 = False
        elif mq6 == "6":
            score += 1
            mloop6 = False
        elif mq6.lower() == "end" or mq6.lower() == "stop" or mq6.lower() == "quit":
            death()
            break
        elif mq6.lower() == "help":
            assist()
            mq6 = str(input("Please select an answer.\n")) 
        else:
            mq6 = str(input("Please pick from the options provided.\n"))
    if score <= 10:
        score = "Scum"
    elif score >= 11 and score <=15:
        score = "Brutal"
    elif score > 15:
        score = "God of Violence"
    print("Your Taste: {}" .format(score))
    exit()



    
