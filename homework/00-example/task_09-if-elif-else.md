a = int(input("Сторона a: "))
b = int(input("Сторона b: "))
c = int(input("Сторона c: "))

if a < b + c and b < a + c and c < a + b:
    if a == b == c:
        print("Равносторонний")
    elif a == b or b == c or a == c:
        print("Равнобедренный")
    else:
        print("Разносторонний")
else:
    print("Треугольник не существует")
