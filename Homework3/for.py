while True:
    n = int (input ("Enter n: "))
    operator = input("Enter + or - or * or /: ")
    
    result = int (input ("Enter number: "))
    
    for count in range (1, n):
        m = int (input ("Enter number: "))
        if operator == "+":
            result += m
        elif operator == "-":
            result -= m
        elif operator == "*":
            result *= m
        elif operator == "/":
            result /= m
        else:
            print ("fail operator")
        
        count += 1
    print (result)
    if input ("Continue? (y/n): ") == "y":
        continue
    else:
        print ("Bye")
        break
