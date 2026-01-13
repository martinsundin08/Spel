import random as rand
import time as klockan_tickar
from Funky import *
from mantis_namn import *
Sword = Loot("svärd" ,"Weapond" ,1.2 ,0 )
Spear = Loot("spjut" ,"Weapond",1.4 ,0)
chestplate = Loot("bröstplatta" ,"Armour",0 ,1.5)



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

def fight(Player1):
    mantis = Mantisar(rand.choice(mantis_namn), rand.randint(1,5), rand.randint(1,3),"dinmamma")
    while Player1.alive and mantis.alive:
        take_damage(mantis, Player1.power)
        print(f"Du slog {mantis.name} och gjorde {Player1.power} skada. {mantis.name} har nu {mantis.hp} hp kvar.")
        klockan_tickar.sleep(0)
        if mantis.alive:
            Player1 = take_damage(Player1, mantis.power)
            print(f"{mantis.name} slog dig och gjorde {mantis.power} skada. Du har nu {Player1.hp} hp kvar.")
            klockan_tickar.sleep(0)
        elif not mantis.alive: 
            print(f"Du har besegrat {mantis.name}!")
        elif not Player1.alive:
            print(f"Du har dött av {mantis.name}!")
        else:
            pass
    return Player1


def heal(Player1):
    Player1.hp += 1
    if Player1.hp >= Player1.max_hp:
        Player1.hp = Player1.max_hp
    return Player1

def Playerlootadd(Player1,loot):
    Player1.pungsäck.append(loot)
    Player1.power += loot.powerboost
    Player1.max_hp += loot.hpboost
    return Player1

#player loot kanske ska se till att 

def Playerlootkanskekingfix(Player1):
    for i in Player1.pungsäck:
        Playerlootadd(Player1,i)
        print(i)
    return Player1

def randportal():
    x = rand.randint(0,11)
    return x

# def lootroom():

def gain_xp(Player1, xp):
    Player1.xp += xp  
    print(f"Du fick {xp} xp! Du har nu {Player1.xp} xp!")
    if Player1.xp >= 10 * Player1.level:
        Player1.level += 1
        Player1.xp = 0
        print(f"Grattis, Du har nått nästa level. Du är nu level {Player1.level}!")
    return Player1

    

def main():

    
    print("Välkommen till äventyrsspelet. Du kommer att navigera i en grotta, slåss" \
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
            Player1 = fight(Player1)     
            # if randportal >= 2:
            #     #skicka till mantis
            # else
            #     #skicka till skatt
            
        elif val == "2":
            print(f"""
                  


                      Halloj, {Player1.name}, just nu har du {Player1.hp} liv och din styrka är {Player1.power}

            """)
            
        elif val == "3":
            print(f"Du har {len(Player1.pungsäck)}st saker i ditt inventory och de sakerna är:")
            len(Player1.pungsäck)
            for i in range (len(Player1.pungsäck)):
                print(len(Player1.pungsäck))
                pungpop = Player1.pungsäck.pop(0)
                print(pungpop.itemname)
                print(i)
        
        elif val == "4":
            Player1 = heal(Player1)
            print(f"Du chillade galet och fick 1 hp {Player1.hp}")    
        elif val == "5":
            
            print(Player1.power)
            Player1 = Playerlootadd(Player1, Spear)
            print(Player1.power)
            print(Player1.pungsäck)
        elif val == "6":
            Player1 = gain_xp(Player1, 1)
        elif val == "q":
            break
        else:
            print("Du måste välja något av valen i menyn")
        if not Player1.alive:
            print("Tyvärr dog du. Better luck next time buddy")
        else:
            pass
        
main()