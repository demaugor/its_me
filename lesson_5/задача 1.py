def fact(number):
    if number == 1:
        return number
    else:
        return number * fact(number - 1)

print(fact(int(input('задайте число: '))))