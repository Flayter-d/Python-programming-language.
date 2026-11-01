category = input("Категория: ")
amount = float(input("Сумма покупки, руб.: "))

if category == "азс":
    cashback = amount * 0.05
elif category == "аптека":
    cashback = amount * 0.03
elif category == "супермаркет":
    cashback = amount * 0.01
else:
    cashback = 0.0

print(f"Кешбэк: {cashback:.2f} руб.")
