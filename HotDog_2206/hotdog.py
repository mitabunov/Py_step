"""
Здесь находятся строители хотдогов
"""

from functools import reduce

from product import IProduct
from ingredients import SauceIngredient
from ingredients import MeatIngredient
from ingredients import ToppingIngredient


class HotDog:
    """
    Описание хотдога
    """
    def __init__(self, name):
        self.name = name
        self.ingredients = ['булка']  # Обыкновенный список
        self.price = 200  # Стартовая цена пиццы

    def add_ingredient(self, ingredient: IProduct) -> None:
        """
        Добавляет переданный ингредиент в список ингредиентов
        """
        self.ingredients.append(ingredient)

    def get_price(self) -> int:
        """
        Возвращает итоговую стоимость хотдога, исходя из стартовой
        цены, а также стоимости её ингредиентов.
        """
        total_price = self.price
        for ingredient in self.ingredients[1:]:
            total_price += ingredient.price
        return total_price

    def __str__(self):
        return f"{self.name}: {', '.join(map(str, self.ingredients))}"


class HotDogBuilder:

    def __init__(self, name):
        self.hotdog = HotDog(name)  # Пустая булка
        self.sauce = SauceIngredient()  # Фабрика соусов
        self.meat = MeatIngredient()  # Фабрика мяса
        self.topping = ToppingIngredient()  # Фабрика топпингов

    def add_sauce(self, sauce: str) -> None:
        """
        Добавляет соус
        """
        sauce = self.sauce.create_ingredient(sauce)
        self.hotdog.add_ingredient(sauce)

    def add_meat(self, meat: str) -> None:
        """
        Добавляет мясо
        """
        meat = self.meat.create_ingredient(meat)
        self.hotdog.add_ingredient(meat)

    def add_topping(self, topping: str) -> None:
        """
        Добавляет топпинг
        """
        topping = self.topping.create_ingredient(topping)
        self.hotdog.add_ingredient(topping)

    def make_hotdog(self, sauce=None, meat=None, topping=None) -> HotDog:
        """
        Метод, собирающий хотдог в правильной последовательности
        """
        pass


class DeutschBuilder(HotDogBuilder):
    """
    Строитель немецкий бургер
    """
    def __init__(self, name='Немецкий'):
        super().__init__(name)

    def make_hotdog(self, sauce='кетчуп', meat='салями', topping='сыр') -> HotDog:
        self.add_sauce(sauce)
        self.add_topping(topping)
        return self.hotdog


class FrenchBuilder(HotDogBuilder):

    def __init__(self, name='Франкобургер'):
        super().__init__(name)

    def make_hotdog(self, sauce='кетчуп', meat='салями', topping='грибы') -> HotDog:
        self.add_sauce(sauce)
        self.add_meat(meat)
        self.add_topping(topping)
        return self.hotdog


class IndividualBuilder(HotDogBuilder):

    def __init__(self, name='Индибургер'):
        super().__init__(name)

    def make_hotdog(self, sauce=None, meat=None, topping=None) -> HotDog:
        self.add_sauce(sauce)
        self.add_meat(meat)
        self.add_topping(topping)
        return self.hotdog


class HotDogger:
    """
    Директор, который управляет строителями хотдогов
    """
    def __init__(self):
        self.builder = None

    def set_builder(self, builder: DeutschBuilder) -> None:
        self.builder = builder

    def make_hotdog(self, hotdog: str) -> HotDog:
        if hotdog == 'Немецкий':
            self.set_builder(DeutschBuilder())
            return self.builder.make_hotdog()
        elif hotdog == 'Франкобургер':
            self.set_builder(FrenchBuilder())
            return self.builder.make_hotdog()
        elif hotdog == 'Индибургер':
            self.set_builder(IndividualBuilder())
            sauce = input('Какой соус - кетчуп, горчица, майонез: ')
            meat = input('Какое мясо - баранина, свинина, салями: ')
            topping = input('Какой топпинг - сыр, огурцы, грибы: ')
            return self.builder.make_hotdog(sauce, meat, topping)