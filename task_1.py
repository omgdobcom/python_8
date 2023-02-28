# Создать телефонный справочник с возможностью импорта и экспорта данных в формате csv. 
# Доделать задание вебинара и реализовать Update, Delete
# Информация о человеке: Фамилия, Имя, Телефон, Описание

# Корректность и уникальность данных не обязательны.

# Функционал программы
# 1) телефонный справочник хранится в памяти в процессе выполнения кода.
# Выберите наиболее удобную структуру данных для хранения справочника.

# 2) CRUD: Create, Read, Update, Delete

# Create: Создание новой записи в справочнике: ввод всех полей новой записи, занесение ее в справочник.
# Read: он же Select. Выбор записей, удовлетворяющих заданном фильтру: по первой части фамилии человека.
# Берем первое совпадение по фамилии.
# Update: Изменение полей выбранной записи. Выбор записи как и в Read, заполнение новыми значениями.
# Delete: Удаление записи из справочника. Выбор - как в Read.
# 3) экспорт данных в текстовый файл формата csv

# 4) импорт данных из текстового файла формата csv

# Используйте функции для реализации значимых действий в программе

phone_book = []

def menu(data: list):
    while True:
        print('Выберите действие: ')
        print('1 - создать новую запись')
        print('2 - распечатать содержимое справочника')
        print('3 - импортировать данные с текстового файла')
        print('4 - найти заданную запись по фамилии')
        print('5 - изменить данные выбранной записи')
        print('6 - удаление данных из справочника')
        print('7 - записать данные в файл с учётом удалённого абонента')
        
        get = input('Введите действие: ')
        if get == '':
            print('До свидания!')
            break
        elif get == '1':
            data = create(data, get_data())
        elif get == '2':
            print_phone_book(data)
        elif get == '3':
            name_file = get_file_name()
            batch_data = get_batch_data(name_file)
            data = batch_create(data, batch_data)
        elif get == '4':
            print(find_name_data(data))
        elif get == '5':
            change = print(change_data(data))
        elif get == '6':
            delete = delete_rec(data)
        elif get == '7':
            write_data(data)
        else:
            print("Такого пункта нет.Попробуйте ещё раз!")

def create(data: list, elem: tuple) -> list: # добавляет запись в существующую телефонную книгу
    data.append(elem)
    return data

def print_phone_book(data: list) -> None:
    for value in data:
        print(f'{value[0]}, {value[1]}, {value[2]}, {value[3]}')

def get_data() -> tuple: # запрашивает данные у пользователя
    surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    phone = input('Введите номер телефона: ')
    discription = input('Введите описание: ')
    return (surname, name, phone, discription)

def get_file_name() -> str:
    return input('Введите имя файла: ')


def get_batch_data(name_file: str) -> list: 
    lst = []
    with open('data08_1.txt', 'r', encoding='utf-8') as file:
        for line in file:
            temp = tuple(line.strip().split('#'))
            lst.append(temp)
    return lst

def batch_create(data: list, batch_data) -> list:   
    for elem in batch_data:
        data = create(data, elem)
    return data

def find_name_data(data: list) -> list: 
    name = input("Введите фамилию абонента: ")
    for el in data:
        if name.casefold() in (el[0]).casefold():
            return el

def change_data(data: list) -> list:
    change_name = find_name_data(data)
    change_name = list(change_name)
    change_name[2] = input("Введите номер телефона абонента: ")
    change_name[3] = input("Введите статус абонента: ")
    return list(change_name)
    
def delete_rec(data: list) -> list: 
    find_name = find_name_data(data)
    data.remove(find_name)
    return data

def write_data(data: list) -> list: 
    
    with open('HW8\data08_2.txt', 'w', encoding='utf-8') as file:
        for elem in data:
            file.write(f"{'#'.join(elem)}\n")

menu(phone_book)