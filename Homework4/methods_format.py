#1 Task. 

#Вводится строка.
# Если в строке больше символов в нижнем регистре - вывести все в нижнем,
#если больше в верхнем - вывести все в верхнем,
#если поровну - вывести в противоположных регистрах.


s = input ("1. Enter a string: ")

count_l = count_u = 0


for i in s:
    if i.islower ():
        count_l += 1
    elif i.isupper ():
        count_u += 1
    elif count_l > count_u:
        print (s.lower())
    elif count_l < count_u:
        print (s.upper())
    else:
        print (s.swapcase())
print ("Upper case = ", count_u, "Lower case = ",count_l)

 #2 Task
#Вводится строка.
#Если в строке каждое слово начинается с заглавной буквы, тогда
#добавить в начало строки 'done. '.
#Иначе заменить первые 5 элементов строки на 'draft: '.
# (можно использовать метод replace и/или конкатенацию строк + срезы)

s = input ("2. Enter a string: ")
s1 = s * 2

t = "done."

template_1 = "Some string {0}\nSome edited string {1}"

if s.istitle ():
    print (t + s)
else:
    print (s.replace (s [:5],"draft"))

print (template_1.format (s, s1))


#3 Task

#Если длина строки больше 20, то обрезать лишние символы до 20.
#Иначе дополнить строку символами '@' до длины 20.
#(можно использовать метод ljust либо конкатенацию и дублирование (+ и *))

#После выполнения кажого пункта выводить результат типа:
#1. Исходная строка: "some string".
#Результат: "some edited string".
# (Использовать форматирование строк f, format либо %)

s = input ("3. Enter a string: ")
s1 = s * 2

template_1 = "Some string {0}\nSome edited string {1}"

if len (s) > 20:
     s = s [:21]
     print (s)
else:
    print (s.ljust (20, "@"))
    
print (template_1.format (s, s1))
     

