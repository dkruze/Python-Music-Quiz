#File: Final Project Function 5
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

def electrofunction():
    score = 1
    eq1 = str(input(" Since you like electronic music, what subgenre would you most identify with?\n 1) House\n 2) Electronica\n 3) Chiptune\n 4) Synthprog\n 5) Electroambient\n 6) Hyperpop\n"))
    eloop1 = True
    while eloop1:
        if eq1 == "2" or eq1 == "5":
            score += 3
            eloop1 = False
        elif eq1 == "1" or eq1 == "3" or eq1 == "4" or eq1 == "6":
            score += 2
            eloop1 = False
        elif eq1.lower() == "end" or eq1.lower() == "stop" or eq1.lower() == "quit":
            death()
            break
        elif eq1.lower() == "help":
            assist()
            eq1 = str(input("Please select an answer.\n"))
        else:
            eq1 = str(input("Please pick from the options provided.\n"))
    eq2 = str(input(" If someone asked you 'who invented electronic music?' who would you say?\n 1) Richard D James\n 2) Daft Punk\n 3) Genesis\n 4) Laurie Spiegel\n 5) Kraftwerk\n 6) Ryuichi Sakamoto\n"))
    eloop2 = True
    while eloop2:
        if eq2 == "1" or eq2 == "5":
            score += 2
            eloop2 = False
        elif eq2 == "4" or eq2 == "6":
            score += 3
            eloop2 = False
        elif eq2 == "3" or eq2 == "2":
            score += 1
            eloop2 = False
        elif eq2.lower() == "end" or eq2.lower() == "stop" or eq2.lower() == "quit":
            death()
            break
        elif eq2.lower() == "help":
            assist()
            eq2 = str(input("Please select an answer.\n"))
        else:
            eq2 = str(input("Please pick from the options provided.\n"))
    eq3 = str(input(" From the given list, pick your preferred record (given in the form [artist] - [album]):\n 1) JUSTICE - Cross\n 2) Kanye West - 808s and Heartbreaks\n 3) 100 gecs - 1000 gecs\n 4) Oneohtrix Point Never - Replica\n 5) New Order - Power, Corruption, and Lies\n 6) Who are any of these people?\n"))
    eloop3 = True
    while eloop3:
        if eq3 == "2" or eq3 == "1" or eq3 == "5":
            score += 2
            eloop3 = False
        elif eq3 == "4" or eq3 == "3":
            score += 3
            eloop3 = False
        elif eq3 == "6":
            score += 1
            eloop3 = False
        elif eq3lower() == "end" or eq3.lower() == "stop" or eq3.lower() == "quit":
            death()
            break
        elif eq3.lower() == "help":
            assist()
            eq3 = str(input("Please select an answer.\n"))
        else:
            eq3 = str(input("Please pick from the options provided.\n"))
    eq4 = str(input(" Somebody asks you to put on a crowd pleaser. Who do you pick?\n 1) Joy Division\n 2) Daft Punk\n 3) Aphex Twin\n 4) DEVO\n 5) The Weeknd\n 6) SOPHIE\n"))
    eloop4 = True
    while eloop4:
        if eq4 == "6" or eq4 == "1":
            score += 2
            eloop4 = False
        elif eq4 == "2" or eq4 == "4":
            score += 3
            eloop4 = False
        elif eq4 == "3" or eq4 == "5":
            score += 1
            eloop4 = False
        elif eq4.lower() == "end" or eq4.lower() == "stop" or eq4.lower() == "quit":
            death()
            break
        elif eq4.lower() == "help":
            assist()
            eq4 = str(input("Please select an answer.\n"))
        else:
            eq4 = str(input("Please pick from the options provided.\n"))
    eq5 = str(input(" Which of these artists is furthest from your repertoire?\n 1) The Human League\n 2) Deadmau5\n 3) Charli XCX\n 4) Burial\n 5) Skrillex\n 6) The Chemical Brothers\n"))
    eloop5 = True
    while eloop5:
        if eq5 == "5" or eq5 == "2":
            score += 3
            eloop5 = False
        elif eq5 == "1" or eq5 == "3":
            score += 1
            eloop5 = False
        elif eq5 == "4" or eq5 == "6":
            score += 2
            eloop5 = False
        elif eq5.lower() == "end" or eq5.lower() == "stop" or eq5.lower() == "quit":
            death()
            break
        elif eq5.lower() == "help":
            assist()
            eq5 = str(input("Please select an answer.\n"))
        else:
            eq5 = str(input("Please pick from the options provided.\n"))
    if score <= 10:
        score = "Pleb"
    elif score >= 11 and score <=13:
        score = "Normie"
    elif score > 13:
        score = "400 IQ"
    print("Your Taste: {}" .format(score))
    exit()
