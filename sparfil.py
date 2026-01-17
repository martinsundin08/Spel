from Spel import *
from Funky import *

def save_file(player):
     f = open("spar_fil.txt", mode="w",encoding='utf-8')
     f.write(f"{player.name}-{player.power}-{player.max_hp}-{player.max_pungsäcksize}-{player.role}-{bool(player.alive)}-{player.pungsäck}-{player.hp}-{player.level}-{player.xp}")
     f.close()
     print("det har sparat nu")
     return
    



def save_file_open(player):
    f = open("spar_fil.txt")
    savelist = f.read().split("-")
    f.close()
    print(savelist)
    player.name = savelist[0]
    player.power = float(savelist[1])
    player.max_hp = float(savelist[2])
    player.max_pungsäcksize = int(savelist[3])
    player.role = savelist[4]
    player.alive = bool(savelist[5])
    player.pungsäck = list(savelist[6])
    player.hp = float(savelist[7])
    player.level = int(savelist[8])
    player.xp = int(savelist[9])
    
    return player
    