start = int(input("Начало интервала, ч: "))
end = int(input("Конец интервала, ч: "))
arrival = int(input("Курьер приехал, ч: "))

if start <= arrival <= end:
    print("Вовремя")
elif arrival < start:
    print("Раньше интервала")
else:
    delay = arrival - end
    print(f"Опоздание на {delay} ч")
