import re

# 1. List of digits is given. Print a number - quantity of unique
#  digits in a list.

a = [5, 3, -2, 1, 3, -2, 1, 5]

unique_list = a[:]
count = 0

for i in unique_list:
    if a.count(i) > 1:
        unique_list.remove(i)
        quantity = len(unique_list)
print('1.a. Unique digits:', unique_list, 'Quantity: ', quantity)

# or 1 more solution:

unique_set = set(a)
q = len(unique_set)
print('1.b. unique elements: ', q)

# 2. How many digits are in the list a and b at the same time?
# Print a digit and list of intersecting elements in decreasing
# order.

b = [3.35, -12.56, 1, 4.75, 5, -3]
c = len(a + b)
print('2.a. Elements quantity in a & b: ', c)

a_set = set(a)
b_set = set(b)
print('2.b. Intersecting elements quantity: ', len(a_set.intersection(b_set)))

c2 = a_set & b_set
c3 = list(c2)
print('2.c. Intersecting Set: ', c2, ';', 'Descending List: ', c3[::-1])

# 3.How many unique words are in the text?

text = (
    'Duis dolor libero, ornare at mollis eget, aliquam ut elit.'
    'Morbi vitae convallis enim. Nulla in fringilla erat, id euismod urna.'
    'Mauris vitae diam mauris. Donec condimentum cursus dapibus.'
    'Morbi euismod vitae velit vuloutate gravida.'
)

all_words = re.findall(r'[a-zA-Z]+', text)
new_text = set(all_words)
print('3. Unique words in text: ', len(new_text))
