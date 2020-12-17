# 1. Merge 2 dictionaries in 1 and print result.

dict_1 = {'a': 32, 'b': -3}
dict_2 = {'c': 2, 'd': 0.34}

merged = dict_1.update(dict_2)
print('1. Merged dict:', dict_1)


# 2. Multiply values of result dict and print it.

result = 1
for i in dict_1:
    result = result*dict_1[i]
print('2. Multiplication: ', result)

# 3. Create a dictionary with keys - numbers from 1 to 10
# values: same keys in cube

n = dict.fromkeys([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
m = {i: i**3 for i in n}
print('3. Cubic values dict:', m)

# 4. Dict of keys and values is given.
# Create a dict with keys from list "keys" elements.
# values will be elements of list "values"

keys = ['name', 'age', 'country']
values = ['Max', 21, 'Ukraine']

my_dict = {'keys': keys[:], 'values': values[:]}
print('4. Dictionary:', my_dict)

# 5. Create a dict with keys from string symbols
# values are number counts of symbol in a string

string = 'programmer'
my_dict1 = {i: string.count(i) for i in string}
print('5. String and symbol count dict: ', my_dict1)
