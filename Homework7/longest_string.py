"""
    Написать функцию, которая принимает список строк,
    и возвращает другой список, содержащий все самые длинные строки.
    Например:
    [in] ['a', 'asd', 'bd', 'q', 'dsq']
    [out] ['asd', 'dsq']
"""
input_string = input("Enter list elements: ")
input_list = input_string.split(",")
print(input_list)
output_list = []


def longest_strings(input_list):

    count = 0

    for i in input_list:
        if len(i) > count:
            count = len(i)

    for i in input_list:
        if len(i) == count:
            output_list.append(i)
    print(output_list)
    return input_list


longest_strings(input_list)
