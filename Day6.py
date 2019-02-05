import random

class Person:     #(value               )
    def __init__(self, name, hp, mp, atk):  #define
        self.name = name
        self.hp = hp
        self.maxmp = mp
        self.maxhp = hp
        self.mp = mp
        self.atk_high = atk + 10      #own veriable
        self.atk_low = atk - 10
        self.action = ["physical Attack"]

    def stats(self):
        print(self.name)
        print(f"{self.hp}/{self.maxhp}")
        print(f"{self.mp}/{self.maxmp}")

    def generate_atk_damage(self):
        dmg = random.randint(self.atk_low, self.atk_high)
        return dmg

    def take_damage(self, dmg):
        self.hp = self.hp - dmg
        if self.hp < 0:
           self.hp = 0
        return self.hp

    def choose_action(self):
        index =  1
        print("ACTIONS: ")
        for element in self.action:
            print("{}. {}".format(index, element))
            index = index + 1
