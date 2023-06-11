i = int(input("Введите число для вычисления факториала: "))

factorial = 1
while i > 1:
    factorial *= i
    i -= 1
    
print( factorial)