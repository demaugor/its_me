"""a = int(100)
print("цена 1-20")
b = int(200)
print ("цена 20-25")
c = int(250)
print ("цена 25-30")
i = int(400)
print ("цена 30-35")
d = int(500)
print ("цена 35-40")
e = int(800)
print ("цена 40-50")
f = int(1200)
print ("цена 50-55")
g = int(1800)
print ("цена 55-60")
h = int(3500)
print ("цена 60-65")


summ = a * int(input("введите множетель 1-20"))
summ1 = b * int(input("введите множетель 20 25"))
summ2 = c * int(input("введите множетель 25-30"))
summ8 = i * int(input("введите множетель 30-35"))
summ3 = d * int(input("введите множетель 35-40"))
summ4 = e * int(input("введите множетель 40-50"))
summ5 = f * int(input("введите множетель 50-55"))
summ6 = g * int(input("введите множетель 55-60"))
summ7 = h * int(input("введите множетель 60-65"))

lastsumm = int(summ + summ1 + summ2 + summ3 + summ4 + summ5 + summ6 + summ7 + summ8 )


print (lastsumm)
"""
prise= {"1-20":{int:(10000)},
        "20-25":{int:(20000)},
        "25-30":{int:(25000)},
        "30-35":{int:(40000)},
        "35-40":{int:(50000)},
        "40-50":{int:(80000)},
        "50-55":{int:(120000)},
        "55-60":{int:(180000)},
        "60-65":{int:(350000)}, 
    }
while True:
    while True:
        selected_prise = input("Введите уровень (оставьте пустым для вывода списка): ")
        if not selected_prise:
            print("Список доступных уровней: ", *prise.keys(), sep="\n - ")
            continue
        if selected_prise not in prise:
            print("Такого уровня нет(ещё)!")
            continue
        break
    
    множетель = int(input("множетель"))
    print(
    f"\tобщая цена{selected_prise * множетель} ")
    
            
    