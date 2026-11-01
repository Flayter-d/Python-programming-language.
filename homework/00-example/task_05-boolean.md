score1 = int(input("Балл за первый экзамен: "))
score2 = int(input("Балл за второй экзамен: "))
score3 = int(input("Балл за третий экзамен: "))

passed_count = 0
if score1 >= 40:
    passed_count += 1
if score2 >= 40:
    passed_count += 1
if score3 >= 40:
    passed_count += 1

all_passed = passed_count == 3

print(f"Сдано экзаменов: {passed_count}")
print(f"Сессия закрыта: {all_passed}")
