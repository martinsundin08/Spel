import json


def save_game(player):
     with open("savefile.json", mode = "w", encoding='utf-8') as write_file:
          json.dump(player.to_dict(), write_file, indent = 3, ensure_ascii=True)


def load_save_file(PlayerClass):
     
     with open("savefile.json", mode = "r", encoding = "utf-8") as read_file:
          data = json.load(read_file)
          
     return PlayerClass.from_dict(data)


#arkivering av gammla sparfunktioner som inte använde sig av json, de funkade bra utom inventoriet

# def save_file(player):
#      f = open("spar_fil.txt", mode="w",encoding='utf-8')
#      sackItems = ",".join(str(element) for element in str(player.pungsäck))
#      f.write(f"{player.name}-{player.power}-{player.max_hp}-{player.max_pungsäcksize}-{player.role}-{bool(player.alive)}-{player.pungsäck}-{player.hp}-{player.level}-{player.xp}")
#      f.close()
#      print("det har sparat nu")
#      return

# def player(player):
#      player_data = {
#           "name": player.name ,
#           "power": player.power ,
#           "max_hp": player.max_hp ,
#           "max_pungsäcksize": player.max_pungsäcksize,
#           "role": player.role,
#           "alive": player.alive,
#           "pungsäck": player.pungsäck,
#           "hp": player.hp,
#           "level": player.level,
#           "xp": player.xp
#      }
#      loot_data = {
#           "itemname": Loot.itemname,
#           "itemtype": Loot.itemtype,
#           "powerboost": Loot.powerboost,
#           "HPboost": Loot.hpboost
#      }

#      with open("savefile.json", mode = "w", encoding='utf-8') as write_file:
#           json.dump(player_data,loot_data, write_file, indent = 3)

# def to_dict(self):
#      return {
#           "name": self.name ,
#           "power": self.power ,
#           "max_hp": self.max_hp ,
#           "max_pungsäcksize": self.max_pungsäcksize,
#           "role": self.role,
#           "alive": self.alive,
#           "pungsäck": self.pungsäck,
#           "hp": self.hp,
#           "level": self.level,
#           "xp": self.xp
#      }
# def to_dict(self):
#      return {
#           "itemname": self.itemname,
#           "itemtype": self.itemtype,
#           "powerboost": self.powerboost,
#           "HPboost": self.hpboost
#      }

# def new_try_saving (player):
#      json.dump(player, indent=2)

# def save_file_open(player):
#     f = open("spar_fil.txt")
#     savelist = f.read().split("-")
#     f.close()
#     print(savelist)
#     print(savelist[6])
#     pungsäckfix3 = savelist.pop(6)
#     print(savelist)
#     print(savelist[6])
#     player.name = savelist[0]
#     player.power = float(savelist[1])
#     player.max_hp = float(savelist[2])
#     player.max_pungsäcksize = int(savelist[3])
#     player.role = savelist[4]
#     player.alive = bool(savelist[5])
#     player.hp = float(savelist[6])
#     player.level = int(savelist[7])
#     player.xp = int(savelist[8])
#     player.pungsäck = []
#     print(pungsäckfix3)
#     tecken_som_ska_bort = ("[")
#     tecken_som_ska_bort1 = ("]")
#     pungsäckfix2 = pungsäckfix3.replace(tecken_som_ska_bort, "")
#     pungsäckfix21 = pungsäckfix2.replace(tecken_som_ska_bort1, "")
#     print(pungsäckfix21)
#     x = pungsäckfix21.split(", ")
#     print(x)
#     player = inventory_fix_for_loading(player,x)
    
    
#     return player
    

# def inventory_fix_for_loading(player, list):
#      for i in range (len(list)):
#           print(list[i])
#           if list[i] == "<Spel.Loot object at 0x000001CB402DFF50>":
#                playerlootadd(player, Sword)
#                print("hej")
          
#           elif list[i] == "<Spel.Loot object at 0x000001CB402DFFB0>":
#                playerlootadd(player, Spear)
#                print("hej")
#           elif list[i] == "<Spel.Loot object at 0x000001CB402E70D0>":
#                playerlootadd(player, Chestplate)
#                print("hej")
#           elif list[i] == "<Spel.Loot object at 0x000001CB402EF290>":
#                playerlootadd(player, Tank)
#                print("hej")
#           else:
#                print("hallå där martin nu har du jobb att göra")

#      return player
     