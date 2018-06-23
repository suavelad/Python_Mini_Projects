#! usr/bin/python3
"""
This program prints out a random quote for the user
"""
from random import choice


Quotes=["Make hay while the sun shines","Be Wise",
        " Seeth a man diligent,he will serve before kings and not ordinary men",
        "Hard work pays","Be Educative"]


ResponseA= input("Do you want to get today's quote?  y or n  >> " ).lower()

if ResponseA=="y":
    quoteA= choice(Quotes)
    print(" ")
    print("**********************************************")
    print(quoteA)
    print("**********************************************")
    print(" ")
    ResponseB = input("Do you want more quotes? y or n >>").lower()
    if ResponseB=="y":
        quoteB= choice(Quotes)
        print(" ")
        print("**********************************************")
        print(quoteB)
        print("**********************************************")
        print(" ")
    else:
        print(" ")
        print("**********************************************")
        print ("Have a nice day ")
        print("**********************************************")
        print(" ")
        exit

elif ResponseA=="n":
    print(" ")
    print("**********************************************")
    print ("Have a nice day ")
    print("**********************************************")
    print(" ")

else:
    exit
