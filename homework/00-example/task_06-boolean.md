age = int(input("Возраст: "))
answer = input("Опыт работы есть (да/нет): ")
has_experience = answer == "да"
fits = age >= 18 and age <= 65 and has_experience
print(f"Подходит: {fits}")
