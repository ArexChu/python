#coding: utf-8

import random

rps = ["rock","paper","scissors"]

while(1):
    rps_human = input("please input rock,paper or scissors:")
    rps_random = random.choice(rps)
    if(rps_human == "rock"):
        if(rps_random == "scissors"):
            print("you win")
            break
        elif(rps_random == "paper"):
            print("you lose")
            break
        else:
            print("continue")
    elif(rps_human == "paper"):
        if(rps_human == "rock"):
            print("you win")
            break
        elif(rps_human == "scissors"):
            print("you lose")
            break
        else:
            print("continue")
    elif(rps_human == "scissors"):
        if(rps_random == "paper"):
            print("you win")
            break
        elif(rps_random == "rock"):
            print("you lose")
            break
        else:
            print("continue")
