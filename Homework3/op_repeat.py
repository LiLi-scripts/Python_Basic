n = input ("Enter a 5-digit number: ")

while True:

    try:
        k = int (n)
    except ValueError:
        print ("Input Number: ", n, " - is not a digit")
        break

    if 9999 < k <= 99999:
        # 99999
        k1 = k // 10000 * 10000  # 90000
        k2 = k // 1000 * 1000 - k1 # 9000
        k3 = k // 100 * 100 - k1 - k2  # 900
        k4 = k // 10 * 10 - k1 - k2 -k3  # 90
        k5 = k - k1 - k2 - k3 - k4  # 9
        print (k1 + k3 + k5)
        break
    else:
        print ("Number is not 5-digit")
        break
