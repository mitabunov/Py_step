"""
Задача на взаимодействие между классами. Разработать систему «Интернет-магазин».

ТОВАРОВЕД добавляет информацию о ТОВАРЕ. КЛИЕНТ делает и оплачивает ЗАКАЗ на ТОВАРЫ.
ТОВАРОВЕД регистрирует ПРОДАЖУ.

Каждое слово, написанные выше в верхнем регистре - отдельный класс, то есть их всего 5:
товаровед, товар, клиент, заказ, продажа.

Вся остальная реализация остаётся на усмотрение разработчика. Главное, чтобы на выходе
получилась программа, демонстрирующая связь между пятью классами, которая описана во
втором абзаце.

Подсказка: можно сделать так, чтобы у ТОВАРОВЕДА был список со всеми доступными ТОВАРАМИ,
а также список с осуществлёнными ПРОДАЖАМИ, который является списком ЗАКАЗОВ.
"""



"""
Работает только вот с такими костылями
Если предварительно прописать эти функции.

Сами по себе они работают нормально, но в классах я не могу пришить их как надо.
"""


products = ['Apple', 'Tiramussu', 'Prada', 'Mochnato']# наименования
amounts  = [27, 38, 17, 40] # количество
prices = [11,33,66,99] # цена

prod_serrss = ['Apple', 'Prada', 'Mochnato', 'Tiramissu'] # заказ по наименованию
n_n = [10,20,30,40] # заказ по количеству наименований

price_list = list(zip(products, amounts,prices))
prod_ser = 'Prada' #  искомый продукт


def product(products, amounts, prices):
    price_list = list(zip(products, amounts,prices))
    return price_list
price_list_1 = product(products, amounts, prices)

price_list_1
prod_ser = 'Prada'

def search_product(prod_ser, price_list):
    order_ind = [(n,x.index(prod_ser)) for n,x in enumerate(price_list) if str(prod_ser) in x]
    print(f'Найдено: {prod_ser}, цена: {prices[order_ind[0][0]]}, кол-во: {amounts[order_ind[0][0]]}')
    return order_ind[0][0]

s_p = search_product(prod_ser, price_list_1)


def sale(price_list_1, amounts, n):
#     new_amount = price_list[0][1]-n
    amounts[s_p] = amounts[s_p] - n
#     price_list.insert(1, new_amount)
#     price_list.insert(1, new_amount)
#     price_list[0][1] =new_amount
    
    return amounts

# sale(price_list_1, amounts, 5)

def sale_out_list(price_list, amounts, n):
    try:
        amm_new = sale(price_list,amounts,n)
        if amm_new[s_p] <=0:
            del products[s_p]
        price_list_new = list(zip(products, amm_new,prices))
        return price_list_new
    except IndexError:print('Нет в наличии')
s_o_l=sale_out_list(price_list_1, amounts, 11)
print(s_o_l)

def add_basket(prod_ser,price_list, n):
    sum_order = []
#     sum_order.append(price_list[search_product(prod_ser)][0])
    sum_order.append(price_list[s_p][2] * n)
    # sum_order.append(price_list[2][1]*3)
    return prod_ser, sum(sum_order)

print(add_basket('Apple', price_list_1, 10), add_basket('Prada', price_list_1, 5))

def order_final(prod_ser,price_list, n):
    
    order = []
    order += add_basket(prod_ser, price_list, n)

    return order

def sum_order(prod_serrss, n_n):
    return [(order_final(prod_ser,price_list, n)[1])
             for n in n_n]

sum_order_final= sum(sum_order(prod_serrss, n_n))
sum_order_final
       



products = ['Apple', 'Tiramussu', 'Prada', 'Mochnato']
amounts  = [27, 38, 17, 40]
prices = [11,33,66,99]

prod_serrss = ['Apple', 'Prada', 'Mochnato', 'Tiramissu']
n_n = [10,20,30,40]

"""
Но если вышенаписанные функции закомментировать, то файл будет работать с ошибкой
Классы не видят функций других классов
"""



class Product:
    def __init__(self, products, amounts, prices):
        self.products=products
        self.amounts=amounts
        self.prices=prices
        
    def make_price_list(self, products, amounts,prices):
        price_list = list(zip(products, amounts,prices))
        return price_list
    
