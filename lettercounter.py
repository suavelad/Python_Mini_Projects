#! /usr/bin/python3

"""

This program counts the number of letters in a word
Example: a:30, b:4, etc

"""

import os

def lettercounter():

    count=0
    diction = [ ]
    letters=[ ]

    letters = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')

    wordings = input("insert your words >> ")
    words=wordings.lower()

    for letter in letters :
        for  word in words:
            if letter == word:
                diction.append(letter)
    print (diction)

    for letter in letters:
        num= diction.count(letter)    
        print ("%s : %d" %(letter, num))
        
   

lettercounter()