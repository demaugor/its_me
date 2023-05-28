number = int(input("Введите число: "))

if number % 3 == 0:
    print("Fizz" , end="") 
if number % 5 == 0:
    print("Buzz")

else:
    print("Число не делится на 3 и на 5 без остатка")