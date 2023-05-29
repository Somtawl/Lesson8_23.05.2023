def user_input():
    request = input("Выберите действие: \n 1 - Добавить нового пользователя \n 2 - Найти пользователя \n 3 - Удалить пользователя \n 4 - Изменить данные пользователя \n exit для выхода из программы \n")
    return request

def main():
    while True:
        ask = user_input()
        if ask == "1": new_user()
        if ask == "2": search_user("find")
        if ask == "3": search_user("delete")
        if ask == "4": search_user("edit")
        if ask == "exit": 
            print("Завершение работы")
            break



def new_user():
    first_name = input("Введите имя: ")
    last_name = input("Введите фамилию: ")
    patronymic = input("Введите отчество: ")
    birth_date = input("Введите дату рождения: ")
    tel_number = input("Введите номер телефона: ")
    file = open("db.txt", "a")
    file.write(first_name + "_" + last_name + "_" + patronymic + "_" + birth_date + "_" + tel_number + "\n")
    file.close

def search_user(command):
    file = open("db.txt", "r")
    lines = file.readlines()
    first_name = input("Введите имя: ")
    last_name = input("Введите фамилию: ")
    patronymic = input("Введите отчество: ")
    birth_date = input("Введите дату рождения: ")
    tel_number = input("Введите номер телефона: ")
    result = []
    string_number = 1
    for i in lines:
        #string = file.readline()
        search = i.split("_")
        tmp_result = []
        tmp_string = ""
        if search[0] == first_name: tmp_string = tmp_string + "Имя "
        if search[1] == last_name: tmp_string = tmp_string + "Фамилия "
        if search[2] == patronymic: tmp_string = tmp_string + "Отчество "
        if search[3] == birth_date: tmp_string = tmp_string + "Дата рождения "
        if search[4] == tel_number: tmp_string = tmp_string + "Номер телефона"
        if len(tmp_string) > 0:
            tmp_string = "Строка № " + str(string_number) + " " + tmp_string
            tmp_result.append(tmp_string)
            tmp_result.append(i.replace("_"," "))
            result.append(tmp_result)
        string_number = string_number + 1
    if len(result) != 0:
        print("Результаты поиска:")
        for i in range(len(result)):
            print("Совпадение по полям: ", result[i][0]," - ", result[i][1])
    if len(result) == 0:
        print("Нет совпадений")
        return
    if command == "find":
        return
    if command == "delete" and len(result) != 0:
        sting_to_delete = int(input("Укажите строку для удаления:"))
        delete_user(sting_to_delete - 1)
    if command == "edit" and len(result) != 0:
        sting_to_edit = int(input("Укажите строку для редактирования:"))
        edit_user(sting_to_edit - 1)


def delete_user(string):
    file = open("db.txt", "r").readlines()
    file.pop(int(string))
    with open("db.txt","w") as F:
        F.writelines(file)

def edit_user(string):
    file = open("db.txt", "r").readlines()
    old_line = file[int(string)]
    edit_request = int(input("Для изменения имени нажмите 1 \n Для изменения фамилии нажмите 2 \n Для изменения отчества нажмите 3 \n Для изменения даты рождения нажмите 4 \n Для изменения номера телефона нажмите 5 \n"))
    edit_value = input("Укажите новое значение ")
    tmp_line = old_line.split("_")
    print(tmp_line[0],edit_value)
    if edit_request == 1: new_line = old_line.replace(tmp_line[0],edit_value)
    if edit_request == 2: new_line = old_line.replace(tmp_line[1],edit_value)
    if edit_request == 3: new_line = old_line.replace(tmp_line[2],edit_value)
    if edit_request == 4: new_line = old_line.replace(tmp_line[3],edit_value)
    if edit_request == 5: new_line = old_line.replace(tmp_line[4],edit_value)
    writer = open("db.txt", "w")
    for line in file:
        if line == old_line:
            writer.write(new_line)
        else:
            writer.write(line)
    writer.close()

main()