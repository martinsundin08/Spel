import random as rand
import time as klockan_tickar
from Funky import *
from mantis_namn import *
from lootlist import *

class Loot():
    def __init__(self,itemname ,itemtype ,powerboost,hpboost ):
        self.itemname = itemname
        self.itemtype = itemtype
        self.powerboost = powerboost
        self.hpboost = hpboost

alive = True

Sword = Loot("svärd" ,"Weapond" ,1.2 ,0 )
Spear = Loot("spjut" ,"Weapond",1.4 ,0)
Chestplate = Loot("bröstplatta" ,"Armour",0 ,1.5)
Tank = Loot("Pansarvagn","Weapond" ,12 ,12)

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
           player.alive = False 
           print("Grattis, du klarade spelet!!")
    return player


def take_damage(Target, damage):   
    Target.hp -= damage
    if Target.hp <= 0:
        Target.hp = 0
        Target.alive = False
    return Target

def fight(player):
    mantis = Mantisar(rand.choice(mantis_namn), rand.randint(1,5), rand.randint(1,3),"dinmamma")
    total_damage = mantis.hp
    while player.alive and mantis.alive:
        take_damage(mantis, player.power)
        print(f"Du slog {mantis.name} och gjorde {player.power} skada. {mantis.name} har nu {mantis.hp} hp kvar.")
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
        else:
            pass
    return player


def heal(player):
    player.hp += 1
    if player.hp >= player.max_hp:
        player.hp = player.max_hp
    return player

def playerlootadd(player,loot):
    player.pungsäck.append(loot)
    player.power += loot.powerboost
    player.max_hp += loot.hpboost
    if len(player.pungsäck) > player.max_pungsäcksize:
        playerlootremove(player)
    else:
        pass
    return player

#player loot kanske ska se till att 


def playerlootremove(player):
    for i in range (len(player.pungsäck)):
        item = player.pungsäck[i]
        if item.itemtype == "Weapond":
            print(f"({i}) {item.itemname}et som har en skade boost på {item.powerboost}")
        elif item.itemtype == "Armour":
            print (f"({i}) din {item.itemname}an som har en hp boost på {item.hpboost}")
    
    print("Nu måste du ta bort en sak i ditt inventory för du har för mycket skit!!!")
    val = int(input())
    if val < 0:
        print("Snälladu skriv en av siffrorna bredvid dina items!!")
    elif val > len(player.pungsäck):
        print("Snälladu skriv en av siffrorna bredvid dina items!!")    
    else:
        player.pungsäck.pop((val))
    
    return player
 
def playerlootcheck(player):
    print(f"Du har {len(player.pungsäck)}st saker i ditt inventory och de sakerna är:")
    len(player.pungsäck)
    for i in range (len(player.pungsäck)):
                
        pungpop = player.pungsäck[i]
        if pungpop.itemtype == "Weapond":
            print(f"{i} Detta är ditt {pungpop.itemname} som har en skade boost på {pungpop.powerboost}")
        elif pungpop.itemtype == "Armour":
            print(f"{i}Detta är din {pungpop.itemname} som har en hp boost på {pungpop.hpboost}")
    return player
                
def lootchest (player):
    x = rand.choice(lootlist)
    playerlootadd(player,x)
    print(f"Wow, du hittade en skattkista och i skattkistan låg en/ett {x.itemname}!!")
    return player

def randportal(player):
    x = rand.randint(0,11)
    if x <= 8:
        fight(player)
    elif x > 8:
        lootchest(player)
    else:
        pass
    return player


def main():

    print("Välkommen till äventyrsspelet👍😢😃😎. Du kommer att navigera i en grotta, slåss" \
    " mot mantisar och samla skatter. \nMen se upp för satanisterna!")
    player_name = input("Nu får du skapa en karaktär. vad heter du?\n")
    
    while True:
        
            role_choise = input("Nu får du välja vilken klass du ska vara resten av spelet, du kan välja mellan pungråtta 1, Lennart Bladh 2 och fritidschefen 3!(skriv siffran efter för att välja roll.)")
            if role_choise == "1":
                Player1 = Player(player_name, 0.7, 5, 8, "pungråtta")
                break
            elif role_choise == "2":
                Player1 = Player(player_name, 1.4, 8, 5, "Lennart Bladh")
                break
            elif role_choise == "3":
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
            Player1 = playerlootcheck(Player1)
        elif val == "4":
            Player1 = heal(Player1)
            print(f"Du chillade galet och fick 1 hp {Player1.hp}")    
        elif val == "5":
            
            print(Player1.power)
            Player1 = playerlootadd(Player1, Spear)
            print(Player1.power)
            print(Player1.pungsäck)
        elif val == "6":
            Player1 = gain_xp(Player1, 1)
        elif val == "7":
            playerlootremove(Player1)
        elif val == "q":
            break
        else:
            print("Du måste välja något av valen i menyn")
        if not Player1.alive:
            print("Tyvärr dog du. Better luck next time buddy")
        else:
            pass
        
main()