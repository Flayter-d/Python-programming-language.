age = int(input("Возраст: "))

is_discount = age < 18 or age >= 65
is_full = not is_discount

print(f"Льготный билет: {is_discount}")
print(f"Полный билет: {is_full}")
