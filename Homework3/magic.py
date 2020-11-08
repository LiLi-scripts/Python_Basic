while True:
    m = int (input ("Choose a number: "))
    count = 1 
    import random
    random_number = random.randint (1, 100)
    
    while True:
        if m < random_number :
            print ("Magic number is bigger")
            count += 1
            m = int (input ("Choose a number: "))
        elif m > random_number :
            print ("Magic number is smaller")
            count += 1
            m = int (input ("Choose a number: "))
        else:
            break
    print ("Congratulations! Magic number is yours: ", random_number)
    print ("Number of your attempts: ", count)

    if input ("Continue? y/n: ") == "y":
        count = 0
    else:
        break
    