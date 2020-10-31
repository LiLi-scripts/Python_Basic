x, y = int(input("enter x: ")), int(input("enter y: "))


if x >0:
    if y >0:
        print("I")
    elif y < 0:
        print("IV")
    else:
        print("on the x axis")
if y < 0:
    if x > 0:
        print("II")
    elif x < 0:
        print("III")
    else:
        print("on the y axis")
        