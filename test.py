from main import Cat, GuestsList, NewGuests

cats = [
    {
        "name": 'Барон',
        "gender": "мальчик",
        "age": 2,
    },
    {
        "name": 'Сэм',
        "gender": "мальчик",
        "age": 2,
    },
]

for cat in cats:
    pussy = Cat()
    pussy.init_from_dict(cat)
    print(pussy.get_name())
    print(pussy.get_gender())
    print(pussy.get_age())

collection = []
a = "N"
while True:
    personnel_collection = {}
    if a == "N" or a == "n":
        all_name = input('Введите имя: ')
        city = input('Введите город: ')
        status = input('Введите роль сотрудника: ')
        print('Нажмите "Y", если хотите завершить заполнение списка, '
              '"N", если хотите продолжить заполнение')
        personnel_collection['all_name'] = all_name
        personnel_collection['city'] = city
        personnel_collection['status'] = status

        collection.append(personnel_collection)
        a = input()
        continue
    elif a == "Y" or a == "y":
        break

for guest in collection:
    if guest['status']:
        guest_person = NewGuests()
        guest_person.init_from_dict(guest)
    else:
        guest_person = GuestsList(guest['all_name'], guest['city'])
    print(guest_person)
