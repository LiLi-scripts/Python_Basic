
a=input()
b=input()

operator=input("Enter + or - or * or /: ")

try:
    a, b = int(a), int(b)
except Exception as e:
    print("not a digit")
else:
    if operator =="+":
        print(a+b)
    if operator =="-":
        print(a-b)
    if operator =="*":
        print(a*b)
    if operator =="/" and b !=0:
        print(a/b)
    else:
        print("0")



     








