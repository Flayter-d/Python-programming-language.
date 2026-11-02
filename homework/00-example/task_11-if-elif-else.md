has_policy = input("Полис ОМС есть (да/нет): ")
age = int(input("Возраст: "))

if has_policy == "да":
    if age < 18:
        print("Запись к педиатру")
    else:
        print("Запись к терапевту")
else:
    print("Доступен платный приём")
