import math


def area(r):
    '''Находит произведение числа pi на удвоенное число поданное на вход
    
            Параметры:
                r (int) - радиус круга
                
            Возвращаемое значение:
                math.pi * r * r: Найденная площадь круга с радиусом r
    
    '''
    return math.pi * r * r


def perimeter(r):
    return 2 * math.pi * r

