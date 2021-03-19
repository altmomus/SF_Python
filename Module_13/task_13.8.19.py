Tickets = int(input('Введите количество билетов:'))
Age = [int(input('Введите возраст гостя:')) for i in range(Tickets)]
price = []
for i in Age:
    if i < 18:
        price.append(int(0))
    elif 18 <= i < 25:
        price.append(int(990))
    else:
        price.append(int(1390))
if len(price) > 3:
    print('Цена билетов:', sum(price)*0.9)
else:
    print('Цена билетов:', sum(price))
