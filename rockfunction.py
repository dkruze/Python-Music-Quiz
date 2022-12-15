#File: Final Project Function 2
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

def rockfunction():
    score = 1
    rq1 = str(input(" Since you like rock music, which decade do you prefer?\n 1) 60s or Older\n 2) 70s\n 3) 80s\n 4) 90s\n 5) 00s\n 6) 10s to Today\n"))
    rloop1 = True
    while rloop1:
        if rq1 == "5" or rq1 == "6":
            score += 1
            rloop1 = False
        elif rq1 == "2" or rq1 == "3" or rq1 == "4":
            score += 3
            rloop1 = False
        elif rq1 == "1":
            score += 2
            rloop1 = False
        elif rq1.lower() == "end" or rq1.lower() == "stop" or rq1.lower() == "quit":
            death()
            break
        elif rq1.lower() == "help":
            assist()
            rq1 = str(input("Please select an answer.\n"))
        else:
            rq1 = str(input("Please pick from the options provided.\n"))
    rq2 = str(input(" Who is the best guitar player on this list?\n 1) Johnny Greenwood\n 2) Jack White\n 3) Tom Morello\n 4) Steve Vai\n 5) Yngwie Malmsteen\n 6) Jimi Hendrix\n"))
    rloop2 = True
    while rloop2:
        if rq2 == "2" or rq2 == "3":
            score += 2
            rloop2 = False
        elif rq2 == "1" or rq2 == "6":
            score += 3
            rloop2 = False
        elif rq2 == "4" or rq2 == "5":
            score += 1
            rloop2 = False
        elif rq2.lower() == "end" or rq2.lower() == "stop" or rq2.lower() == "quit":
            death()
            break
        elif rq2.lower() == "help":
            assist()
            rq2 = str(input("Please select an answer.\n"))
        else:
            rq2 = str(input("Please pick from the options provided.\n"))
    rq3 = str(input(" Which of these bands do you think has the most consistently good discography?\n 1) The Police\n 2) Coldplay\n 3) Sublime\n 4) MGMT\n 5) R.E.M.\n 6) Led Zeppelin\n"))
    rloop3 = True
    while rloop3:
        if rq3 == "2" or rq3 == "4":
            score += 2
            rloop3 = False
        elif rq3 == "1" or rq3 == "5":
            score += 3
            rloop3 = False
        elif rq3 == "3" or rq3 == "6":
            score += 1
            rloop3 = False
        elif rq3.lower() == "end" or rq3.lower() == "stop" or rq3.lower() == "quit":
            death()
            break
        elif rq3.lower() == "help":
            assist()
            rq3 = str(input("Please select an answer.\n"))
        else:
            rq3 = str(input("Please pick from the options provided.\n"))
    rq4 = str(input(" Somebody asks you to put on a crowd pleaser. Who do you pick?\n 1) Radiohead\n 2) Aerosmith\n 3) Guns N' Roses\n 4) Alice in Chains\n 5) Red Hot Chili Peppers\n 6) Queen\n"))
    rloop4 = True
    while rloop4:
        if rq4 == "2" or rq4 == "5" or rq4 == "6":
            score += 2
            rloop4 = False
        elif rq4 == "1" or rq4 == "4":
            score += 3
            rloop4 = False
        elif rq4 == "3":
            score += 1
            rloop4 = False
        elif rq4.lower() == "end" or rq4.lower() == "stop" or rq4.lower() == "quit":
            death()
            break
        elif rq4.lower() == "help":
            assist()
            rq4 = str(input("Please select an answer.\n"))
        else:
            rq4 = str(input("Please pick from the options provided.\n"))
    rq5 = str(input(" Who do you think has the most trustworthy political senses?\n 1) Rage Against the Machine\n 2) Fugazi\n 3) Ween\n 4) Nirvana\n 5) ZZ Top\n 6) The Grateful Dead\n"))
    rloop5 = True
    while rloop5:
        if rq5 == "2" or rq5 == "3":
            score += 3
            rloop5 = False
        elif rq5 == "1" or rq5 == "4":
            score += 1
            rloop5 = False
        elif rq5 == "6" or rq5 == "5":
            score += 2
            rloop5 = False
        elif rq5.lower() == "end" or rq5.lower() == "stop" or rq5.lower() == "quit":
            death()
            break
        elif rq5.lower() == "help":
            assist()
            rq5 = str(input("Please select an answer.\n"))
        else:
            rq5 = str(input("Please pick from the options provided.\n"))
    if score <= 9:
        score = "Needs Work"
    elif score >= 10 and score <=13:
        score = "Average"
    elif score > 13:
        score = "Badass"
    print("Your Taste: {}" .format(score))
    exit()
