"""
Реализовать программу для робота-пылесоса.

Робот-пылесос имеет три функции уборки:
1. Сухая уборка
2. Влажная уборка
3. Комбинированная уборка

Робот умеет переключаться между этими уборками в зависимости от типа
поверхности, на которой он находится в данный момент. Тип поверхности
высчитывается сам по коэффициенту трения coefficient_of_friction.

Каждый тип поверхности и соответствующий ему режим уборки задаётся
следующими условиями:
0 <= coefficient_of_friction < 10 -> плитка -> комбинированная уборка
10 <= coefficient_of_friction < 20 -> ламинат -> сухая уборка
20 >= coefficient_of_friction -> ковёр -> влажная уборка

Примечание: стоит посмотреть в сторону пройденных поведенческих паттернов.
Детали реализации остаются за программистом.
"""


class SurfaceClean(object):
    @staticmethod
    def cleaning(coefficient_of_friction):
        raise NotImplementedError()


class CombiCleaning(SurfaceClean):
    @staticmethod
    def cleaning(coefficient_of_friction):
        print ('Комбинированная уборка плитки')


class DryCleaning(SurfaceClean):
    @staticmethod
    def cleaning(coefficient_of_friction):
        print ('Сухая уборка ламината')


class DampCleaning(SurfaceClean):
    @staticmethod
    def cleaning(coefficient_of_friction):
        print ('Влажная уборка ковра')


class Hoover(object):
    @classmethod
    def make_clean(cls, coefficient_of_friction):
        try:
            if coefficient_of_friction <= 10:
                clean_type = CombiCleaning

            elif coefficient_of_friction >= int(11) and coefficient_of_friction <=int(20):
                clean_type = DryCleaning

            elif coefficient_of_friction >=21:
                clean_type = DampCleaning
          
            else:
                raise RuntimeErrorError('Выберите поверность для очистки %s' % coefficient_of_friction)

            byterange = clean_type.cleaning(coefficient_of_friction)
            return cls(byterange, coefficient_of_friction)
        
        except TypeError:
            print('Выберите поверность для очистки')
        except:
            print('Выберите поверность для очистки')            
    def __init__(self, byterange, coefficient_of_friction):
        self._byterange = byterange
        self._coefficient_of_friction = coefficient_of_friction


Hoover.make_clean(9)  
Hoover.make_clean(33)  
Hoover.make_clean(19)  
# Hoover.make_clean()

