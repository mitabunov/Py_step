from collections import deque 
# Ввести некоторое число и записать его цифры в стек, который нужно реализовать.
# Вывести это число из стека так, чтобы его цифры шли в обратном порядке.


class Stack:
    def __init__(self, chislo=None, chislo_l=None):
        self.chislo= chislo
        self.chislo_l =chislo_l
        
#     @staticmethod
    def make_arr(self,chislo):
    #     chislo = int(input())
        self.chislo_l = list(map(int,str(chislo)))
        return (self.chislo_l)
    
#     @staticmethod
    def make_outstack(self, chislo_l):

        self.chislo_l = chislo_l
        intStack = deque()

        for i in self.chislo_l:
            intStack.append(i)

        for _ in range(len(intStack)):
            print(intStack.pop())
        
def main():
    print('Введите число без пробелов:')
    chislo = int(input())
    chislo_l = Stack().make_arr(chislo)
    print(chislo_l)
    s_out = Stack().make_outstack(chislo_l)


if __name__ == '__main__':
    main()         

