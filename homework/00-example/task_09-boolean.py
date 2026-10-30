price1 = int(input("Цена первого товара, руб.: "))
price2 = int(input("Цена второго товара, руб.: "))

# Считаем, сколько товаров дороже 1000 рублей
count_over_1000 = 0
if price1 > 1000:
    count_over_1000 += 1
if price2 > 1000:
    count_over_1000 += 1

# Купон действует, если ровно один товар дороже 1000
coupon_valid = count_over_1000 == 1
print(coupon_valid)
