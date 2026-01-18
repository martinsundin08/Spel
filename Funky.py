# class Loot():
#     def __init__(self,itemname ,itemtype ,powerboost,hpboost ):
#         self.itemname = itemname
#         self.itemtype = itemtype
#         self.powerboost = powerboost
#         self.hpboost = hpboost



class Mantisar():
    def __init__(self, name, hp, power, loot):
        self.name = name
        self.hp = hp
        self.power = power
        self.loot = []
        self.alive = True


#    Arkivering av gammal eller viktig kod

# def pungsäckadd(player, a):
#     player.inventory.append(a)
#     return player

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

# def fight(Player1):
#     mantis = Mantisar(rand.choice(mantis_namn), rand.randint(1,5), rand.randint(1,3),"dinmamma")
#     while Player1.alive and mantis.alive:
#         take_damage(mantis, Player1.power)
#         print(f"Du slog {mantis.name} och gjorde {Player1.power} skada. {mantis.name} har nu {mantis.hp} hp kvar.")
#         klockan_tickar.sleep(0)
#         if mantis.alive:
#             Player1 = take_damage(Player1, mantis.power)
#             print(f"{mantis.name} slog dig och gjorde {mantis.power} skada. Du har nu {Player1.hp} hp kvar.")
#             klockan_tickar.sleep(0)
#         elif not mantis.alive: 
#             print(f"Du har besegrat {mantis.name}!")
#         elif not Player1.alive:
#             print(f"Du har dött av {mantis.name}!")
#         else:
#             pass
#     return Player1

# def gain_xp(Player1, xp):
#     Player1.xp += xp  
#     print(f"Du fick {xp} xp! Du har nu {Player1.xp} xp!")
#     if Player1.xp >= 10 * Player1.level:
#         Player1.level += 1
#         Player1.xp -= 10 * Player1.level
#         print(f"Grattis, Du har nått nästa level. Du är nu level {Player1.level}!")
#     return Player1

   # if val == "1":
    #     print(f"Du poppade nyss {player.itemname}")
    #     player.pungsäck.pop(0)
    # elif val == "2":
    #     player.pungsäck.pop(1)
    # elif val == "3":
    #     player.pungsäck.pop(2)
    # elif val == "4":
    #     player.pungsäck.pop(3)
    # elif val == "5":
    #     player.pungsäck.pop(4)
    # elif val == "6":
    #     player.pungsäck.pop(5)
    # elif val == "7":
    #     player.pungsäck.pop(6)
    # elif val == "8":
    #     player.pungsäck.pop(7)
    

    # def Playerlootkanskekingfix(Player1):
#     for i in Player1.pungsäck:
#         Playerlootadd(Player1,i)
#         print(i)
#     return Player1


# def pungsäcksizecontroll(player):
#     if len(player.pungsäck) > player.max_pungsäcksize:
#         player.alive = False
#         return player
#     else: 
#         return player 