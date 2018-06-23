#! usr/bin/python3

"""
learning OOP
"""

import  random

class Pound:
    def __init__(self, rare=False):
        self.rare=rare

        if self.rare:
            self.value=1.25
        else:
            self.value=1.00
        
        self.value =1.00
        self.colour= "gold"
        self.num_edge=1
        self.diameter=22.5
        self.thickness=3.15 
        self.heads= True

    def rust(self):
        self.colour="greenish"
    
    def clean(self):
        self.colour="gold"

    def flip(self):
        options=[True,False]
        choice= random.choice(options)
        self.heads=choice

    def __del__(self):
        print("Coin Spent")
        


coin1=Pound()
coin2=Pound()
print (coin2.colour)
coin2.rust()


print (coin2.colour)
coin2.clean()

print(coin2.colour)

print(coin1.heads)

coin1.flip()
print(coin1.heads)


print (coin1.value)
