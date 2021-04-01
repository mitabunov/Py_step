# Задание 1. Дана строка string. Найти длину наибольшей подстроки, в которой нет повторяющихся букв.
# Пример:
# Вход: string = "abcabcbb", Выход: 3. Потому что подстрока "abc" с длиной 3
# Вход: string = "bbbbb", Выход: 1. Потому что подстрока "b" с длиной 1
# Вход: string = "pwwkew", Выход: 3. Потому что подстрока "wke" с длиной 3
# Вход: string = "", Выход: 0. Потому что подстрока "" с длиной 0
def length_of_longest_substring(s):
	pivot, slider, ans = 0,0,0
	lookup_table = set()

	n = len(s)
	while slider<n:
		if s[slider] not in lookup_table:
			lookup_table.add(s[slider])
			slider += 1
			ans = max(len(lookup_table), ans)
		else:
			lookup_table.remove(s[pivot])
			pivot += 1
		

	return ans


# Задание 2. Дан массив из чисел, найти такой подмассив, который содержит наибольшую сумму чисел и вернуть эту сумму.
# Вход: nums = [-2,1,-3,4,-1,2,1,-5,4], Выход: 6. Потому что у подмассива [4,-1,2,1] сумма 6
# Вход: nums = [1], Выход: 1. Потому что у подмассива [1] сумма 1
# Вход: nums = [5,4,-1,7,8], Выход: 23. Потому что у подмассива [5,4,-1,7,8] сумма 23
def max_sub_array(nums):
    if len(nums) == 1:
        return nums[0]

    total = nums[0]
    best = nums[0]

    for i in nums[1:]:
        if i > (total + i):
            total = i
        else:
            total += i

        best = max(best, total)

    return best

def main():
    # test_1
    print()
    print()
    print('# test_1')
    print()
    test_arr_strings = ['abcabcbb', 'bbbbb', 'pwwkew', '']

    for i in test_arr_strings:
        print(length_of_longest_substring(i))
        
    print('-----------------------------')
    # test_2
    print()
    print()
    print('# test_2')
    print()
    tes_arr_nums = [[-2,1,-3,4,-1,2,1,-5,4],[1],[5,4,-1,7,8]]
    for i in tes_arr_nums:
        print(max_sub_array(i))
    print('-----------------------------')
   

if __name__ == '__main__':
    main()

