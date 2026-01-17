import random as rand
import time as klockan_tickar
import json as json
from Funky import *
from mantis_namn import *
from lootlist import *
from sparfil import *


class Loot():
    def __init__(self,itemname ,itemtype ,powerboost,hpboost ):
        self.itemname = itemname
        self.itemtype = itemtype
        self.powerboost = powerboost
        self.hpboost = hpboost

    def to_dict(self):
        return {
          "itemname": self.itemname,
          "itemtype": self.itemtype,
          "powerboost": self.powerboost,
          "HPboost": self.hpboost
        }

    @classmethod
    def from_dict(cls, d):
        return cls(
            d["itemname"],
            d["itemtype"],
            d.get("powerboost", 0),
            d.get("hpboost", d.get("HPboost", 0))
        )


Sword = Loot("svärd" ,"Weapond" ,1.2 ,0 )
Spear = Loot("spjut" ,"Weapond",1.4 ,0)
Chestplate = Loot("bröstplatta" ,"Armour",0 ,1.5)
Tank = Loot("Pansarvagn","Weapond" ,12 ,12)
lootlist = []


for i in range (33):
    lootlist.append(Spear)

for i in range (33):
    lootlist.append(Sword)
for i in range (33):
    lootlist.append(Chestplate)
lootlist.append(Tank)


print(f"{Tank.itemname},{Tank}")
print(f"{Spear.itemname},{Spear}")
print(f"{Chestplate.itemname},{Chestplate}")
print(f"{Sword.itemname},{Sword}")

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
    
    def to_dict(self):
        sackItems = []
        for i in range(len(self.pungsäck)):
            sackItems.append(self.pungsäck[i].to_dict())

        return {
          "name": self.name ,
          "power": self.power ,
          "max_hp": self.max_hp ,
          "max_pungsäcksize": self.max_pungsäcksize,
          "role": self.role,
          "alive": self.alive,
          "pungsäck": sackItems,
          "hp": self.hp,
          "level": self.level,
          "xp": self.xp
     }

    @classmethod
    def from_dict(cls, d):
        p = cls(
            d["name"],
            d["power"],
            d["max_hp"],
            d["max_pungsäcksize"],
            d["role"],
        )
        p.alive = d.get("alive", True)
        p.hp = d.get("hp", p.max_hp)
        p.level = d.get("level", 0)
        p.xp = d.get("xp", 0)

        p.pungsäck = [Loot.from_dict(item) for item in d.get("pungsäck", [])]

        if p.hp > p.max_hp:
            p.hp = p.max_hp

        return p
    
lootlist = []
for i in range (33):
    lootlist.append(Spear)

for i in range (33):
    lootlist.append(Sword)
for i in range (33):
    lootlist.append(Chestplate)
lootlist.append(Tank)

def pungsäckadd(player, a):
    player.pungsäck.append(a)
    return player


    
def gain_xp(player, xp):
    player.xp += xp  
    print(f"Du får {xp} xp efter fighten! Du har nu {player.xp} xp!")
    if player.xp >= 10 * player.level:
        player.level += 1
        player.xp = 0
        print(f"Grattis, Du har nått nästa level. Du är nu level {player.level}!")
        if player.level == 5: 
           print("Grattis, du klarade spelet!!")
           exit(0)
    return player

def take_damage(Target, damage):   
    Target.hp -= damage
    if Target.hp <= 0:
        Target.hp = 0
        Target.alive = False
    return Target

def fight(player):
    mantis = Mantisar(rand.choice(mantis_namn), rand.randint(1,5), rand.randint(1,3),"")
    total_damage = mantis.hp
    while player.alive and mantis.alive:
        take_damage(mantis, player.power)
        print(f"Du slog {mantis.name} och gjorde {player.power} skada. {mantis.name} har nu {mantis.hp:.1f} hp kvar.")
        klockan_tickar.sleep(0)
        if mantis.alive:
            player = take_damage(player, mantis.power)
            print(f"{mantis.name} slog dig och gjorde {mantis.power} skada. Du har nu {player.hp} hp kvar.")
            klockan_tickar.sleep(0)
        elif not mantis.alive: 
            print(f"Du har besegrat {mantis.name}!")
            gain_xp(player, total_damage)
        elif not player.alive:
            print(f"Du har dött av {mantis.name}!")
            print("Better luck next time BUDDY!!")
            exit(0)
        else:
            pass
    return player


def heal(player):
    player.hp += 1

    if player.hp >= player.max_hp:
        player.hp = player.max_hp

    return player