class Client(Product):
    def __init__(self, prod_ser, price_list, n):
        self.prod_ser = prod_ser
        self.price_list = price_list
        self.n = n
    
    def search_product(self, prod_ser, price_list):
        '''
            Функция поиска продукта
            @ prod_ser : наимевание продукта
            @ price_list : база для поиска
            return : индекс искомого продукта
        '''
        order_ind = [(n,x.index(self. prod_ser)) for n,x in enumerate(self.price_list) if str(self.prod_ser) in x]
        print(f'Найдено: {prod_ser}, цена: {prices[order_ind[0][0]]}, кол-во: {amounts[order_ind[0][0]]}')
        return order_ind[0][0]
    
    def add_basket(self,prod_ser,price_list, n):
        '''
            Функция добавления продукта
            @ prod_ser : наимевание продукта
            @ price_list : база для поиска
            @ n : количество
            return : имя продукта, сумму заказа по подукту
        '''        
        sum_order = []
    #     sum_order.append(price_list[search_product(prod_ser)][0])
#         s_p = ProductExpert(prod_ser, price_list,5).search_product(self,prod_ser, price_list)
        s_p = self.search_product(self,prod_ser, price_list)
        
        sum_order.append(price_list[s_p][2] * n)
        # sum_order.append(price_list[2][1]*3)
        return prod_ser, sum(sum_order)
    
class Order(Product):
    
    def order_make(self, prod_serrss,n_n):
        '''
            Функция поиска продукта
            @ prod_serrss : список заказанных продуктов 
            @ n_n : список количеств заказанных продуктов
            return :  словарь >>> наименование: количество
        '''        
        count_list = dict(zip(prod_serrss, n_n))
        return count_list
        
    
    def order_final(self,prod_ser,price_list, n):
        '''
            Функция конесного заказа по количеству
            @ prod_ser : наимевание продукта
            @ price_list : база для поиска
            @ n : количество
            return : список заказанных продуктов
        '''          
        order = []
        order += add_basket(prod_ser, price_list, n)

        return order

    def sum_order(self,prod_serrss, n_n):
        '''
            Функция конечной суммы заказа
            @ prod_serrss : список заказанных продуктов 
            @ n_n : список количеств заказанных продуктов
            return :  список >>> суммы по заказанным продуктам
        '''        
        return [(order_final(prod_ser,price_list, n)[1])
                 for n in n_n]

class Sale:
    def sale(self, price_list, amounts, n):
        '''
            Функция уменьшения количества продукта в базе
            @ price_list : прайс лист
            @ amounts: количество продукта в базе
            @ n : количество заказанного продукта
            return :  количество оставшегося продукта 
        '''        
        amounts[s_p] = amounts[s_p] - n   
        return amounts

    # sale(price_list_1, amounts, 5)

    def sale_out_list(self, price_list, amounts, n):
        '''
            Функция обновления базы продуктов
            @ price_list : прайс лист
            @ amounts: количество продукта в базе
            @ n : количество заказанного продукта
            return :  обновленн 
        ''' 
        try:
            amm_new = sale(price_list,amounts,n)
            if amm_new[s_p] <=0:
                del products[s_p]
            price_list_new = list(zip(products, amm_new,prices))
            return price_list_new
        except IndexError:print('Нет в наличии')    
          
    
class ProductExpert(Client, Order, Sale):
    pass



def main():
#     price_list_1 = product(products, amounts, prices)
#     s_p = search_product(prod_ser, price_list_1)
    print(Product(products, amounts,prices).make_price_list(products, amounts,prices))
    print(ProductExpert(prod_ser, price_list, 100).order_make(prod_serrss,n_n))
    s_p = ProductExpert(prod_ser, price_list,5).search_product(prod_ser, price_list)
#     print(ProductExpert(prod_ser, price_list,5).add_basket(prod_ser, price_list,5))
    print(Order(price_list, amounts, 5).order_final(prod_ser,price_list, 5))
    print(Order(price_list, amounts, 5).sum_order(prod_serrss, n_n))
    print(ProductExpert(prod_ser, price_list, 5).sum_order(prod_serrss, n_n))
    print(Sale().sale(price_list, amounts, 5))
    print(Sale().sale_out_list(price_list, amounts, 5))


if __name__ == '__main__':
    main()




