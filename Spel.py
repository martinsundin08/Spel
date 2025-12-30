import random as rand
import time as klockan_tickar
from loot import *
from mantis_namn import *

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

class Mantisar():
    def __init__(self, name, hp, power, loot):
        self.name = name
        self.hp = hp
        self.power = power
        self.loot = []
        self.alive = True




def pungsäckadd(Player1, a):
    Player1.pungsäck.append(a)
    return Player1

def pungsäcksizecontroll(Player1):
    if len(Player1.pungsäck) > Player1.max_pungsäcksize:
        Player1.alive = False
        return Player1
    else: 
        return Player1 

def take_damage(Target, damage):   
    Target.hp -= damage
    if Target.hp <= 0:
        Target.hp = 0
        Target.alive = False
    return Target

def fight(Player):
    mantis = Mantisar(rand.choice(mantis_namn), rand.randint(1,5), rand.randint(1,3))
    while Player.alive and mantis.alive:
        mantis = take_damage(mantis, Player.power)
        print(f"Du slog mantisen {mantis.name} och gjorde {Player.power} skada. Mantisen har nu {mantis.hp} hp kvar.")
        if mantis.alive:
            pass
    return


def heal(Player1):
    Player1.hp += 1
    if Player1.hp >= Player1.max_hp:
        Player1.hp = Player1.max_hp
    return Player1

def randportal():
    x = rand.randint(0,11)
    return x

# def lootroom():


def main():
    Svärd = Loot("svärd" ,1.2 ,1)
    Spjut = Loot("spjut" ,1.4 ,1)

    print (f"{Svärd.itemname}")
    print (f"{rand.choice(mantis_namn))


    
    print("Välkommen till äventyrsspelet. Du} kommer att navigera i en grotta, slåss" \
    " mot mantisar och samla skatter. \nMen se upp för satanisterna!")
    Player_name = input("Nu får du skapa en karaktär. vad heter du?\n")
    
    while True:
        
        role_choise = input("Nu får du välja vilken klass du ska vara resten av spelet, du kan välja mellan pungråtta 1, Lennart Bladh 2 och fritidschefen 3!(skriv siffran efter för att välja roll.)")
        if role_choise == "1":
            Player1 = Player(Player_name, 0.7, 5, 8, "pungråtta")
            break
        elif role_choise == "2":
            Player1 = Player(Player_name, 1.4, 8, 5, "Lennart Bladh")
            break
        elif role_choise == "3":
            Player1 = Player(Player_name, 1, 5, 2, "Fritidschefen")
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
            pass
            # if randportal >= 2:
            #     #skicka till mantis
            # else
            #     #skicka till skatt
            
        elif val == "2":
            print(f"""
                  


                      Halloj, {Player1.name}, just nu har du {Player1.hp} liv och din styrka är {Player1.power}


""")
            
        elif val == "3":
            Player1 = pungsäckadd(Player1, "leogiganorma")
            Player1 = pungsäcksizecontroll(Player1)
            print(len(Player1.pungsäck))
            print(Player1.pungsäck)
        
        elif val == "4":
            Player1 = heal(Player1)
            print(f"Du chillade galet och fick 1 hp {Player1.hp}")    
        elif val == "5":
            klockan_tickar.sleep(60)
        elif val == "q":
            break
        else:
            print("Du måste välja något av valen i menyn")
        
main()
print("Spelet är slut.")