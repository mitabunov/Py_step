
#!/usr/bin/env python3
"""
Задание 1. При старте приложения запускаются три потока. Первый поток заполняет
список случайными числами. Второй поток находит сумму элементов списка,
а третий поток среднеарифметическое значение в списке. Полученный список, сумма и
среднеарифметическое выводятся на экран.
"""
import threading, random, time

# n=10
def rand_arr_gener(n):
    list_randint = [random.randint(-10,10) for _ in range(n)]
    return list_randint

# def rand_arr_summ(n):
#     print('Summa',sum(rand_arr_gener(n)))
#     return sum(rand_arr_gener(n))

def rand_arr_summ(list_randint):
    print('Summa',sum(list_randint))
    return sum(list_randint) 

def rand_arr_mean(list_randint):
    print('Mean', sum(list_randint)/len(list_randint))
    return (sum(list_randint)/len(list_randint))



def main():
    
    n=1000000
    list_randint = rand_arr_gener(n)
    start_time_0 = time.time()
 
    print(list_randint)
    # print(rand_arr_gener(n))
    print(rand_arr_summ(list_randint))
    print(rand_arr_mean(list_randint))
    end_time_0 = time.time()

    print('Цепочкой:', end_time_0 - start_time_0)

    # t1 = threading.Thread(target=rand_arr_gener, args=(n,))
    t2 = threading.Thread(target=rand_arr_summ, args=(list_randint,))
    t3 = threading.Thread(target= rand_arr_mean, args=(list_randint,))

    start_time_1 = time.time()
    # t1.start()
    t2.start()
    t3.start()
    # t1.join()
    t2.join()
    t3.join()
    end_time_1 = time.time()

    print('Многопоточность',end_time_1 - start_time_1)


if __name__=='__main__':
    main()    


