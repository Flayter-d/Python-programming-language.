cashier1 = input("Касса 1 открыта (да/нет): ")
cashier2 = input("Касса 2 открыта (да/нет): ")
cashier3 = input("Касса 3 открыта (да/нет): ")

# Считаем, сколько касс открыто (сравниваем со строкой "да")
open_count = 0
if cashier1 == "да":
    open_count += 1
if cashier2 == "да":
    open_count += 1
if cashier3 == "да":
    open_count += 1

# Ровно одна касса открыта, если счётчик равен 1
exactly_one_open = open_count == 1
print(exactly_one_open)
