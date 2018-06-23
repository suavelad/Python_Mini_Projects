#! usr/bin/python3

"""
This Program encrypts and decrypts messages
"""


import pyperclip

def Cipher():
    try:

        # mode ="encrypt" # or decrypt
        mode = input("Do you want to \" encrypt \" or \" decrypt\" ? >>")



        message=input("Insert the Message you want to {} >>".format(mode))


        #encrypting and decrypting key
        key = int(input("Please insert your {} key >>".format(mode)))

        LETTERS= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        translated=''

        message= message.upper()

        for symbol in message:
            if symbol in LETTERS:
                num=LETTERS.find(symbol)
                if mode=="encrypt":
                    num=num+key
                elif mode=="decrypt":
                    num=num-key
                if  num >= len(LETTERS):
                    num= num- len(LETTERS)
                elif num < 0:
                    num= num + len(LETTERS)
                translated= translated + LETTERS[num]
            else:
                translated=translated + symbol

        print("")
        print("*****************************************")
        print("The {}ed message is: ".format(mode))
        print (translated)

        pyperclip.copy(translated)
    except:
        print("Check what you inputted")   
        Cipher() 

Cipher()