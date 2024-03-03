import time #Команда записи Интервала в начале.
print("Крестоносцы вновь нападают на Русские земли. Сможет ли Варяжское ополчение отбить атаку.")
time.sleep(5) #Команда интервала между выводом, пишется здесь после принта с описанием.
class Воин:
    def __init__(self, name, hp, damage):
        self.name = name #str
        self.hp = hp #int
        self.damage = damage #int
    def hit(self, Юнит):
        Юнит.hp -= self.damage
        if Юнит.hp > 0:
            print(f'"{self.name}" атаковал "{Юнит.name}". У "{Юнит.name}" осталось {Юнит.hp} здоровья')
        else:
            print(f'"{self.name}" атаковал "{Юнит.name}". "{Юнит.name}" убит')
            Юнит.hp = 0
        return Юнит.hp
 
from random import randint as rnd
 
Юнит1 = Воин('Варяг', 100, 20)
Юнит2 = Воин('Крестоносец', 100, 20)
Юниты = [Юнит1, Юнит2]
 
while True:
    attack_index = rnd(0,1) #Кто атакует
    target_index = (attack_index +1)%2 #Кого атакует
    target_hp = Юниты[attack_index].hit(Юниты[target_index])
    time.sleep(3) #Команда интервала между выводом, пишется здесь после индекса.
    if target_hp == 0:
        print(f'"{Юниты[attack_index].name}" Одержал Победу!')
        break
