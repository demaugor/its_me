km = int(input("Сколько километров будем ехать? -> ")) 
long = 0
while long != km:
    if long % 5 == 0:
        print(f"Мы проехали {long} км.") 
    long += 1

print("Ура! Мы доехали до города Б! Всего пройдено %s километров." % long)