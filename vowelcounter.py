#! /usr/bin/python3

"""
This program counts the number of vowels in a word
"""
def vowelcounter():
    
   
    vowels = ('a','e','i','o','u')
    count = 0
    word = input("Insert your words >>")
    words= word.lower()
    
    for word in words:
        if word in vowels:
            count+=1
        else:
            count+=0
    print ("We have %d Vowels in the word  \"%s\""%(count,words))


vowelcounter()