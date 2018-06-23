"""
This program is a contact addressbook that stores it in a text file
"""

import sys

ns=0
dd = open('contactbook.txt', 'r')
def adressbook(ns,dd):
    for line in dd:
        ns=ns+1

    print(" This addressbook stores names and phone number")
    print("  ")
    print("*****************************************************")
    contacts=[ ]
    try:
        try:
            number= int(input(" How many contacts do you want to register? >>"))
        except (ValueError):
            print ("It requires an integer")
            print("  ")
        for no in range(number):
            ns+=1

            name= input("Please insert the name  >>")
            phoneno=input("Please insert the phone number >>")
            contact = "{:3d}  Name: {:20} Phone Number: {:35}".format(ns,name,phoneno)
            # contact = str(ns) + "  "+ "Name: "+name + " : "+ "Phone Number: "+phoneno
            contacts.append(contact)

            print (contact)
            print (" Inserted Sucessfully")
            print(" ")
            
        print("*****************************************************")
        print("These are the contacts you added to the addressbook")
        print(" ")
        for con in contacts:
            print (con)
            print(" ")
        print("*****************************************************")
        print(" ")

        responseA= input("Are the contacts correct? y or n >>").lower()
        if responseA=="y":
            for con in contacts:
                address = open("contactbook.txt","a")
                address.write(con + '\n')
            print(" ")
            print("*****************************************************")    
            print ("     Successfully added to the addressbook")
            print("*****************************************************")
            print(" ")
        elif responseA =="n":
            responseB= input("Do you want to start again ? y or n >>").lower()
            if responseB=="y":
                adressbook(ns,dd)
            elif responseB=="n":
                print(" ")
                print("*****************************************************")    
                print ("     Nothing was saved to the addressbook")
                print("*****************************************************")
                print(" ")
                exit
            else:
                exit
        else:
            exit
                
    except ValueError:
        print("Check your input")
        retry= input("Do you want to start again? y or n >>").lower()
        if retry=="y" :
            adressbook()
        
        elif retry=="n" :
            exit
        else:
            exit

adressbook(ns,dd)