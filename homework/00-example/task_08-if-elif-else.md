limit = int(input("Разрешённая скорость, км/ч: "))
actual = int(input("Фактическая скорость, км/ч: "))

excess = actual - limit

if excess <= 20:
    fine = 0
elif 21 <= excess <= 40:
    fine = 750
elif 41 <= excess <= 60:
    fine = 1500
elif 61 <= excess <= 80:
    fine = 2500
else:
    fine = 5000

print(f"Штраф: {fine} руб.")
