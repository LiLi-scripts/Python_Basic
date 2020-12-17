my_list = ['53', 23, 'python', 'red', 2.0, False]

# 1.Create copy of my_list
z = my_list[:]
print('1.', z)

# 2. Change list order to vice versa
z.reverse()
print('2.', z)

# 3.Take out element with index 3 and make it variable tmp
tmp = z.pop(3)
print('3.', z)

# 4. Delete element 'red'
z.remove('red')
print('4.', z)

# 5. Insert tmp element in the beginning of the list
z.insert(0, tmp)
print('5.', z)

# 6. Extend my_list with a copy (combine in one list)
combined = my_list*2
print('6.', combined)

# 7. Change last 23 to 123
combined.insert(-5, 123)
del combined[-5]
print('7.', combined)

# 9. For each element : print element and count in a list

for i in combined:
    print('9. Element: ', i, ', Count: ', combined.count(i))

# 10. Delete elements that appear more than once and print result

short_list = combined[:]
for i in combined:
    if combined.count(i) > 1:
        short_list.remove(i)
print('10.', short_list)
