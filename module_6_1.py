from classes.superclass.subclass.mammal import Mammal
from classes.superclass.subclass.predator import Predator
from classes.superclass.subclass.flower import Flower
from classes.superclass.subclass.fruit import Fruit


if __name__ == '__main__':
    a1 = Predator('Волк с Уолл-Стрит')
    a2 = Mammal('Хатико')
    p1 = Flower('Цветик семицветик')
    p2 = Fruit('Заводной апельсин')

    print(a1.name)
    print(p1.name)

    print(a1.alive)
    print(a2.fed)
    a1.eat(p1)
    a2.eat(p2)
    print(a1.alive)
    print(a2.fed)