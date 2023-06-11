factorial = 1
factorial_2 = 1000

n = 1
o = 5

while factorial <= factorial_2:
    if n > 1:
        print(factorial, "==", str(o) + "!")
    factorial *= n
    n += 1
    o += 1