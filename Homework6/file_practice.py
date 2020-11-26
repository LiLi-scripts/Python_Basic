"""
    Выполните все пункты.
    * можно описывать вложенные with open(), если это необходимо.
    * работа в основном с одним файлом, поэтому имя можно присвоить переменной
"""

# 1.
# Создайте файл file_practice.txt
# Запишите в него строку 'Starting practice with files
# # Файл должен заканчиваться пустой строкой'
new_file = open('file_practice.txt', 'w')
new_file.write('Starting practice with files\n\n')
new_file.close()

# 2.
# Прочитайте файл, выведете содержимое на экран
# Прочитайте первые 5 символов файла и выведите на экран
with open('file_practice.txt', 'r') as f:
    print(f.read())
    print(f.read(5))

# 3.
# Прочтите файл 'files/text.txt'
# В прочитанном тексте заменить все буквы 'i' на 'e', если 'i' большее
# количество, иначе - заменить все буквы 'e' на 'i'
# Полученный текст дописать в файл 'file_practice.txt'

with open('text.txt', 'r+') as f:
    data = f.read()

e = data.count('e')
i = data.count('i')
if i > e:
    print(data.replace('i', 'e'))
    data1 = data.replace('e', 'i')
elif e > i:
    print(data.replace('e', 'i'))
    data1 = data.replace('e', 'i')

with open('file_practice.txt', 'a') as f1:
    f1.write(data1)

# 4.
# Вставьте строку '*some pasted text*'.
# Если после вставки курсор остановился на четной позиции
#   - добавить в конец файла строку '\nthe end',
# иначе - добавить в конец файла строку '\nbye'
# Прочитать весь файл и вывести содержимое.

with open('file_practice.txt', 'a') as f2:
    f2.write('\n*some pasted text*')
    position = f2.tell()
    if position % 2 == 0:
        f2.write('\nthe end')
    else:
        f2.write('\nbye')
