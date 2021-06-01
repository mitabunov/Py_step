"""
Создайте приложение для приготовления пасты. Приложение должно уметь
создавать минимум три вида пасты. Классы различной пасты должны иметь
следующие методы:

- Тип пасты;
- Соус;
- Начинка;
- Добавки.

Для реализации используйте любой из пройденных порождающих паттернов.
Для упрощения проверки, в комментарии к коду  напишите название выбранного
паттерна.
"""


from enum import Enum
import time

PastaProgress = Enum('PastaProgress', 'queued preparation baking ready')
PastaDough = Enum('PastaSize', 'long short shallow')
PastaSauce = Enum('PastaSauce', 'tomato creme_fraiche pesto bolon cheesen')
PastaTopping = Enum('PastaTopping', 
                    'mozzarella double_mozzarella bacon parmezzano red_onion champignon oregano')
PastaFilling = Enum('PastaFilling', 
                    'salt pepper oleooliva vine')
STEP_DELAY = 1

class pastaPic:
    PIC = u"\U0001F35D"
    PIC_PIG = u"\U0001F43D"
    PIC_SIZE = u"\u27A1"

class Pasta:
    def __init__(self, name):
        self.name = name
        self.dough = None
        self.sauce = None
        self.topping = []
        self.filling = None

    def __str__(self):
        return self.name

    def prepare_dough(self, dough):
        self.dough = dough
        print(f'Готовятся {self.dough.name} макаронины для {self}...')
        time.sleep(STEP_DELAY)
        print(f'Готовы {self.dough.name} макаронины')

class CarbonareBuilder:
    def __init__(self):
        self.pasta = Pasta('carbonare')
        self.progress = PastaProgress.queued
        self.baking_time = 1

    def prepare_dough(self):
        self.progress = PastaProgress.preparation
        self.pasta.prepare_dough(PastaDough.long)

    def add_sauce(self):
        print('Добавление tomato sauce в carbonare...')
        self.pasta.sauce = PastaSauce.tomato
        time.sleep(STEP_DELAY)
        print('Добавлен tomato sauce')

    def add_topping(self):
        topping_desc = 'double mozzarella, oregano'
        topping_items = (PastaTopping.double_mozzarella, PastaTopping.oregano)
        print(f'Добавлена начинка ({topping_desc}) в Карбонаре')
        self.pasta.topping.append([t for t in topping_items])
        time.sleep(STEP_DELAY)
        print(f'Добавлены ({topping_desc})')

    def add_filling(self):
        filling_desc = 'salt, pepper, oleooliva, vine'
        filling_items = (PastaTopping.salt, PastaTopping.oleooliva)
        print(f'Добавлена добавка ({filling_desc}) в Карбонаре')
        self.pasta.filling.append([t for t in filling_items])
        time.sleep(STEP_DELAY)
        print(f'Готово с добавкой ({filling_desc})')   
        
    def bake(self):
        self.progress = PastaProgress.baking
        print(f'Карбонара приготовится через {self.baking_time} секунд')
        time.sleep(self.baking_time)
        self.progress = PastaProgress.ready
        print('Карбонара готова')

        
class BoloniezzeBuilder:
    def __init__(self):
        self.pasta = Pasta('Boloniezze')
        self.progress = PastaProgress.queued
        self.baking_time = 1 # in seconds for the sake of the example

    def prepare_dough(self):
        self.progress = PastaProgress.preparation
        self.pasta.prepare_dough(PastaDough.short)

    def add_sauce(self):
        print('Добавляем томатный соус в болоньезе...')
        self.pasta.sauce = PastaSauce.tomato
        time.sleep(STEP_DELAY)
        print('Добавлен томатный соус')

    def add_topping(self):
        topping_desc = 'double mozzarella, oregano'
        topping_items = (PastaTopping.double_mozzarella, PastaTopping.oregano)
        print(f'Добавляем начинку ({topping_desc}) в болоньезе')
        self.pasta.topping.append([t for t in topping_items])
        time.sleep(STEP_DELAY)
        print(f'Начинка ({topping_desc}) добавлена')
        
    def add_filling(self):
        filling_desc = 'salt, pepper, oleooliva, vine'
        filling_items = (PastaTopping.salt, PastaTopping.pepper)
        print(f'Добавлена добавка ({filling_desc}) в Карбонаре')
        self.pasta.filling.append([t for t in filling_items])
        time.sleep(STEP_DELAY)
        print(f'Готово с добавкой ({filling_desc})') 

    def bake(self):
        self.progress = PastaProgress.baking
        print(f'Приготовится через {self.baking_time} секунд')
        time.sleep(self.baking_time)
        self.progress = PastaProgress.ready
        print('Болоньезэ!')

        
class MakaronenBuilder:
    def __init__(self):
        self.pasta = Pasta('Makaronen')
        self.progress = PastaProgress.queued
        self.baking_time = 7 # in seconds for the sake of the example

    def prepare_dough(self):
        self.progress = PastaProgress.preparation
        self.pasta.prepare_dough(PastaDough.shallow)

    def add_sauce(self):
        print('Добавление crème fraîcheв в вермишельку')
        self.pasta.sauce = PastaSauce.creme_fraiche
        time.sleep(STEP_DELAY)
        print('Добавлен crème fraîcheв в вермишельку')

    def add_topping(self):
        topping_desc = 'mozzarella, bacon, red_onion, oregano'
        topping_items =  (PastaTopping.mozzarella,
                          PastaTopping.bacon,
                          PastaTopping.red_onion, 
                          PastaTopping.oregano)
        print(f'Добавлены ({topping_desc}) в вермишелечку')
        self.pasta.topping.append([t for t in topping_items])
        time.sleep(STEP_DELAY)
        print(f'Добавлены добавки ({topping_desc})')
        
    def add_filling(self):
        filling_desc = 'salt, pepper, oleooliva, vine'
        filling_items = (PastaTopping.salt, PastaTopping.pepper)
        print(f'Добавлена добавка ({filling_desc}) в вермишель!')
        self.pasta.filling.append([t for t in filling_items])
        time.sleep(STEP_DELAY)
        print(f'Готово с добавкой ({filling_desc})') 
        
    def bake(self):
        self.progress = PastaProgress.baking
        print(f'Хрючево будет готово через {self.baking_time} мгновений')
        time.sleep(self.baking_time)
        self.progress = PastaProgress.ready
        print(f'{pastaPic.PIC_PIG}Ваше хрючево готово!')

        
class Waiter:
    def __init__(self):
        self.builder = None

    def construct_pasta(self, builder):
        self.builder = builder
        steps = (builder.prepare_dough, 
                 builder.add_sauce, 
                 builder.add_topping, 
                 builder.bake)
        [step() for step in steps]

    @property
    def pasta(self):
        return self.builder.pasta

        
def validate_style(builders):
    try:
        input_msg = 'Какую пасту приготовить? [b]oloniezze, [m]akaronen или [с]arbonara? '
        pasta_style = input(input_msg)
        builder = builders[pasta_style]()
        valid_input = True
    except KeyError:
        error_msg = 'Извините, доступны только клавиши [b], [m], [c]'
        print(error_msg)
        return (False, None)
    return (True, builder)

    
def main():
    builders = dict(b = BoloniezzeBuilder, m = MakaronenBuilder, c = CarbonareBuilder)
    valid_input = False
    while not valid_input:
        valid_input, builder = validate_style(builders)
    print()
    waiter = Waiter()
    waiter.construct_pasta(builder)
    pasta = waiter.pasta
    print()
    print(f'{pasta}{pastaPic.PIC}, сэр!')

    
if __name__ == '__main__':
    main()

