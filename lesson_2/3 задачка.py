price = float(input("Введите стоимость товара: "))

if price > 500:
    discount = 20
elif price > 100:
    discount = 15
elif price > 80:
    discount = 10
else:
    discount = 5

discount_amount = price * discount / 100
price_with_discount = price - discount_amount

print(f"Цена со скидкой {discount}%: {price_with_discount}")