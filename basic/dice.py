#coding: utf-8

from random import randint
class Dice():
    sides = 6
    def __init__(self,sides):
        self.sides = sides
    def roll_dice(self):
        x = randint(1,self.sides)
        print(x, end=' ')
dice = Dice(6)
for i in range(10):
    dice.roll_dice()
