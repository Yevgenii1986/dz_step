def calculate_sum(number_one, number_two):
    res = number_one + number_two
    return res


result = calculate_sum(3, 4)
print(result)

my_list = [1, 5, 6, 55, 8, 3]


def calculate_average(nam):
    res = sum(nam) / len(nam)
    return res


result = calculate_average(my_list)
print(result)


def factorial(x, y):
    a = [i for i in range(1, x + 1)]
    b = [i for i in range(1, y + 1)]
    sum_one = 1
    sum_two = 1
    for i in a:
        sum_one *= i
    for i in b:
        sum_two *= i

    return sum_one, sum_two


result = factorial(3, 4)
print(result)

my_list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def filter_even(number):
    res = [i for i in number if not i % 2]
    return res


result = filter_even(my_list_2)
print(result)


def filter_even(*args: int) -> list[int]:
    res = []
    for i in args:
        if not i % 2:
            res.append(i)
    return res


result = filter_even(1, 2, 3, 5, 6, 8, 9, 3, 5, 76, 4)
print(result)

my_string = input("input string")


def palindrome(string: str) -> bool:
    return string == string[::-1]


result = palindrome(my_string)
print(result)
numbers = [2, 3, 5]


def modify_list(n: list[int]) -> list[int]:
    square = []
    for i in n:
        square.append(i ** 2)
    return square


result = modify_list(numbers)
print(result)
