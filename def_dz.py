number_2 = int(input("input number"))


def counting_money(num: int) -> list[int]:
    if num < 80:
        one = num % 10
        two = num - (num - 10)
        update_two = num - (one + two + 10)
        five = update_two // 5

        return [one, two, five]
    else:
        one = num % 10
        two = 10
        five = 10
        ten = (num - (one + (two * 2) + (five * 5))) // 10
        return [one, two, five, ten]


res = counting_money(number_2)
numes = ["one dollar", "two dollars", "five dollars", "ten dollars"]
result = list(zip(numes, res))

print(result)

my_list_3 = [
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
result = filter_unique_dicts(my_list_3, list_of_key)
print(result)
