#! usr/bin/python3

"""
This program receives temperature input in Celcius or Frehrenheit from the user
and converts it is to Frehrenheit or Celcius

"""

def Celcius2Frehrenheit():
    Cel =int(input("Please insert the  Celcius value >>"))
    Result = ((9/5)*Cel) +32
    print (" ")
    print ("**********************************************************")
    print ("%d Degree Celcius = %d Degree Frehrenheit "%(Cel,Result))
    print ("**********************************************************")

    print (" ")

def Frehrenheit2Celcius():
    Fre =int(input("Please insert the  Frehrenheit value >>"))
    Result = ((5/9)*(Fre-32))
    print (" ")
    print ("**********************************************************")
    print ("%d Degree Frehrenheit  = %d Degree Celcius "%(Fre,Result))
    print ("**********************************************************")
    print (" ")
    
    

print("This program can only convert Celcius to Frehrenheit or vice versa")
print(" ")

print("For Celcius-> Frehrenheit Conversion: Press A ; For Frehreneit -> Celcius : Press B")
Datainput= input(">> ").upper()
if Datainput== "A":
    Celcius2Frehrenheit()
elif Datainput == "B":
    Frehrenheit2Celcius()

else:
    print("You inserted a wrong input")



    



