"""
    Необходимо реализовать форму регистрации пользователей.
    Поля формы: номер телефона, email, пароль и подтверждение пароля.
    !!! Для решения необходимо использовать функции и рекурсию, а не циклы. !!!
    пункты с ** - дополнительно, но не обязательно (не влияет на оценку)
    1. Пользователь вводит номер телефона.
        Программа проверяет валидность телефона:
        - приводит номер к формату 380501234567
        - если номер не получается привести к нужному формату
            то запрашивает ввод номера еще раз
            и так до тех пор, пока не будет введен валидный номер
    2. Пользователь вводит email.
        Программа проверяет валидность email:
        - должен иметь длину 6 символов и больше
            (функция len())
        - содержать один символ '@'
            (строчный метод count())
        - ** содержать логин и полный домен (логин@полный.домен)
        Пользователь может вводить email до тех пор, пока он не будет валидным.
    3. Пользователь ввод пароль.
        Программа проверяет надежность пароля:
        - минимум 8 символов
            (функция len())
        - пароль не должен содержать пробельные символы
            (строчный метод isspace())
        - наличие минимум 1 буквы в верхнем регистре, 1 в нижнем и 1 цифры
            (строчные методы isupper(), islower(), isdigit())
        - ** наличие минимум 1 спец символа
    4. После успешного ввода пароля пользователь вводит подтверждение пароля.
        Если подтверждение пароля не сходится с введенным паролем,
        то возвращаемся к пункту 3.
        Программа выводит сообщение:
        Поздравляем с успешной регистрацией!
        Ваш номер телефона: +380501234567
        Ваш email: example@mail.com
        Ваш пароль: **********
"""

def main ():
    phone =  input_phone ()
    email = input_email ()
    password = input_password ()

    print ("Your phone number: +" + phone)
    print ("Your e-mail: ", email)
    print ("Your password: ", password)

def input_phone ():
    phone = input ("1. Enter mobile number: ")
    phone = phone.replace(" ", "")

    if phone.isdigit ():
        print ("Phone you entered is: ", phone)
        if len (phone) != 12:
            print ("Check entered number! Expected 12 digits")
            return input_phone ()
    else: 
        print ("Incorrect number. Input digit")
        return input_phone()
    return phone

def input_email ():
    email = input ("2. Enter e-mail: ")
    if "@" in email:
        if len (email) < 6:
            print ("Incorrect length. Min 6 symbols")
            return input_email()
    else:
        print ("Incorrect input. Missing @")
        return input_email ()
    return (email)

def input_password ():
    password = input ("3. Enter Password: ")
    password_1 = ""

    lower_case = 0
    upper_case = 0
    digit_case = 0

    if len (password) < 8:
            print ("Incorrect length. Min 8 symbols")
            return input_password ()

    for i in password:
        if i.isspace() is True:
            print ("Watch out spaces. Input again")
            return input_password ()

    for i in password:
        if i.isupper() is True:
            upper_case = 1
            break

    for i in password:
        if i.islower () is True:
            lower_case = 1
            break

    for i in password:
        if i.isdigit () is True:
            digit_case = 1
            break

    if lower_case + upper_case + digit_case == 3:
        password_1 = input ("Re-enter password: ")
        if password == password_1:
            print ("4. Congrats with successful registratioin!")
    else:
        print ("Lower, Upper, Digit condition is not met. Input again")
        return input_password ()
    return (password)


main ()



