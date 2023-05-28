from datetime import date

year = int(input(" введите год: "))
month = int(input(" введите месяц: "))
day = int(input(" день: "))

d0 = date.today()
d1 = date(year,month,day)
age = (d0 - d1).days / 365

if age >= 18:
    print("вход дан")
else:
    print("пшол нахуй от сюда")
