#! /usr/bin/python3

"""
This program finds the factorial of any positive integer
"""

def loopfactorial():
    print("This function is for solving Factorial(n)")
    n= input("lets find the factorial of what? >> ")
    b=1
    for num in range(1,n+1):
        a= num *1
        b=a*b
    print (b)
        
loopfactorial()

# def recursionfactorial(n):
#     if n ==0:
#         return 1
#     else:
#         num = n * recursionfactorial(n-1)
#         print (num)

# recursionfactorial(3)


    

