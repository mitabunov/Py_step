"""
Описать класс «домашняя библиотека». Предусмотреть возможность
поиска книги по какому-либо признаку, например, по автору или по
году издания (признаки придумать самому), добавление книг в библиотеку,
удаления книг из нее, сортировки книг по разным полям (придумать самому
по каким).

Подсказка: задачу просто решить, если помимо класса "домашняя библиотека"
будет ещё и класс "Книга" со всеми соответствующими полями.

Вся реализация и разные "придумки" остаются на усмотрение разработчика.
"""

class Books:
    def __init__(self, name_b, author_b, year_b):

        self.name_b = name_b
        self.author_b = author_b
        self.year_b = year_b

    def bookmake_0(self, name_b, author_b, year_b):
#     '''
#     Функция создает объекты
#     @ name_b : имя
#     @ author_b : автор
#     @ year_b : год издания 
#     return : словарь
#     '''

        self.data = {}       
        self.data[str(name_b)] = {
            "author": str(author_b),
            "year": int(year_b)
        }
        return self.data
    
    def __repr__(self):
        return repr((self.name_b, self.author_b, self.year_b))

class Stack(Books):
    def __init__(self):
        self.stack = []
        self.max = None

    def pop(self, item):
        self.stack.pop(item)
    
    def push(self, item):
        self.stack.append(item)

    def get_sort_year(self): 
#     '''
#     Функция сортировки по году
#     return : отсортированный список
#     ''' 
        sorted_stack = sorted(self.stack, key=lambda book: book.year_b)
        return sorted_stack
    
    def get_sort_name(self): 
#     '''
#     Функция сортировки по названию
#     return : отсортированный список
#     '''  
        sorted_stack = sorted(self.stack, key=lambda book: book.name_b)
        return sorted_stack
    
    def get_sort_author(self):
#     '''
#     Функция сортировки по автору
#     return : отсортированный список
#     '''   
        sorted_stack = sorted(self.stack, key=lambda book: book.author_b)
        return sorted_stack
    
    def find_author(self, author):
#     '''
#     Функция поиска по автору
#     return : список авторов
#     ''' 
        authors = [x for x in self.stack if x.author_b == str(author)]
        return authors
    
    def find_year_release(self, year):
#     '''
#     Функция поиска по году году выпуска
#     return : список по условию
#     ''' 
        years = [x for x in self.stack if x.year_b == int(year)]
        return years
    
    def find_books(self, book):
#     '''
#     Функция поиска по названию
#     return : список
#     ''' 
        books = [x for x in self.stack if x.name_b == str(book)]
        return books
    
    def del_author(self,author):
#     '''
#     Функция удаления по автору
#     @ author : строка 
#     return : обновленный список
#     ''' 
        # получим список индексов книг для удаления   
        serch = [self.stack.index(x) for x in self.stack if x.author_b == str(author)]
        while len(serch) != 0:
            for i in serch:
                self.stack.pop(i) # удаляем согласно списку индексов
            return self.stack
    
    
    def del_book(self,name):
#     '''
#     Функция удаления по названию книги
#     @ name : строка 
#     return : обновленный список
#     '''        
        serch = [self.stack.index(x) for x in self.stack if x.name_b == str(name)]
        while len(serch) != 0:
            for i in serch:
                self.stack.pop(i)
            return self.stack
        

        
    def __repr__(self):
        return repr(self.stack)


def main():
    # создадим книги
    b = Books('День', 'Темных Д.А', 2037)
    b0 = Books('Вечер','Темных Д.А', 1940)
    b1 = Books('Вечер', 'Светлых Н.Е', 1837)
    b2 = Books('Сумерки', 'Порри Гаттер', 2051)
    b3 = Books('Сумрак', 'Светлых Н.Е', 2101)
    b4 = Books('Ночь', 'Ночников Г.Ы', 2101)
    b5 = Books('Рассвет', 'Порри Гаттер', 2102)
    # repr(b),repr(b0)
    arr_books = [b,b0,b1,b2,b3,b4,b5]
    #print(arr_books)

    # создадим нашу "библиотеку"
    s = Stack()
    for i in arr_books:
        s.push(i)
    # type(s)
    print(repr(s))

    print()
    print('*******Сортировка по году***********')
    print(s.get_sort_year())

    print()
    print('********Сортировка по автору**********')
    print(s.get_sort_author())

    print()
    print('********Сортировка по названию**********')
    print(s.get_sort_name())

    print()
    print('Поиск по автору')
    print(s.find_author('Темных Д.А'))
    print('====================')
    print()
    print('Поиск по году')
    print(s.find_year_release(2101))
    print('====================')
    print()
    print('Поиск по названию')
    print(s.find_books('Вечер'))
    print()
    print('.........Удаление по названию........')
    print(s.del_book('Вечер'))
    print(s.del_book('Вечер'))

    print('.........Удаление по автору........')
    print(s.del_author('Порри Гаттер'))
    print(s.del_author('Порри Гаттер'))


if __name__ == '__main__':
    main()
