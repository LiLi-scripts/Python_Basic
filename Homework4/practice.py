#Выполнить описанные действия над строкой.

#string = 'Lorem, Ipsum, is, simply, dummy, text, of, the, printing, industry.'

# 1. Изменить строку таким образом, чтоб вместо ', ' был пробел ' '
#    Вывести получившуюся строку.

s = 'Lorem, Ipsum, is, simply, dummy, text, of, the, printing, industry.'
print (s.replace (", " , " "))

# 2. Вывести индекс самой последней буквы 's' в строке.

print (s.rindex ("s"))

# 3. Вывести количество букв 'i' в строке (регистр не имеет значения).

print (s.count ("i"))

# 4. Вывести срез строки.
#    Условие: от 'simply' до 'of' не включительно
#    Результат: 'simply dummy text'
#    (используйте методы find или index для получения индексов)

print (s [18:39])

# 5. Продублируйте первую половину строки 3 раза и склейте с второй половиной.
#    Выведите результат.

print (len (s))
print (s [:33] * 3 + s [33:])
