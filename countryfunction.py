#File: Final Project Function 6
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

def countryfunction():
    score = 1
    cq1 = str(input(" Since you like country music, how do you feel about the state of country today?\n 1) Irredeemable. Trash, in fact\n 2) Perfectly Fine\n 3) Better than Ever\n 4) Losing its Edge\n 5) Better than it was a decade ago, that's for sure\n 6) Who Really Cares?\n"))
    cloop1 = True
    while cloop1:
        if cq1 == "4" or cq1 == "5" or cq1 == "6":
            score += 3
            cloop1 = False
        elif cq1 == "1" or cq1 == "2" or cq1 == "3":
            score += 2
            cloop1 = False
        elif cq1.lower() == "end" or cq1.lower() == "stop" or cq1.lower() == "quit":
            death()
            break
        elif cq1.lower() == "help":
            assist()
            cq1 = str(input("Please select an answer.\n"))
        else:
            cq1 = str(input("Please pick from the options provided.\n"))
    cq2 = str(input(" Who among these choices is the funniest?\n 1) David Allan Coe\n 2) Wheeler Walker Jr.\n 3) Jerry Reed\n 4) C.W. McCall\n 5) Rodney Carrington\n 6) Father John Misty\n"))
    cloop2 = True
    while cloop2:
        if cq2 == "1" or cq2 == "2":
            score += 3
            cloop2 = False
        elif cq2 == "4" or cq2 == "3" or cq2 == "6":
            score += 2
            cloop2 = False
        elif cq2 == "5":
            score += 1
            cloop2 = False
        elif cq2.lower() == "end" or cq2.lower() == "stop" or cq2.lower() == "quit":
            death()
            break
        elif cq2.lower() == "help":
            assist()
            cq2 = str(input("Please select an answer.\n"))
        else:
            cq2 = str(input("Please pick from the options provided.\n"))
    cq3 = str(input(" You're in your garage at midday and the only thing on the day's itinerary is beer. Who are you listening to?\n 1) Zac Brown Band\n 2) Waylon Jennings\n 3) Willie Nelson\n 4) Tim McGraw\n 5) Faith Hill\n 6) Kenny Chesney\n"))
    cloop3 = True
    while cloop3:
        if cq3 == "3" or cq3 == "5":
            score += 2
            cloop3 = False
        elif cq3 == "2":
            score += 3
            cloop3 = False
        elif cq3 == "1" or cq3 == "4" or cq3 == "6":
            score += 1
            cloop3 = False
        elif cq3.lower() == "end" or cq3.lower() == "stop" or cq3.lower() == "quit":
            death()
            break
        elif cq3.lower() == "help":
            assist()
            cq3 = str(input("Please select an answer.\n"))
        else:
            cq3 = str(input("Please pick from the options provided.\n"))
    cq4 = str(input(" Somebody asks you to put on a crowd pleaser. Who do you pick?\n 1) Keith Urban\n 2) Johnny Cash\n 3) Blake Shelton\n 4) Brad Paisley\n 5) Carrie Underwood\n 6) Hank Williams\n"))
    cloop4 = True
    while cloop4:
        if cq4 == "2" or cq4 == "4" or cq4 == "5":
            score += 2
            cloop4 = False
        elif cq4 == "6":
            score += 3
            cloop4 = False
        elif cq4 == "1" or cq4 == "3":
            score += 1
            cloop4 = False
        elif cq4.lower() == "end" or cq4.lower() == "stop" or cq4.lower() == "quit":
            death()
            break
        elif cq4.lower() == "help":
            assist()
            cq4 = str(input("Please select an answer.\n"))
        else:
            cq4 = str(input("Please pick from the options provided.\n"))
    cq5 = str(input(" You need a hype record; what do you pick?\n 1) Cowboys from Hell\n 2) Tennessee Whiskey\n 3) Leh-Nerd Skin-Nerd\n 4) Gunfighter Ballads\n 5) The Outlaws\n 6) The Great Pretender\n"))
    cloop5 = True
    while cloop5:
        if cq5 == "1" or cq5 == "2":
            score += 3
            cloop5 = False
        elif cq5 == "3" or cq5 == "4":
            score += 1
            cloop5 = False
        elif cq5 == "5" or cq5 == "6":
            score += 2
            cloop5 = False
        elif cq5.lower() == "end" or cq5.lower() == "stop" or cq5.lower() == "quit":
            death()
            break
        elif cq5.lower() == "help":
            assist()
            cq5 = str(input("Please select an answer.\n"))
        else:
            cq5 = str(input("Please pick from the options provided.\n"))
    if score <= 10:
        score = "Not Tryin'"
    elif score >= 11 and score <=13:
        score = "Perfectly Good"
    elif score > 13:
        score = "Bitchin'"
    print("Your Taste: {}" .format(score))
    exit()
