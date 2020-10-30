#2. Task
a=int(input("Enter nr1: "))
b=int(input("Enter nr2: "))
c=int(input("Enter nr3: "))

if a>b and a>c or a<b and a<c:
    a>b>c, a>c>b, a<b<c, a<c<b
    print(a)
if b>a and b>c or b<a and b<c:
    b>a>c, b>c>a, b<a<c, b<c<a
    print(b)
if c>a and c>b or c<a and c<b:
    c>a>b, c>b>a, c<a<b, c<b<a
    print(c)
else: 
    print(a, b, c)
    

    

