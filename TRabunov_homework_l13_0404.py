"""
Общие указания по домашней работе.

Для начала посмотреть это видео о PEP8 (всего 3 минуты):
https://www.youtube.com/watch?v=hgI0p1zf31k

Задачи ниже на оценку. Есть дополнительная задача на плюс к скиллу:
Выложить решение в личный кабинет в виде проекта с виртуальным окружением,
из-под которого будет возможно запустить код с решениями задач.
"""
import random

# Задача 1.
# Напишите алгоритм вывода чисел Фибоначчи до n-ого члена.
# Числа Фибоначчи – это последовательность, где каждое следующее число
# после 1 является суммой двух ему предшествующих. То есть ряд чисел
# Фибоначчи выглядит так: 1, 1, 2, 3, 5, 8, 13, 21…
#
# Пример.
# Для n=5 вывод будет таким: 1, 1, 2, 3, 5
# Для n=4 вывод будет таким: 1, 1, 2, 3
# Для n=2 вывод будет таким: 1, 1
def get_fib(n: int) -> str:  
    f1 = f2 =1
    print(f1,f2, end=', ')

    i = 2
    while i < n:
        f1, f2 = f2, f1+f2
        print(f2, end=', ')
        i +=1


# Задача 2.
# Дан отсортированный по возрастанию массив из чисел и число target. Написать
# функцию, которая возвращает индекс числа target в массиве, если оно там есть.
# Если его там нет, тогда функция возвращает индекс, где это число должно стоять
# в массиве, если бы его туда вставляли, не нарушая порядок сортировки.
#
# Пример.
# На вход: nums = [1,3,5,6], target = 5
# Выход: 2
#
# На вход: nums = [1,3,5,6], target = 2
# Выход: 1
#
# На вход: nums = [1,3,5,6], target = 7
# Выход: 4
#
# На вход: nums = [1,3,5,6], target = 0
# Выход: 0
#
# На вход: nums = [1], target = 0
# Выход: 0
def get_index(lst_nums, target):

    """
    Функция сравнивает два списка
    @ lst_nums : исследуемый список
    @ target: искомое число
    return : индекс запращиваемого числа
    """ 
    
    if target == 0:
        lst_nums.insert(0, target)
        print(lst_nums.index(target))
        

    elif target in lst_nums:
        print(lst_nums.index(target))

    elif target not in lst_nums:
        ind_i = [i for i in lst_nums if i<target]
    #     lst_nums.insert(target-1, target)
        ind_targ = ind_i[-1]
        t_i = int(lst_nums.index(ind_targ))
        lst_nums.insert(t_i+1, target)
        print(t_i+1,lst_nums)
    #     print(lst_nums.index(target), lst_nums)
    else:
        pass


# Задача 3.
# Дан массив из чисел от 1 до 100. В нём пропущено одно число. Найти это число.
def get_skipped_num(num_del):
    """
    Функция сравнивает два списка
    @ nums_etalon : список содержащий все числа
    @ num_del : список с пропущенным числом
    return : пропущенное число
    """
    result = [x for x in nums_etalon  if x not in num_del]
    return result

def main():
    # test_1
    print()
    print('test #1---------------')
    n_lst = [5,4,2,66,'11',11]
    try:
        for i in n_lst:
            print("/n",get_fib(i))
    except (TypeError ):
        print('Только инты !! Не строка >>>', i, 'Индекс в списке >>>',n_lst.index(i))

    #test_2
    print()
    print('test #2---------------')
    targ_lst = [3, 12, 102, 0]
    lst_nums = [1,3,5,6,10,100]

    # проверяем есть число из targ_lst в списке lst_nums
    print(lst_nums)
    for i in targ_lst:
        get_index(lst_nums, i)

    #test_3
    print()
    print('test #3---------------')
    nums_etalon = list(range(100))

    # сделаем список со случайно удаленным числом
    num_del = nums_etalon.copy()
    randnum=random.randrange(0,len(nums_etalon)) 
    num_del.pop(randnum)
    # randnum, len(nums_etalon),len(num_del)

    # сравним два списка
    print(get_skipped_num(num_del), randnum)


# "Запускатр" нашей программы. Оставить не тронутым.
if __name__ == '__main__':
    main()
