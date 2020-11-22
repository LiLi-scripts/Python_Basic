# Генератор паролей.
#Пользователь выбирает 1 из 3 вариантов:
#1. Сгенерировать простой пароль (только буквы в нижнем регистре, 8 символов)

from random import choice, randint
from string import ascii_lowercase, ascii_uppercase, ascii_letters, digits, punctuation

result = str ('')


def simple_pass (result):

    string_ = ascii_lowercase

    choose_symbol = choice (string_)
    result = result + choose_symbol
    
    if len (result) < 8:
        simple_pass (result)
    else:
        print ("1. Simple password: ", result)

simple_pass (result)


#2. Сгенерировать средний пароль (любые буквы и цифры, 8 символов)

def medium_pass (result):
    
    string_ = ascii_letters + digits

    choose_symbol = choice (string_)
    result = result + choose_symbol
    
    if len (result) < 8:
        medium_pass (result)
    else:
        print ("2. Medium password: ", result)

medium_pass (result)

#3. Сгенерировать сложный пароль (минимум 1 большая буква, 1 маленькая, 1 цифра и 1 спец-символ, длина от 8 до 16 символов)
#(для 3 пункта можно генерировать пароли до тех пор, пока не выполнится условие)


def strong_pass (result):
    
    string_ = ascii_lowercase + ascii_uppercase + digits + punctuation

    choose_symbol = choice (string_)
    random_length = randint (8, 16)
    result = result + choose_symbol
    
    if  len (result) < random_length:
        strong_pass (result)
    else:
        print ("3. Strong password: ", result)

strong_pass (result)

#Additional tasks:
#1. Позволить пользователю выбирать длину пароля, но предупреждать, что
# пароль ненадежный, если длина меньше 8 символов

i = int (input ("#Additional task. Choose password length: "))
if i < 8:
    print ("Password is unsecure. Needs to be more than 8")
else:
    pass


def diff_pass (result):
    
    string_ = ascii_letters + digits

    choose_symbol = choice (string_)
    result = result + choose_symbol
    
    if len (result) < i:
        diff_pass (result)
    else:
        print ("Additional task: ", result)

diff_pass (result)
