
def work_with_phonebook():	
    choice=show_menu()
    phone_book=read_txt('phon.txt')
    while (choice!=8):
        if choice==1:
            print_result(phone_book)
        elif choice==2:
            last_name=input('lastname ')
            print(find_by_lastname(phone_book,last_name))
        elif choice==3:
            number=input('number ')
            print(find_by_number(phone_book,number))  	
        elif choice==4:
            lastname=input('lastname ')
            name=input('name ')
            number=input('number ')
            comment=input('comment ')
            print(add_user(lastname,name,number,comment,phone_book))
        elif choice==5:
            last_name=input('lastname ')
            new_number=input('new  number ')
            print(change_number(phone_book,last_name,new_number)) 
        elif choice==6:
            user_data=input('name file ')
            write_txt(user_data,phone_book)
        elif choice==7:
            last_name=input('lastname ')
            print(delete_by_lastname(phone_book,last_name))
        choice=show_menu()
    write_txt('phon.txt',phone_book)

def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Заменить номер абонента\n"
          "6. Сохранить справочник в текстовом формате\n"
          "7. Удалить абонента по фамилии\n"
          "8. Закончить работу")
    choice = int(input())
    return choice

def print_result(contact_list: list):
    list_of_contacts = sorted(contact_list, key=lambda x: x['Фамилия'])
    for contact in list_of_contacts:
        for key, value in contact.items():
            print(f'{key}: {value:12}', end='')
        print()

def find_by_lastname(phone_book,last_name):
    search_value = last_name
    found_contacts = []
    for contact in phone_book:
        #contact['Фамилия'] = contact['Фамилия'].replace(' ','')
        if contact['Фамилия'] == search_value:
            found_contacts.append(contact)
    if len(found_contacts) == 0:
        return 'Контакт не найден!'
    else:
        return found_contacts


def change_number(phone_book,last_name,new_number):
    for contact in phone_book:
        #contact['Фамилия'] = contact['Фамилия'].replace(' ','')
        if contact['Фамилия'] == last_name:
            contact['Телефон'] = new_number
            return "Номер изменен"
    return "Контакт не найден"

def delete_by_lastname(phone_book,last_name):
    search_result = []
    for contact in phone_book:
        #contact['Фамилия'] = contact['Фамилия'].replace(' ','')
        if contact['Фамилия'] == last_name:
            search_result.append(contact)
    phone_book.remove(search_result[0])
    return "Контакт удален"

def find_by_number(phone_book,number):
    search_value = number
    found_contacts = []
    for contact in phone_book:
        #contact['Телефон'] = contact['Телефон'].replace(' ','')
        if contact['Телефон'] == search_value:
            found_contacts.append(contact)
    if len(found_contacts) == 0:
        return 'Контакт не найден!'
    else:
        return found_contacts

def add_user(lastname,name,number,comment,phone_book):
    comment=f"{comment}\n"
    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']
    new_user=dict(zip(fields, [lastname,name,number,comment]))
    phone_book.insert(0,new_user)
    return "Абонент добавлен"
    
def read_txt(filename): 
    phone_book=[]
    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open(filename,'r',encoding='utf-8') as phr:
        for line in phr:
           record = dict(zip(fields, line.split(',')))
           phone_book.append(record)
    return phone_book

def write_txt(filename , phone_book):
    with open(filename,'w',encoding='utf-8') as phrw:
        for i in range(len(phone_book)):
            s=''
            for v in phone_book[i].values():
                s = s + v + ','
            phrw.write(f'{s[:-1]}')
    print(f"Файл сохранен {filename}")

work_with_phonebook()