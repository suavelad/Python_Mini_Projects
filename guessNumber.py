#! usr/bin/python3

"""
This program takes the user's guess and compares it with the computer's guess.
The code continues to run until the user makes a right guess.
"""

from random import randint

def guesses ():
    try:
        
        user_guess = int(input("Guess a number between 0-99  >>"))
        computer_guess = randint(0, 99)

        if user_guess > computer_guess :
            print ("Computer's guess: %d and Your guess was: %d" %(computer_guess,user_guess))
            print(" Whoah!!! Your guess is too HIGH.")
            print("       ")
            guesses()

        
        elif user_guess < computer_guess :
            print("Computer's guess: %d and Your guess was: %d" %(computer_guess,user_guess))
            print(" Whoah!!! Your guess is too LOW." )
            print("       ")
            guesses()

        elif user_guess == computer_guess :
            print ("Computer's guess: %d and Your guess was: %d" %(computer_guess,user_guess))
            print("       ")
            print(" Yeee!!! Your guess was RIGHT.")
            print("       ")
            response= input("Do you want to play again? y or n >> ")
            if (response == "y"):
                print("       ")
                guesses()

            else :
                print("I hope you enjoyed yourself?")
                print("       ")
                exit
       
           
        else:
            print(" Your input is not an integer")
            print("       ")
            guesses()

    except (NameError, SyntaxError ):
            print(" Your input is invalid")
            print("       ")
            guesses()




guesses()