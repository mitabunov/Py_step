"""
Домашнее задание:

1. (Необязательно) Послушать "Научно-технический реп - Полиморфизм"

2. (Обязательно) Реализовать классы и потомки по следующей схеме:

Класс Vehicle (средство передвижения).
У объектов класса Vehicle есть поля:
working_engine - с момента создания равно False, является обозначением того, заведен двигатель или нет

У объектов класса Vehicle есть методы:
start - выводит надпись "Двигатель заведен", если working_engine False и меняет его на True
move - выводит надпись "Средство передвижения едет", если working_engine True
stop - вывод надпись "Двигатель остановлен", если working_engine True и меняет его на False

У класса Vehicle есть потомки:
Tank - танк
Car - машина
Boat - надувная лодка

У объектов класса Tank есть поля:
count_ammo - с момента создания равно 10, боезапас танка

У объектов класса Tank есть методы:
move - выводит надпись "Гусиницы заскрипели от движения", если working_engine True, иначе выдаёт надпись "Нужно завести двигатель"
shoot - выводит надпись "Танк выстрелил" и уменьшает count_ammo на 1, если count_ammo > 0, иначе выдаёт надпись "Снаряды кончились"

У объектов класса Car есть поля:
fuel - с момента создания равно 100, топливо машины

У объектов класса Car есть методы:
start - выводит надпись "Двигатель машины заведён", если working_engine False, и меняет его на True. Если fuel <= 0, выдаёт надпись "Бензина нет"
move - выводит надпись "Машина поехала" и уменьшает fuel на 10, если working_engine True, иначе выдаёт надпись "Машина не заведена",
если fuel во время езды станет <= 0, тогда вывести надпись "Машина заглохла" и установить working_engine на False

У объектов класса Boat есть поля:
air_pressure - с момента создания равно 100, давление воздуха внутри лодки

У объектов класса Boat есть методы:
start - выводит надпись "Мотор лодки гудит", если working_engine False, и меняет его на True. Если если air_pressure <= 0, выдаёт надпись "Лодка тонет!" и двигатель не заводится
move - выводит надпись "Лодка плывёт", если working_engine True, и уменьшает air_pressure на 10, иначе выдаёт надпись "Мотор лодки не заведен"

Все объекты классов никаких дополнительных параметров на вход не получают, то есть их классы вызываются с пустыми скобками.
У классов-потомков только один родитель - Vehicle.

Прочие методы и дополнения остаются на ваше усмотрение.
"""

#pip install emoji --upgrade

import emoji as em
from colorama import Fore, Back, Style


class bcolors:
#         HEADER = '\033[95m'
        HEADER = Style.BRIGHT
        
        OKGREEN = '\033[92m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        UNDERLINE = '\033[4m'
        LIGHTGRAY = "\033[37m"
        EXPLOSION = em.emojize(':fire:', language='en')
        TANK = em.emojize(':video_game:', language='en')
        CAR =  u"\U0001F690"
#         SHOOTEND = em.emojize(':red_circle:', language='en')
        SHOOTEND = u"\U0001F626"
        BOAT = em.emojize(':speedboat:')
        SWIMM = em.emojize(':droplet:')
#         DRIVING = em.emojize(':smile:')
        DRIVING =  u"\u27A1"
        START = em.emojize('/play wups',language='en')

class Vehicle:
    def __init__(self, working_engine=False):
        self.working_engine = working_engine

    def start(self):
        if self.working_engine == False:
            print(f'Двигатель заведен {bcolors.START}')
            self.working_engine = True

    def move(self):
        if self.working_engine == True:
            print('Средство передвижения едет')

    def stop(self):
        if self.working_engine == True:
            print('Двигатель остановлен')
            self.working_engine = False

print(f'{bcolors.HEADER}Vehicle:{bcolors.ENDC}')
car1 = Vehicle()
car1.start()
car1.move()
car1.stop()

class Tank(Vehicle):
    def __init__(self, working_engine=False, count_ammo=10):
        self.count_ammo = count_ammo
        super().__init__(working_engine)

    def move(self):
        if self.working_engine == True:
            print("Гусеницы заскрипели от движения")
        else:
            print("Нужно завести двигатель")

    def shoot(self):
        if self.count_ammo <= 0:
            print(f"Снаряды кончились :( {bcolors.SHOOTEND}", self.count_ammo)
        else:
#             print("Танк выстрелил", self.count_ammo )
            print(f"Танк выстрелил {bcolors.EXPLOSION*self.count_ammo}", self.count_ammo)
            self.count_ammo -= 1

print()
print(f'{bcolors.HEADER}Tank:{bcolors.TANK}{bcolors.ENDC}')
tank1 = Tank()
tank1.start()
tank1.move()
for i in range(0,11):
    tank1.shoot()



class Car(Vehicle):
    def __init__(self, working_engine=False, fuel=100):
        super().__init__(working_engine)
        self.fuel = fuel

    def start(self):
        if self.fuel <= 0:
            print("Бензина нет")
        else:
            if self.working_engine == False:
                print("Двигатель машины заведен")
                self.working_engine = True

    def move(self):
        if self.working_engine == True:
            print(f"Машина поехала{bcolors.DRIVING * (self.fuel//10)}", self.fuel)
            self.fuel -= 10
        if self.fuel <= 0:
            print(f"Машина заглохла :({bcolors.SHOOTEND}", self.fuel)
            self.working_engine = False


print()
print(f'{bcolors.HEADER}Car:{bcolors.CAR}{bcolors.ENDC}')
car1 = Car()
car1.start()
for i in range(0,100,10):
    car1.move()

class Boat(Vehicle):
    def __init__(self, working_engine=False, air_pressure=100):
        super().__init__(working_engine)
        self.air_pressure = air_pressure

    def start(self):
        if self.air_pressure <= 0:
            print("Лодка тонет и двигатель не заводится")
        else:
            if self.working_engine == False:
                print("Мотор лодки гудит")
                self.working_engine = True

    def move(self):
        if self.working_engine == True:
            print(f"Лодка плывет{bcolors.SWIMM * (self.air_pressure//10)}", self.air_pressure)
            self.air_pressure -= 10

            if self.air_pressure <= 0:
                self.working_engine = False
                print(f"Лодка тонет и двигатель не заводится :( {bcolors.SHOOTEND}")
        else:
            print("Мотор лодки не заведен")



print()
print(f'{bcolors.HEADER}Boat:{bcolors.BOAT}{bcolors.ENDC}')
boat1 = Boat()
boat1.start()

for i in range(0,100,10):
    boat1.move()
