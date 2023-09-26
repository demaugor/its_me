initial = deposit = int(input("депозин: "))
percent = float(input("процент: "))/100
print(f'начальный депозит: {initial}, годовой процент: {percent*100}')


for month in range(12):
    income = deposit * percent / 12
    deposit += income
    print(f'месяц: {month+1}, доход: {income}, вклад: {deposit}')


year_percent = (deposit - initial) / initial
print(f'годовой процент с учётом капитализации составил: {year_percent*100}')