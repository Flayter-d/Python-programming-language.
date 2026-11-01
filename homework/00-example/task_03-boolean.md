height = int(input("Рост, см: "))
age = int(input("Возраст: "))
with_adult = input("Со взрослым (да/нет): ")

# Условия: рост >= 120 И (возраст >= 10 ИЛИ сопровождение взрослого)
can_ride = height >= 120 and (age >= 10 or with_adult == "да")

print(f"Можно на аттракцион: {can_ride}")
