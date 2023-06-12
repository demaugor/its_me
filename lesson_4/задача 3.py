factorial = 1
factorial_2 = 1000

i = 1
o = 0

while factorial <= factorial_2:
    if i > 1:
        print(factorial, "==", str(o) + "!")
    factorial *= i
    
    i += 1
    o += 1