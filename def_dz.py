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
