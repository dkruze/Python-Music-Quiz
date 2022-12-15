#File: Final Project Main
#Author: Daniel Kruze
#Date: Nov 24 2021

from sys import exit
from popfunction import *
from rockfunction import *
from metalfunction import *
from hiphopfunction import *
from electrofunction import *
from countryfunction import *

def assist():
    print(" For this generator, you will first select the music genre you're interested in for today.\n This will provide you with a brief quiz of 5 or 6 questions concerning that genre, and based on your answers you will be provided an estimated taste assessment.\n For each quiz, please provide for an answer the number associated with the answer choice you want to select.\n From this menu, you may quit at any time and run the program again by typing 'main()' into the command line and pressing the ENTER key.\n When you are finished, if you would like to see another genre, simply type 'main()' into the command line and hit the ENTER key.\n Happy quizzing!\n")
    main()

def kitty():
    print("             |\     _,,,---,,_  ")
    print(" ZZzzz   /,`.-'`'    -.   ;-;;;-, __")
    print("           | ,4- _) )-,_. ,\  (  ` ''--' ")
    print("        ---'---'' (_/--'  `-'\_)\n ")
    main()

def main():
    print(" Please select a genre:")
    options = str(input(" Pop\n Rock\n Metal\n Hip Hop\n Electronic\n Country\n If you'd like detailed instructions, ask for 'help'\n Or, if you'd like to see a kitty cat, ask for 'kitty'\n"))
    loop = True
    while loop:
        if options.lower() == "pop":
            popfunction()
            break
        elif options.lower() == "rock":
            rockfunction()
            break
        elif options.lower() == "metal":
            metalfunction()
            break
        elif options.lower() == "hip hop":
            hiphopfunction()
            break
        elif options.lower() == "electronic":
            electrofunction()
            break
        elif options.lower() == "country":
            countryfunction()
            break
        elif options.lower() == "help":
            assist()
            break
        elif options.lower() == "kitty":
            kitty()
            break
        elif options.lower() == "end" or options.lower() == "stop" or options.lower() == "quit" or options.lower() == "exit" or options.lower() == "back" or options.lower() == "done" or options.lower() == "leave":
            print(" See you next time!\n")
            exit()
        else:
            options = str(input("Please pick from the options provided. And check your spelling, I'm not that good at coding. Yet.\n"))

print(" Welcome to the Music Taste Generator 2021!\n Written and coded by Daniel Kruze, the foremost arbiter of musical thought in the modern age.\n\n Or so he says.\n")
main()
