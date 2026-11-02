has_sub = input("Подписка есть (да/нет): ")
minutes = int(input("Длительность поездки, мин: "))

if has_sub == "да":
    if minutes <= 30:
        print("Поездка входит в подписку")
    else:
        cost = (minutes - 30) * 5
        print(f"К оплате: {cost} руб.")
else:
    cost = 50 + minutes * 8
    print(f"К оплате: {cost} руб.")
