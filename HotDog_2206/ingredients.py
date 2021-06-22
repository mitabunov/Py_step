"""
Здесь находятся фабрики ингредиентов.
"""

from abc import ABC, abstractmethod

from product import IProduct
from souseprice import AlfredoSauce
from souseprice import TomatoSauce
from souseprice import MayoSauce
from meatprice import BeefMeat
from meatprice import PorkMeat
from meatprice import SalamiMeat
from toppingprice import MushroomTopping
from toppingprice import CucumberTopping
from toppingprice  import ChiliTopping
from toppingprice  import CheeseTopping


class Ingredients(ABC):
    """
    Абстрактное описание фабрики ингредиентов
    """
    @abstractmethod
    def create_ingredient(self, ingredient: str) -> IProduct:
        ...


class SauceIngredient(Ingredients):
    """
    Фабрика соусов
    """
    def create_ingredient(self, ingredient: str) -> IProduct:
        if ingredient == 'горчица':
            return AlfredoSauce()
        elif ingredient == 'кетчуп':
            return TomatoSauce()
        elif ingredient == 'майонезный':
            return MayoSauce()


class MeatIngredient(Ingredients):
    """
    Фабрика мяса
    """
    def create_ingredient(self, ingredient: str) -> IProduct:
        if ingredient == 'баранина':
            return BeefMeat()
        elif ingredient == 'свинина':
            return PorkMeat()
        elif ingredient == 'салями':
            return SalamiMeat()


class ToppingIngredient(Ingredients):
    """
    Фабрика топпингов
    """
    def create_ingredient(self, ingredient: str) -> IProduct:
        if ingredient == 'грибы':
            return MushroomTopping()
        elif ingredient == 'огурцы':
            return CucumberTopping()
        elif ingredient == 'чили':
            return ChiliTopping()
        elif ingredient == 'сыр':
            return CheeseTopping()
