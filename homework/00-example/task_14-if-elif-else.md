on_time = input("Сдана в срок (да/нет): ")
score = int(input("Баллы: "))

if score < 0 or score > 10:
    print("Ошибка ввода")
else:
    if on_time == "да":
        if 9 <= score <= 10:
            print("Оценка: 5")
        elif 7 <= score <= 8:
            print("Оценка: 4")
        elif 5 <= score <= 6:
            print("Оценка: 3")
        else:  # score < 5
            print("Работа не зачтена")
    else:  # on_time == "нет"
        if score >= 5:
            print("Оценка: 3")
        else:
            print("Работа не зачтена")
