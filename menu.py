import os
import sys
import shutil
import json

from bank_account import account
from victorina import victorina


def make_directory(folder_name):

    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
        return 'Папка создана'
    else:
        return 'Папка с таким именем уже существует - придумайте другое имя!'


def delete_file_dir(f_name):
    if os.path.exists(f_name):
        shutil.rmtree(f_name, ignore_errors=True)
        if os.path.exists(f_name):
            return 'Файл не удален!'
        else:
            return 'Файл(папка) удален!'
    else:
        return 'Такого объекта не сущестует!'


def copy_file_dir():
    path_from = input('Введите название исходного файла(папки) для копирования: ')
    if os.path.exists(path_from):
        path_to = input('Введите новое название для копии файла(папки): ')
        if path_from == path_to:
            print('Имена исходного и конечного объектов должны быть разными! Попробуйте снова.')
        else:
            if os.path.exists(path_to):
                print('Объект с таким именем уже существует. Введите другое имя для копии.')
            else:
                if os.path.isfile(path_from):

                    shutil.copy(path_from, path_to)
                    if os.path.exists(path_to):
                        print('Объект успешно скопирован')
                    else:
                        print('Что-то пошло не так с этим копированием...')
                else:
                    shutil.copytree(path_from, path_to)
                    if os.path.exists(path_to):
                        print('Объект успешно скопирован')
                    else:
                        print('Что-то пошло не так с этим копированием...')
    else:
        print('Исходного объекта не существует, введите другое имя!')

def change_dir(dir_path):
    if os.path.exists(dir_path):
        os.chdir(dir_path)
        return f'Вы перешли в деректорию: {os.getcwd()}'
    else:
        return 'Нет такой директории! Попробуйте еще раз.'


def save_dirlist():
    dirlist_data = {
        'files': [],
        'dirs': [],
    }
    dir_list = os.listdir(os.getcwd())
    for item in dir_list:
        if os.path.isfile(item):
            dirlist_data['files'].append(item)
        else:
            dirlist_data['dirs'].append(item)

    with open('dir_list', 'w', encoding='utf-8') as f:
        f.write(json.dumps(dirlist_data))
    with open('dir_list', 'r', encoding='utf-8') as f:
        # f.read(json.dumps(dirlist_data))
        if json.load(f) == dirlist_data:
            return 'Содержимое директории успешно записано в файл dir_list'
        else:
            return 'Ошибка сохранения данных директории в файл'


if __name__ == '__main__':

    while True:
        print('1. создать папку')
        print('2. удалить (файл/папку)')
        print('3. копировать (файл/папку)')
        print('4. просмотр содержимого рабочей директории')
        print('5. посмотреть только папки')
        print('6. посмотреть только файлы')
        print('7. просмотр информации об операционной системе')
        print('8. создатель программы')
        print('9. играть в викторину')
        print('10. мой банковский счет')
        print('11. смена рабочей директории')
        print('12. сохранить содержимое рабочей директории в файл')
        print('13. выход')

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            print(make_directory(input('Введите имя папки: ')))
        elif choice == '2':
            print(delete_file_dir(input('Введите имя папки(файла) для удаления: ')))
        elif choice == '3':
            copy_file_dir()
        elif choice == '4':
            print(os.listdir())
        elif choice == '5':
            print([x for x in os.listdir() if not os.path.isfile(x)])
        elif choice == '6':
            print([x for x in os.listdir() if os.path.isfile(x)])
        elif choice == '7':
            print(sys.platform)
        elif choice == '8':
            print('*** Viktoria! ***')
        elif choice == '9':
            victorina()
        elif choice == '10':
            account()
        elif choice == '11':
            print(change_dir(input('Введите путь к новой рабочей директори: ')))
        elif choice == '12':
            print(save_dirlist())
        elif choice == '13':
            break
        else:
            print('Неверный пункт меню')