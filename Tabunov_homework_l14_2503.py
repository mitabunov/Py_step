import numpy as np
import random

# Задание 1. Даны два списка: num1, num2 (размеры любые). Напечатать их медиану.
def median(num1, num2):
    lst = num1 + num2
    sortedLst = sorted(lst)
    lstLen = len(lst)
    index = (lstLen - 1) // 2

    if (lstLen % 2):
        return sortedLst[index]
    else:
        return (sortedLst[index] + sortedLst[index + 1])/2.0


# Задание 2. Дана строка s, вернуть наибольшую подстроку-палиндром в строке s. Если их будет несколько,
# вернуть первую попавшуюся.
# Пример: s = "babad", вывод: "bab"
# Пример: s = "cbbd", вывод: "bb"
# Пример: s = "a", вывод: "a"
# Пример: s = "ac", вывод: "a"
def longestPalindrome(S: str) -> str:

    n = len(S)
    max_length = 0
    for i in range(n):
        for j in range(i+1, n+1):
            substring = S[i:j]
            lsub = len(substring)
            if substring[:lsub//2]==substring[:lsub//2:-1]:
                if lsub >= max_length:
                    longest_palindrome = substring
                    max_length = lsub
    return longest_palindrome

# Задание 3. Дан список из строк. Вывести наибольший префикс для этих строк. Если такого префикса нет,
# вывести пустую строку.
# Пример: strs = ["flower","flow","flight"], вывод: "fl"
# Пример: strs = ["dog","racecar","car"], вывод: ""
def longest_common_prefix(strs):
    if strs:
        first = strs[0]
        if len(first) > 0 and len(strs) > 1:
            rest = strs[1:]
            for i in range(0, len(first)):
                for str in rest:
                    if i >= len(str) or first[i] != str[i]:
                        return first[:i]
        return first
    else:
        return ""


def main():
    # test_1
    print()
    print('------test_1-------')

    randrange = random.randint(0,10)
    num1 = list(map(lambda _: random.randint(0, 10), range(randrange)))
    num2 = list(map(lambda _: random.randint(0, 10), range(randrange)))
    num_all = num1+num2
    num_med_np = np.median(num_all) 
    print(num1, num2, num_all, num_med_np)
    num_med_def = median(num1, num2)
    print(bool(num_med_def == num_med_np))
    
    #test_2
    print()
    print('------test_2-------')

    print(longestPalindrome("aabcdcb"))
    print(longestPalindrome("bananas"))
    print(longestPalindrome("pad"))

    #test_3
    strs = [['100', '10', '1000'],["flower","flow","flight"],["dog","racecar","car"]]
    print()
    print('------test_3-------')


    for i in strs:
        print(longest_common_prefix(i))    

if __name__ == '__main__':
    main()
