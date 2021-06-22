class Client:
    """Класс клиента"""
    def __init__(self, name, money):
        self.name = name
        self.money = int(money)

    def get_money(self):
        """Возвращает текущее количество денег"""
        return self.money

    def make_offer(self):
        print('1 - Немецкий бургер')
        print('2 - Французскийй бургер')
        print('3 - Обычный бургер')
        print('4 - Авторский бургер')
        return input('Какой хотдог делать?')    
