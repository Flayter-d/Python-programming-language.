attendance = int(input("Посещаемость, %: "))
labs_done = int(input("Сдано лабораторных: "))
debt = int(input("Долг по оплате, руб.: "))

check_attendance = attendance >= 75
check_labs = labs_done >= 8
check_debt = debt == 0

is_admitted = check_attendance and check_labs and check_debt

print(f"Посещаемость: {check_attendance}")
print(f"Лабораторные: {check_labs}")
print(f"Нет долга: {check_debt}")
print(f"Допущен: {is_admitted}")
