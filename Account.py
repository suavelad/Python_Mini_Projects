"""
It is an Object Oriented Program. For Bank Transactions
"""

class Account:
    def __init__(self,name,balance,min_balance):
        self.name=name
        self.balance=balance
        self.min_balance=min_balance
    
    def deposit(self,amount):
        self.balance+=amount
    
    def withdraw(self,amount):
        if self.balance - amount >= self.min_balance:
            self.balance-=amount
        else:
            print ("Sorry, You gat no cash")

    
    def statement(self):
        print ("Account Balance : ${} ".format(self.balance))

class Current(Account):
    def __init__(self,name,balance):
        super().__init__(name,balance,min_balance=1000)

details= {"Sunnex":10000}
ResponseA= input("Do you have an account with us? y or n >>").lower()
if ResponseA =="y":
    try:
        username= input("What is your name? >>")
    except:
        print("You don't have an account with us.")
    balance= details[username]
    User= Current(username,balance)
    print(" ")
    print("What transaction do you want to perform ?")
    print(" ")
    ResponseB= input("For deposit: press D, For withdraw: press W, For Bank Statement: press S >>").upper()
    if ResponseB == "D":
        cash_deposit=int(input("How much do you want to deposit? >> $"))
        User.deposit(cash_deposit)
        details[username]=User.balance
        print ("Transaction Sucessful.{}".format(User.statement()))

    elif ResponseB == "W":
        cash_withdraw=int(input("How much do you want to withdraw? >> $"))
        User.withdraw(cash_withdraw)
        details[username]=User.balance
        print ("Transaction Sucessful.{}".format(User.statement()))

    elif ResponseB == "S":
        print (User.statement())
        
    else:
        print ("Transaction Not Successful")

elif ResponseA =="n":
    ResponseC= input("Do you want to create an account ? y or n ").lower()
    if ResponseC =="y":
        username= input("What username will you use? >>")
        amount=int(input("How much are you opening the account with ? $"))
        details[username]=amount
        User= Current(username,amount)
        print("Account Created")
        print ("Transaction Sucessful.{}".format(User.statement()))

        
    elif ResponseC=="n":
        print("Thank you for patronizing us")
        exit
    else:
        print("Thank you for patronizing us")
        exit
    
