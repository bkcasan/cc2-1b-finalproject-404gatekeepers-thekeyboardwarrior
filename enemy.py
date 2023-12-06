# enemy.py

import random

class Enemy:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def take_damage(self, damage):
        self.health -= max(0, damage - self.defense)

    def attack_player(self):
        return max(0, self.attack + random.randint(-2, 2))

    def is_alive(self):
        return self.health > 0

class A(Enemy):
    def __init__(self):
        super().__init__(name="$", health=30, attack=10, defense=5)

class B(Enemy):
    def __init__(self):
        super().__init__(name="%", health=100, attack=20, defense=15)

class C(Enemy):
    def __init__(self):
        super().__init__(name="!", health=25, attack=15, defense=8)
