"""
self 必须是类内函数的第一个参数，必须有
"""

import random


class Creature:
    def __init__(self, c_name, c_hp):
        self.name = c_name
        self.hp = c_hp

    def attack(self):
        force = random.randint(1, 50)
        return force

    def be_attacked(self, hp):
        self.hp -= hp

    def show_hp(self):
        print(self.name, self.hp)

    def is_dead(self):
        if self.hp <= 0:
            return True
        else:
            return False


me = Creature('me', 100)
enemy = Creature("enemy", 80)

while True:
    me.show_hp()
    enemy.show_hp()

    input_str = input("attack or defense(a/d): ")
    if input_str == 'a':
        me_force = me.attack()
        enemy_force = enemy.attack()
        me.be_attacked(enemy_force)
        enemy.be_attacked(me_force)
    elif input_str == 'd':
        enemy_force = enemy.attack()
        enemy.be_attacked(10)
        me.be_attacked(enemy_force)

    if me.is_dead() or enemy.is_dead():
        me.show_hp()
        enemy.show_hp()
        break

if me.dead():
    print('*' * 30 + ' lose')
else:
    print('*' * 30 + ' success')

