from menu import make_directory, delete_file_dir, change_dir, save_dirlist
from os import path, mkdir, rmdir, getcwd
import json


def test_make_directory():
    assert make_directory('delme') == 'Папка успешно создана', 'Test failed!'
    assert path.exists('delme'), 'Test failed!'

    rmdir('delme')


def test_delete_file_dir():
    mkdir('delme')
    assert ('delme') == 'Файл(папка) успешно удален!', 'Test failed!'
    assert ('delme') == 'Такого объекта не сущестует!', 'Test failed!'


def test_change_dir():
    if path.exists(path.join(getcwd(), 'delme')):
        rmdir('delme')
    mkdir('delme')
    fpath_start = getcwd()
    fpath_end = path.join(getcwd(), 'delme')
    assert change_dir('delme') == f'Вы перешли в деректорию: {fpath_end}', 'Test failed!'
    assert change_dir('..') == f'Вы перешли в деректорию: {fpath_start}', 'Test failed!'
    rmdir('delme')
    assert change_dir('delme') == 'Нет такой директории! Попробуйте еще раз.', 'Test failed!'


def test_save_dirlist():
    if not path.exists(path.join(getcwd(), 'delme')):
        mkdir('delme')
    assert save_dirlist() == 'Содержимое директории успешно записано в файл dir_list', 'Test failed!'
    if path.exists('dir_list'):
        with open('dir_list', 'r', encoding='utf-8') as f:
            dirlist_data = json.load(f)
    assert 'delme' in dirlist_data['dirs'], 'Test failed!'
    rmdir('delme')