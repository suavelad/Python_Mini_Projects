#! usr/bin/python3
"""
This program will generate random password
"""

from random import shuffle,choice
def passwordGen():
    low_letters = ("abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*+=")
    passwords=' '
    for c in range(10):
        passwords+=choice(low_letters) 

    
    print ("Your Password is : %s" %(passwords))

passwordGen()