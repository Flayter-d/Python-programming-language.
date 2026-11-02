months = int(input("Отработано месяцев: "))
days_requested = int(input("Дней отпуска: "))

if months < 6:
    print("Отпуск пока недоступен")
else:
    available_days = (months * 28) // 12
    print(f"Доступно дней: {available_days}")
    
    if days_requested <= available_days:
        print("Отпуск согласован")
    else:
        missing_days = days_requested - available_days
        print(f"Не хватает дней: {missing_days}")
