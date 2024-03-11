import time #Команда записи Интервала в начале.
from random import randint as rnd

class Воин:
    def __init__(self, name, hp, damage):
        self.name = name #str
        self.hp = hp #int
        self.damage = damage #int
    def hit(self, Unit):
        Unit.hp -= self.damage
        if Unit.hp > 0:
            print(f'"{self.name}" атаковал "{Unit.name}". У "{Unit.name}" осталось {Unit.hp} здоровья')
        else:
            print(f'"{self.name}" атаковал "{Unit.name}". "{Unit.name}" убит')
            Unit.hp = 0
        return Unit.hp
 
Unit1 = Воин('Варяг', 100, 20)
Unit2 = Воин('Крестоносец', 100, 20)
Units = [Unit1, Unit2]

print("Крестоносцы вновь нападают на Русские земли. Сможет ли Варяжское ополчение отбить атаку.")
time.sleep(5) #Команда интервала между выводом, пишется здесь после принта с описанием.

while True:
    attack_index = rnd(0,1) #Кто атакует
    target_index = (attack_index +1)%2 #Кого атакует
    target_hp = Units[attack_index].hit(Units[target_index])
    time.sleep(3) #Команда интервала между выводом, пишется здесь после индекса.
    if target_hp == 0:
        print(f'"{Units[attack_index].name}" Одержал Победу!')
        break
