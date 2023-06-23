numbers_str = input("Введите числа через пробел: ")
numbers = [float(n) for n in numbers_str.split()]

odd = [num for num in numbers if num % 2 != 0]
even = [num for num in numbers if num % 2 == 0]

result = odd + even
result_str = ", ".join(str(num) for num in result)
print(result_str)