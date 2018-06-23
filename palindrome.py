#! /usr/bin/python3

"""
This code checks if the inserted word is a palindrome. 
Example: racecar = "racecar" when reversed
         man != "nam" when reversed
"""
def palindrome():
    word = input("Insert your own word  >>  ")
    lists=[]
    for a in word:
        lists.append(a)
    if lists == lists[::-1]:
        print("Dope. It is palindrome")
        print(" ")
    else:
        print ("Nah. It is not palindrome")
        print(" ")

palindrome()
