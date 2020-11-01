
number = int (input("Enter digit: "))

n1 = number // 10
n2 = number % 10
n3 = number // 100
n4 = number % 100 // 10
n5 = number % 100 % 10

if number > 0 and number <= 9:
    print(number)
elif number >=10 and number <= 99:
    print (n1 + n2)
    if n1 < n2:
        print ("number increase")
    else:
        print ("number decrease")
elif number >=100 and number <= 999:
    print (n3 + n4 + n5)
    if n3 < n4 and n4 < n5:
        print ("number increase")
    if n3 > n4 and n4 > n5:
        print ("number decrease")
    else:
        print ("random numbers")
else: 
    print ("not in scope")




