from typing import Any
import re
from collections import Counter


# Решить задачи, выложить .py файл с решениями на github. В личный кабинет прикрепить .txt файл с ссылкой на репозиторий.


# Задача 1. Найти количество различных элементов массива. Пример: для [1 4 5 1 1 3] ответ 4.
def count_unique_elems(arr) -> int:
    return len(set(arr))


# Задача 2. Дан файл с логинами и паролями. Найдите топ10 самых популярных паролей.
# Ссылка на файл: https://yadi.sk/i/6ywJqzm93HGmy9
PATH = '/home/mikhail/Рабочий стол/Py_step/pwd.txt'

def del_s(lstt):
    """
    Функция очистки списка
    @ lstt : список
    return : очищенный список
    """
    for i in lstt:
        if i == '':
            lstt.remove(i)
    return lstt

def spl_str(xx_11):
    """
    Функция подготовки списка
    @ xx_11 : список
    return : измененный список
    """
    for i in xx_11:
    #     print(type(i))
        i.split(';')
    return xx_11  

def get_10_popular_password(PATH):
    """
    Функция для подсчета самых популярных паролей
    @ PATH : путь к файлу
    return : топ 10 самых популярных паролей
    """
    xx = open(PATH, 'r').read().split('\n')
    xx_1 = xx.copy()
    xx_fin = [re.split(', ', i) for i in xx_1] # сделаем чероновой список
    lstt = [i for i in xx_fin]
    xx_11 = del_s(xx_1) # очистим от пустых элементов
    xx_12 = spl_str(xx_11) # сделаем очищенный список
    xx_13 = dict(x.split(';')[:2] for x in xx_12) # сделаем словарь "е-мэйл:пароль"
    count_list_passw = Counter(xx_13.values()) 

    return count_list_passw.most_common(10) # вывод самых популярных 


# Задача 3. Дана строка с ссылками. Заменить все ссылки на ***** (5 звёздочек).
# Примеры ссылок:
# www.site.com заменится на *****
# http://example.su заменится на *****
# vk.ru заменится на *****
# https://example.com/smth/else заменится на *****
# и т.д.
# Чем больше разных вариантов будет придумано, тем лучше, но без фанатизма.
# Для простоты, ограничьте набор доменов верхнего уровня (штуки 4-7 достаточно).
def filter_domen(string, substr):
    """
    Функция вычленяет из строки список субстрок
    @ string : список субстрок строки
    @ substr : список частей субстроки
    return : список субстрок для замены
    """
    return [str for str in string if any(sub in str for sub in substr)]

def change_substring(substring, str_new, change_lst):
    """
    Функция меняет субстроку в строке по условию
    @ substring : список субстрок
    @ str_new : список субстрок для замены
    @ change_lst : на что меняем
    return : измененную строку
    """
    for index,item in enumerate(substring):
        if item in str_new:
            substring[index] = change_lst.pop(0) # меняем ("пеpекидываем") субстроку на значение из листа замены
    return (' ').join(substring) 

def censor_link(string):
    """
    Функция меняет субстроку в строке по условию
    @ string : строка для изменения
    return : измененную строку
    """
    
    string_lst = string.split(' ') # из строки делаем список из субстрок
    substr_domen = ['com','su','ru','io', 'gov'] # список с частями субстрок для фильтра
    str_new = filter_domen(string_lst, substr_domen) # список из субстрок для изменения
    change_lst = list(['****'])*len(str_new) # лист значений для замены

    return change_substring(string_lst, str_new, change_lst) 
#     str_out = change_substring(string_lst, str_new, change_lst)
#     return str_out
    


# Здесь писать тесты для функций с решениями
def main():
    # test_1
    print()
    print()
    print('# test_1')
    print()
    arr_lst = [1, 4, 5, 1, 1, 3], [0, 0, 0, 0,0, 0], [1,2,3], ['str', str, 'str', 1,1]

    for i in arr_lst:
        print(count_unique_elems(i))
    print('-----------------------------')
    # test_2
    print()
    print()
    print('# test_2')
    print()
    print(get_10_popular_password(PATH))
    print('-----------------------------')
    #test_3
    print()
    print()
    print('# test_3')
    print()
    str_in = 'В этой строке доменные адреса www.site.com, www.mitabunov.github.io, tabunov.gov, http://example.su, vk.ru, https://example.com/smth/else заменятся на *****'
    print(str_in)
    print(censor_link(str_in))


if __name__ == '__main__':
    main()
