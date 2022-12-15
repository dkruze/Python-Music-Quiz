#File: Final Project Function 4
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

def hiphopfunction():
    score = 1
    hhq1 = str(input(" Since you like Hip-Hop music, who sucks the worst from this list?\n 1) Machine Gun Kelly\n 2) Hopsin\n 3) Logic\n 4) Macklemore\n 5) Fred Durst\n 6) Kid Cudi\n"))
    hhloop1 = True
    while hhloop1:
        if hhq1 == "6" or hhq1 == "5":
            score += 1
            hhloop1 = False
        elif hhq1 == "1" or hhq1 == "3":
            score += 3
            hhloop1 = False
        elif hhq1 == "4" or hhq1 == "2":
            score += 2
            hhloop1 = False
        elif hhq1.lower() == "end" or hhq1.lower() == "stop" or hhq1.lower() == "quit":
            death()
            break
        elif hhq1.lower() == "help":
            assist()
            hhq1 = str(input("Please select an answer.\n"))
        else:
            hhq1 = str(input("Please pick from the options provided.\n"))
    hhq2 = str(input(" Which of these collectives do you like the best?\n 1) Public Enemy\n 2) OFWGKTA\n 3) Run DMC\n 4) NWA\n 5) Three6 Mafia\n 6) Brockhampton\n"))
    hhloop2 = True
    while hhloop2:
        if hhq2 == "1" or hhq2 == "2":
            score += 2
            hhloop2 = False
        elif hhq2 == "3" or hhq2 == "4":
            score += 3
            hhloop2 = False
        elif hhq2 == "6":
            score += 1
            hhloop2 = False
        elif hhq2 == "5":
            score += 4
            hhloop2 = False
        elif hhq2.lower() == "end" or hhq2.lower() == "stop" or hhq2.lower() == "quit":
            death()
            break
        elif hhq2.lower() == "help":
            assist()
            hhq2 = str(input("Please select an answer.\n"))
        else:
            hhq2 = str(input("Please pick from the options provided.\n"))
    hhq3 = str(input(" Which of these younger MCs do you think is best?\n 1) Lil Durk\n 2) Lil Baby\n 3) DaBaby\n 4) Megan Thee Stallion\n 5) Travis Scott\n 6) Playboi Carti\n"))
    hhloop3 = True
    while hhloop3:
        if hhq3 == "2" or hhq3 == "6":
            score += 2
            hhloop3 = False
        elif hhq3 == "5" or hhq3 == "3":
            score += 3
            hhloop3 = False
        elif hhq3 == "4" or hhq3 == "1":
            score += 1
            hhloop3 = False
        elif hhq3.lower() == "end" or hhq3.lower() == "stop" or hhq3.lower() == "quit":
            death()
            break
        elif hhq3.lower() == "help":
            assist()
            hhq3 = str(input("Please select an answer.\n"))
        else:
            hhq3 = str(input("Please pick from the options provided.\n"))
    hhq4 = str(input(" Somebody asks you to put on a crowd pleaser. Who do you pick?\n 1) Kanye West\n 2) Cardi B\n 3) Ice T\n 4) Snoop Dogg\n 5) Ludacris\n 6) Jay-Z\n"))
    hhloop4 = True
    while hhloop4:
        if hhq4 == "4" or hhq4 == "6":
            score += 2
            hhloop4 = False
        elif hhq4 == "1" or hhq4 == "5" or hhq4 == "3":
            score += 3
            hhloop4 = False
        elif hhq4 == "2":
            score += 1
            hhloop4 = False
        elif hhq4.lower() == "end" or hhq4.lower() == "stop" or hhq4.lower() == "quit":
            death()
            break
        elif hhq4.lower() == "help":
            assist()
            hhq4 = str(input("Please select an answer.\n"))
        else:
            hhq4 = str(input("Please pick from the options provided.\n"))
    hhq5 = str(input(" What's closest to your go-to for extreme hip-hop?\n 1) Body Count\n 2) Death Grips\n 3) Run the Jewels\n 4) Eminem\n 5) Immortal Technique\n 6) Denzel Curry\n"))
    hhloop5 = True
    while hhloop5:
        if hhq5 == "2" or hhq5 == "1":
            score += 3
            hhloop5 = False
        elif hhq5 == "4" or hhq5 == "5":
            score += 1
            hhloop5 = False
        elif hhq5 == "3" or hhq5 == "6":
            score += 2
            hhloop5 = False
        elif hhq5.lower() == "end" or hhq5.lower() == "stop" or hhq5.lower() == "quit":
            death()
            break
        elif hhq5.lower() == "help":
            assist()
            hhq5 = str(input("Please select an answer.\n"))
        else:
            hhq5 = str(input("Please pick from the options provided.\n"))
    if score <= 9:
        score = "Trash"
    elif score >= 10 and score <=13:
        score = "Not Bad"
    elif score > 14:
        score = "Let's Gooooo"
    print("Your Taste: {}" .format(score))
    exit()