def playerlootadd(player,loot):
    if len(player.pungsäck) >= player.max_pungsäcksize:
        playerlootremove(player)
    else:
        pass
    player.pungsäck.append(loot)
    player.power += loot.powerboost
    player.max_hp += loot.hpboost
    return player


 

def playerlootremove(player):
    for i in range (len(player.pungsäck)):
        item = player.pungsäck[i]
        if item.itemtype == "Weapond":
            print(f"({i}) {item.itemname}et som har en skade boost på {item.powerboost}")
        elif item.itemtype == "Armour":
            print (f"({i}) din {item.itemname}an som har en hp boost på {item.hpboost}")
    print("Nu måste du ta bort en sak i ditt inventory för du har för mycket skit!!!")
    while True:
        val = input()
        if val.isdigit() == False:
            #isdigit hittas på formelbladet, så ingen ai här johannes🤗
            print("Snälladu skriv en av siffrorna bredvid dina items!!")
        elif int(val) < 0:
            print("Snälladu skriv en av siffrorna bredvid dina items!!")
        elif int(val) > len(player.pungsäck):
            print("Snälladu skriv en av siffrorna bredvid dina items!!") 
        else:
            player.power -= (player.pungsäck[int(val)]).powerboost
            player.max_hp -= (player.pungsäck[int(val)]).hpboost
            player.pungsäck.pop(int(val))
            break
        

    return player
 
def playerlootcheck(player):
    print(f"Du har {len(player.pungsäck)} st saker utav {player.max_pungsäcksize} i ditt inventory och de sakerna är:")
   
    for i in range (len(player.pungsäck)):     
        lootitem = player.pungsäck[i]
        if lootitem. itemtype == "Weapond":
            print(f"{i}  ditt {lootitem.itemname} som har en skade boost på {lootitem.powerboost}")
        elif lootitem.itemtype == "Armour":
            print(f"{i} din {lootitem.itemname} som har en hp boost på {lootitem.hpboost}")

    return player
                
def lootchest (player):
    x = rand.choice(lootlist)
    print(f"Wow, du hittade en skattkista och i skattkistan låg en/ett {x.itemname}!!")
    playerlootadd(player,x)
    return player

def randportal(player):
    x = rand.randint(0,11)
    if x <= 8:
        fight(player)
    else:
        lootchest(player)

    return player

def main(): 
    print("Välkommen till äventyrsspelet👍😢😃😎. Du kommer att navigera i en grotta, slåss" \
        " mot mantisar och samla skatter. \nMen se upp för satanisterna!")
    
    player_name = input("Nu får du skapa en karaktär. vad heter du?\n")
    
    print("Nu får du välja vilken klass du ska vara resten av spelet, du kan välja mellan pungråtta 1, Lennart Bladh 2 och fritidschefen 3!\n(skriv siffran efter för att välja roll.)\n")
    
    while True:
        role_choice = input()

        if role_choice == "1":
            Player1 = Player(player_name, 0.7, 5, 8, "pungråtta")
            break

        elif role_choice == "2":
            Player1 = Player(player_name, 1.4, 8, 5, "Lennart Bladh")
            break

        elif role_choice == "3":
            Player1 = Player(player_name, 1, 5, 2, "Fritidschefen")
            break

        else:
            print("Esnella välj en siffra mellan 1 och 3")

    print(f"Halloj {Player1.name}, du valde klassen {Player1.role}")


    while Player1.alive:
            print("Vad vill du göra?")

            val = input(""" 
                        1. Gå genom portal  2. Kolla stats
                        3. Öppna Pungsäck   4. vila
                        q. Avsluta spelet
                    """)
        
            if val == "1":
                Player1 = randportal(Player1)

            elif val == "2":
                print(f"""
                    


                        Halloj, {Player1.name}.\n   Just nu har du {Player1.hp} liv och din styrka är {Player1.power}.\n    Du har {Player1.xp} xp och är i level {Player1.level}.
                        
                """)
                
            elif val == "3":
                print(Player1.pungsäck) 
                Player1 = playerlootcheck(Player1)

            elif val == "4":
                Player1 = heal(Player1)
                print(f"Du chillade galet och fick 1 hp {Player1.hp}") 

            elif val == "5":
                save_test(Player1)
            elif val == "6":
                Player1 = load_save_file(Player)
            elif val == "7":
                Player1 = playerlootadd(Player1,Spear)
            elif val == "8":
                pass

            elif val == "q":
                exit(0)
            else:
                print("Du måste välja något av valen i menyn")
            

if __name__ == "__main__":
    main()
