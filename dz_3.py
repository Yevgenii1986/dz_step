# 1

# def calculate_sum(number_one, number_two):
#     res = number_one + number_two
#     return res
#
#
# result = calculate_sum(3, 4)
# print(result)


# 2

# my_list = [1, 5, 6, 55, 8, 3]
#
#
# def calculate_average(nam):
#     res = sum(nam) / len(nam)
#     return res
#
#
# result = calculate_average(my_list)
# print(result)


# 3

# def factorial(x, y):
#     a = [i for i in range(1, x + 1)]
#     b = [i for i in range(1, y + 1)]
#     sum_one = 1
#     sum_two = 1
#     for i in a:
#         sum_one *= i
#     for i in b:
#         sum_two *= i
#
#     return sum_one, sum_two
#
#
# result = factorial(3, 4)
# print(result)


# 4.1

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
#
# def filter_even(number):
#     res = [i for i in number if not i % 2]
#     return res
#
#
# result = filter_even(my_list)
# print(result)


# 4.2

# def filter_even(*args: int) -> list[int]:
#     res = []
#     for i in args:
#         if not i % 2:
#             res.append(i)
#     return res
#
#
# result = filter_even(1, 2, 3, 5, 6, 8, 9, 3, 5, 76, 4)
# print(result)


# 5

# my_string = input("input string")
#
#
# def palindrome(string: str) -> bool:
#     return string == string[::-1]
#
#
# result = palindrome(my_string)
# print(result)

# 6
# numbers = [2, 3, 5]
#
#
# def modify_list(n: list[int]) -> list[int]:
#     square = []
#     for i in n:
#         square.append(i ** 2)
#     return square
#
#
# result = modify_list(numbers)
# print(result)

# 7

# def fibonacci(n):
#     fbn1 = fbn2 = 1
#
#     i = 0
#     while i < n - 2:
#         fbn1, fbn2 = fbn2, fbn1 + fbn2
#         i = i + 1
#     return fbn2
#
#
# result = fibonacci(10)
# print(result)


# # 8
# number = int(input("input number"))
#
#
# def counting_money(num: int) -> list[int]:
#     if num < 80:
#         one = num % 10
#         two = num - (num - 10)
#         update_two = num - (one + two + 10)
#         five = update_two // 5
#
#         return [one, two, five]
#     else:
#         one = num % 10
#         two = 10
#         five = 10
#         ten = (num - (one + (two * 2) + (five * 5))) // 10
#         return [one, two, five, ten]
#
#
# res = counting_money(number)
# numes = ["one dollar", "two dollars", "five dollars", "ten dollars"]
# result = list(zip(numes, res))
#
# print(result)

# 9

my_list = [
    {'name': 'mary', 'age': 25, 'lastname': 'ivanova'},
    {'name': 'kate', 'age': 25, 'lastname': 'petrova'},
    {'name': 'mary', 'age': 35, 'lastname': 'ivanova'}
]


def filter_unique_dicts(list_of_dicts, list_of_key):
    seen_values = set()
    result = []

    for d in list_of_dicts:
        current_values = ()
        for key in list_of_key:
            current_values += (d[key],)
        if current_values not in seen_values:
            seen_values.add(current_values)
            result.append(d)

    return result


list_of_key = ['name', 'lastname']
result_1 = filter_unique_dicts(my_list, list_of_key)
print(result_1)
