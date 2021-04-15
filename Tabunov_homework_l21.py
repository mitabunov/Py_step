"""
Реализовать иерархию классов согласно приложенной UML-диаграмме.
Она описывает упрощенные элементы популярной игры Counter-Strike,
в которой команда контер-террористов пытается предотвратить планы
террористов.

Есть абстрактный класс Character, от которого наследуются классы Terrorist
и CounterTerrorist. Помимо этого, есть абстрактный класс Gun, от которого
наследуются AK и M4, каждый из которых состоит в отношении агрегации
соответственно игровой роли (АК для террористов, М4 для контер-террористов).

Реализации стрельбы и перезарядки для каждого класса остаются на усмотрение
разработчика. При желании что-то можно добавить.

В личный кабинет приложить .py файл с реализацией или же ссылку на github
репозиторий.
"""

###


class Character:
    def __init__(self, health):
        self.health = health

    def shooting():
        pass
    def reloading():
        pass


class Gun:
    def __init__(self,ammo, shoot):

        self.ammo = ammo
        self.shoot = shoot
        
    def reloading(self, ammo):
        self.ammo = ammo
        print(self.ammo)
        
    def shooting(self):
        self.ammo -= shoot
        print(self.ammo)
        

class ContraTerroristo(Character):
    def __init__(self, health, ammo, shoot):

        self.health = health
        self.gun = M4(ammo, shoot)

    def shooting(self):
       
        self.gun.shooting()

    def reloading(self):
        
        self.gun.reloading(self)


class Terroristo(Character):
    def __init__(self, health, ammo, shoot):

        self.health = health
        self.gun = AK(ammo, shoot)

    def shooting(self):
        self.gun.shooting()

    def reloading(self):
        
        self.gun.reloading(self)


class M4(Gun):
    def __init__(self, ammo, shoot):
        
        self.ammo = ammo
        self.shoot = shoot

    def shooting(self):
        self.ammo -= 2
        


class AK(Gun):
    def __init__(self, ammo, shoot):
        super().__init__(ammo, shoot)
        self.ammo = ammo
        self.shoot = shoot

    def shooting(self):
        
        self.ammo -= 3
        print(self.ammo)


def main():
    
    c = ContraTerroristo(100, 30,3)
    t = Terroristo(95, 40,3)

    c.shooting()
    c.reloading()
    t.reloading()
    t.shooting()


if __name__ == "__main__":
    main()
