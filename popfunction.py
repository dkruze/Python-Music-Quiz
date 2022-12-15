#File: Final Project Function 1
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

def popfunction():
    score = 1
    pq1 = str(input(" Since you like pop music, which decade do you prefer?\n 1) 60s or Older\n 2) 70s\n 3) 80s\n 4) 90s\n 5) 00s\n 6) 10s to Today\n"))
    ploop1 = True
    while ploop1:
        if pq1 == "1" or pq1 == "4":
            score += 1
            ploop1 = False
        elif pq1 == "2" or pq1 == "3":
            score += 3
            ploop1 = False
        elif pq1 == "5" or pq1 == "6":
            score += 2
            ploop1 = False
        elif pq1.lower() == "end" or pq1.lower() == "stop" or pq1.lower() == "quit":
            death()
            break
        elif pq1.lower() == "help":
            assist()
            pq1 = str(input("Please select an answer.\n"))
        else:
            pq1 = str(input("Please pick from the options provided.\n"))
    pq2 = str(input(" Who would you sooner recognize as the King of Pop?\n 1) Michael Jackson\n 2) Prince\n 3) Peter Gabriel\n 4) Ed Sheeran\n 5) David Bowie\n 6) Adam Levine\n"))
    ploop2 = True
    while ploop2:
        if pq2 == "1" or pq2 == "2":
            score += 2
            ploop2 = False
        elif pq2 == "5" or pq2 == "3":
            score += 3
            ploop2 = False
        elif pq2 == "4" or pq2 == "6":
            score += 1
            ploop2 = False
        elif pq2.lower() == "end" or pq2.lower() == "stop" or pq2.lower() == "quit":
            death()
            break
        elif pq2.lower() == "help":
            assist()
            pq2 = str(input("Please select an answer.\n"))
        else:
            pq2 = str(input("Please pick from the options provided.\n"))
    pq3 = str(input(" Who would you sooner recognize as the Queen of Pop?\n 1) Björk\n 2) Lady Gaga\n 3) Kate Bush\n 4) Charli XCX\n 5) Madonna\n 6) Beyoncé Knowles\n"))
    ploop3 = True
    while ploop3:
        if pq3 == "2" or pq3 == "5":
            score += 2
            ploop3 = False
        elif pq3 == "1" or pq3 == "3":
            score += 3
            ploop3 = False
        elif pq3 == "4" or pq3 == "6":
            score += 1
            ploop3 = False
        elif pq3.lower() == "end" or pq3.lower() == "stop" or pq3.lower() == "quit":
            death()
            break
        elif pq3.lower() == "help":
            assist()
            pq3 = str(input("Please select an answer.\n"))
        else:
            pq3 = str(input("Please pick from the options provided.\n"))
    pq4 = str(input(" Somebody asks you to put on a crowd pleaser. Who do you pick?\n 1) Talking Heads\n 2) ABBA\n 3) T Pain\n 4) Taylor Swift\n 5) Amy Winehouse\n 6) Phil Collins\n"))
    ploop4 = True
    while ploop4:
        if pq4 == "3" or pq4 == "5":
            score += 2
            ploop4 = False
        elif pq4 == "1" or pq4 == "2":
            score += 3
            ploop4 = False
        elif pq4 == "4" or pq4 == "6":
            score += 1
            ploop4 = False
        elif pq4.lower() == "end" or pq4.lower() == "stop" or pq4.lower() == "quit":
            death()
            break
        elif pq4.lower() == "help":
            assist()
            pq4 = str(input("Please select an answer.\n"))
        else:
            pq4 = str(input("Please pick from the options provided.\n"))
    pq5 = str(input(" You've just been broken up with. What album keeps you bound to this mortal coil?\n 1) Red\n 2) Heaven or Las Vegas\n 3) Jagged Little Pill\n 4) SOUR\n 5) Third Eye Blind\n 6) The Queen is Dead\n"))
    ploop5 = True
    while ploop5:
        if pq5 == "2" or pq5 == "6":
            score += 3
            ploop5 = False
        elif pq5 == "1" or pq5 == "4" or pq5 == "5":
            score += 1
            ploop5 = False
        elif pq5 == "3":
            score += 2
            ploop5 = False
        elif pq5.lower() == "end" or pq5.lower() == "stop" or pq5.lower() == "quit":
            death()
            break
        elif pq5.lower() == "help":
            assist()
            pq5 = str(input("Please select an answer.\n"))
        else:
            pq5 = str(input("Please pick from the options provided.\n"))
    if score <= 9:
        score = "Garbage"
    elif score >= 10 and score <=13:
        score = "Normal"
    elif score > 13:
        score = "Refined"
    print("Your Taste: {}" .format(score))
    exit()
