import random

class Dice:
        
    def Roll():

        x=random.randint(1,6)
        y=random.randint(1,6)
        t=(x,y)
        return t

Turn1=Dice.Roll()
print(Turn1)


