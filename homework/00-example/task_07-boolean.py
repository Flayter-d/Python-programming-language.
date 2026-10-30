bottles = int(input("Количество бутылок: "))

can_ship = bottles % 6 == 0 and bottles % 4 == 0
print(can_ship)
