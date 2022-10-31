tickets = int(input("Введите количество необходимых билетов: "))
person = 1
cash = 0
while person <= tickets:
    age_for_ticket = int(input(f'Укажите для какого возраста приобретается билет № {person} ? '))
    if age_for_ticket < 18:
        print('Билет бесплатный')
    elif 18 <= age_for_ticket < 25:
        cash += 990
        print('Стоимость билета: 990 руб.')
    else:
        cash += 1390
        print('Стоимость билета: 1390 руб.')
    person += 1
if tickets > 3:
    sale = cash - ((cash / 100) * 10)
    print(f'Сумма к оплате {sale} руб., 10%-ая скидка за покупку более 3 билетов единовременно')
else:
    print(f'Сумма к оплате {cash} руб.')
