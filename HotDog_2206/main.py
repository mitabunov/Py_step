#!/usr/bin/env python3


from hotdogkiosk import HotDogFacade
from client import Client


def main():
    hotdogkiosk = HotDogFacade()
    client = Client('Шариков', 1000)  # Сообщение о нехватке денег и исключение в print'е
    

    hotdog = hotdogkiosk.make_order(client, 'Немецкий')
    print(hotdog, hotdog.get_price())  # Распечатаем состав пиццы и её цену

    hotdog = hotdogkiosk.make_order(client, 'Франкобургер')
    print(hotdog, hotdog.get_price())

    hotdog = hotdogkiosk.make_order(client, 'Индибургер')
    print(hotdog, hotdog.get_price())


if __name__ == '__main__':
    main()
