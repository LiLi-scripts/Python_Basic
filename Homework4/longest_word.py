"""
    Вводится строка.
    1. Вывести количество слов в введенной строке.
    2. Вывести самое длинное слово и его длину.
"""
s = input ("Enter a string: ")

longest_word = ""
import re

#count = len (re.findall (r"\w+", s))
#print (count)


count = len (re.findall ("[a-zA-Z]+", s))
print ("1. Words quantity =", count)

longest_word = max (s.split (), key = len)
print ("2. Longest_word: ", longest_word, "Length: ", len (longest_word))
    






