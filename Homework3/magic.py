m = int (input ("Choose a number: "))

try = 0

random_number = 1 

import random

random_number = random.randint (1, 100)


while (True):
    if m < random_number:
        print ("Magic number is bigger")
        m = int (input ("Choose a number: "))
    elif m > random_number:
        print ("Magic number is smaller")
        m = int (input ("Choose a number: "))
    else:
        print ("Congratulations! Magic number is yours!")
        print ("Continue? y/n")
        break
    