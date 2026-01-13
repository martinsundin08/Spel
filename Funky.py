class Loot():
    def __init__(self,itemname ,itemtype ,powerboost,hpboost ):
        self.itemname = itemname
        self.itemtype = itemtype
        self.powerboost = powerboost
        self.hpboost = hpboost


class Player():
    def __init__(self, name, power, max_hp, max_pungsäcksize, role):
        self.name = name
        self.power = power
        self.max_hp = max_hp 
        self.max_pungsäcksize = max_pungsäcksize
        self.role = role
        self.alive = True
        self.pungsäck = []
        self.hp = max_hp 
        self.level = 0
        self.xp = 0

class Mantisar():
    def __init__(self, name, hp, power, loot):
        self.name = name
        self.hp = hp
        self.power = power
        self.loot = []
        self.alive = True

# class Roller_stats():
#     def __init__(self, start_kraft, start_liv, start_pungsäck):
#         self.kraft = start_kraft
#         self.liv = start_liv
#         self.start_pungsäck = start_pungsäck

# pungråtta = Roller_stats(0.7, 1, 8)

# lennart_bladh = Roller_stats(1.4, 1.5, 5)

# fritidschefen = Roller_stats(1, 1, 2)


#     try:
#         val = int(input("hur många gånger ???"))
#         print(val * 10)
#     except:
#         print("sluta!")