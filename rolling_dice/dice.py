#! /usr/bin/env/python3
#Rolling a dice
import random
   
while True:
    print("Begin rolling the dices")
    roll = input("Roll dices: yes/no ---> ").startswith("y")
    if roll is True:
        print("Wait for dice will be roll out...")
        print("Here we go!")
        dice_side1 = random.randint(1, 6)
        dice_side2 = random.randint(1, 6)
        print("You rolled out: " + str(dice_side1) + " and " + str(dice_side2))
        if input("Want roll one more time? yes/no: ").startswith("y") == True:
            continue
    else:
        break
        
        
    
