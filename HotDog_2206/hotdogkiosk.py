from typing import Union

from hotdog import HotDogger
from hotdog import HotDog
from client import Client


class HotDogFacade:
    """
    Фасад собакофабрики
    """
    def __init__(self):
        self.cook = HotDogger() 

    def cook_hotdog(self, hotdog: str) -> HotDog:
        """
        Возвращает готовый хот дог
        """
        return self.cook.make_hotdog(hotdog)

    def make_order(self, client: Client, hotdog: str) -> Union[None, HotDog]:
        """
        Обрабатывает заказ клиента
        """
        hotdog = self.cook_hotdog(hotdog)
        hotdog_cost = hotdog.get_price()
        client_money = client.get_money()
        if client_money >= hotdog_cost:
            return hotdog
        else:
            print(f'Не хватает денег! {hotdog.name} стоит: {hotdog_cost}, а у клиента {client_money}')
        
        