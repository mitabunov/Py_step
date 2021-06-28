#!/usr/bin/env python3
"""
Задание 2. Пользователь с клавиатуры вводит путь к файлу. После чего запускаются
три потока. Первый поток заполняет файл случайными числами. Второй поток находит
все простые числа, а третий поток факториал каждого числа в файле. Результаты поиска
каждый поток должен записать в новый файл.

Подсказка: можно воспользоваться высокоуровневой библиотекой concurrent.futures для
создания пула потоков.

Нюансы реализации разрешаются программистом.
"""

import json
import random
import concurrent.futures


print('****************************************************')
print('* Будет создан список из 1_000_000 случайных чисел *')
print('****************************************************')
print()
PATH = str(input('Введите путь создания файла случайных чисел: '))
PATH_TO_PRIME = str(input('Введите путь создания файла простых чисел: '))
PATH_TO_FACTOR = str(input('Введите путь создания файла факториала чисел: '))

# PATH ="/home/mikhail/Py_step/Polystream_2906/1.txt"
# PATH_TO_PRIME ="/home/mikhail/Py_step/Polystream_2906/2.txt"
# PATH_TO_FACTOR ="/home/mikhail/Py_step/Polystream_2906/3.txt"


arr_rand_0= [random.randint(0,20) for _ in range(1000000)]


with open(PATH, 'w') as f:
    f.write(json.dumps(arr_rand_0))

with open(PATH, 'r') as f:
    arr_rand = json.loads(f.read())

print('From _ 1:', arr_rand, type(arr_rand))

def prime_num(arr_rand):
    l = []
    for num in arr_rand:
        if num > 1:
                for i in range(2,num):
                        if (num % i) == 0:
                                break
                else:
                        # print(num)
                        l.append(num)
    return l  

def write_prime_arr():       
    with open(PATH_TO_PRIME, "w") as f:
    # with open("/home/mikhail/Py_step/Polystream_2906/2.txt", "w") as f:

        print(prime_num(arr_rand), file=f)

def find_factorial(num):
    # определяем начальное значение факториала
    factorial=1
    # Если num является натуральным, то
    if(num%1==0 and num >= 0):
        # Вычисляем факториал числа num
        for i in range(1, num+1):
            factorial = i*factorial        
        return (f'{num}! = {factorial}')
    else:
        return ('Невозможно вычислить факториал нецелого и/или отрицательного числа!')

def arr_factorial(arr_rand):
    def find_factorial(num):
        # определяем начальное значение факториала
        factorial=1
        # Если num является натуральным, то
        if(num%1==0 and num >= 0):
            # Вычисляем факториал числа num
            for i in range(1, num+1):
                factorial = i*factorial        
            return (f'{num}! = {factorial}')
        else:
            return ('Невозможно вычислить факториал нецелого и/или отрицательного числа!')
    return [find_factorial(x) for x in arr_rand]

def write_arr_factorial():
    with open(PATH_TO_FACTOR, "w") as f:
        print(arr_factorial(arr_rand), file=f) 


def main():

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.map(write_prime_arr())
        executor.map(write_arr_factorial())
    print()
    print('*****************')
    print('* Файлы созданы *')
    print('*****************')

if __name__=='__main__':

    main()
#     