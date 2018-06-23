#! usr/bin/python3

"""
Simple Calculator that add, multiply, 
substract and Divide two variables
"""

def simplecalculator():

    try:
        def add(A,B):
            ans= A + B 
            return ans 


        def sub(A,B):
            ans= A - B 
            return ans 

        def mut(A,B):
            ans= A * B 
            return ans 

        def div(A,B):
            ans= A / B 
            return ans 

        def close():
            exit

        print ("For Operators, Use addition: + , subtraction: -, multiply: *, division: / ")
        print("  ")    
        print("****************************************************************")
        operand = input (" What Operation do you want to perform ? \"+\", \"-\", \"*\" or \"/ \" ? OR press \" q \"  to exit >>")
        print("  ")    
        if operand==("+" or "-" or "*" or "/" or "q"):
    
            A= int((input ("What is the first variable? >> ")))
            print(" ")
            B= int((input ("What is the second variable? >> ")))

                           
            if operand == "-":
                result= sub(A,B)
                
                
            elif operand == "*":
                result= mut(A,B)

            elif operand == "/":
                result= div(A,B)
            
            elif operand =="+":
                result= add(A,B)
            
                
            else:
                print("  ")    
                print("****************************************************************")
                print ("Sorry! Check your input")
                print("****************************************************************")
                print("  ")
                command= input("Do you want to try again? y or n >> ")
                if command =="y":
                    simplecalculator()
                elif command == "n":
                    exit
                else:
                    exit

    
            print("  ")    
            print("****************************************************************")
            print ("%d %s  %d = %d "  %(A, operand, B, result))
            print("****************************************************************")
            
            
        else:
            print("  ")    
            print("****************************************************************")
            print ("Sorry! It works only for + ,- , * , /  ")
            print("****************************************************************")
            print("  ")
            command= input("Do you want to try again? y or n >> ")
            if command =="y":
                simplecalculator()
            elif command == "n":
                print("Thank you for using the calculator")
                print(" ")
                exit
            else:
                exit
      
    except (ValueError ) :
        print("  ")
        print("****************************************************************")
        print(" Check what you inputted and try again")
        print("****************************************************************")
        print("  ")
        simplecalculator()


simplecalculator()





# def complexcalculator ():


