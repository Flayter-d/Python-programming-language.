is_paid = input("Заказ оплачен (да/нет): ")
has_stock = input("Товар есть (да/нет): ")
address_given = input("Адрес указан (да/нет): ")

can_ship = is_paid == "да" and has_stock == "да" and address_given == "да"
call_customer = is_paid == "да" and address_given == "нет"

print(f"Можно отправлять: {can_ship}")
print(f"Позвонить покупателю: {call_customer}")
