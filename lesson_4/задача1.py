n = int(input("Введите число для вычисления факториала: "))

factorial = 1
while n > 1:
    factorial *= n
    n -= 1
    
print( factorial)