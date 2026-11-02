pressure = float(input("Давление, бар: "))

if pressure < 2.2:
    print("Подкачайте шины")
elif 2.2 <= pressure <= 2.5:
    print("Давление в норме")
else:
    print("Снизьте давление")
