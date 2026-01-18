import random as rand
import time as klockan_tickar
import json as json
from Funky import *
from mantis_namn import *
from lootlist import *
from sparfil import *


class Loot(): #detta är en klass som besriver vilka atribut looten ska ha
    def __init__(self,itemname ,itemtype ,powerboost,hpboost ):
        self.itemname = itemname
        self.itemtype = itemtype
        self.powerboost = powerboost
        self.hpboost = hpboost

    def to_dict(self): #här to dict;ar vi, så vi göt om informationen i klassen till datatypen dictionary
        return {
          "itemname": self.itemname,
          "itemtype": self.itemtype,
          "powerboost": self.powerboost,
          "HPboost": self.hpboost
        }

    @classmethod #här from dictar vi looten, asså vi går från datatypen dictionary till class
    def from_dict(cls, d):
        return cls(
            d["itemname"],
            d["itemtype"],
            d.get("powerboost", 0),
            d.get("hpboost", d.get("HPboost", 0))
        )

#under så deklarerar vi olika variabler i klassen loot, och sätter deras attribut
Sword = Loot("svärd" ,"Weapond" ,1.2 ,0 )
Spear = Loot("spjut" ,"Weapond",1.4 ,0)
Chestplate = Loot("bröstplatta" ,"Armour",0 ,1.5)
Tank = Loot("Pansarvagn","Weapond" ,12 ,12)
lootlist = []#deklarerar lootlisten

# här under skapar vi en loot lista som skattkistorna drar ifrån, vi lägger till det som ska vara vanligare fler gånger och sen lägger vi till tanken endast en gång för den är op
for i in range (33):
    lootlist.append(Spear)

for i in range (33):
    lootlist.append(Sword)
for i in range (33):
    lootlist.append(Chestplate)
lootlist.append(Tank)

class Player(): # här är klassen player och i den förvarar vi allt som rör spelare
    def __init__(self, name, power, max_hp, max_inventory, role):
        self.name = name
        self.power = power
        self.max_hp = max_hp 
        self.max_inventory = max_inventory
        self.role = role
        self.alive = True
        self.inventory = []
        self.hp = max_hp 
        self.level = 0
        self.xp = 0
    
    def to_dict(self): #här to dictar vi klassen player, 
        sackItems = [] # här to dictar vi alla olika variabler av loot klassen som finns i inventoryt
        for i in range(len(self.inventory)):
            sackItems.append(self.inventory[i].to_dict())

        return {
          "name": self.name ,
          "power": self.power ,
          "max_hp": self.max_hp ,
          "max_inventory": self.max_inventory,
          "role": self.role,
          "alive": self.alive,
          "inventory": sackItems,
          "hp": self.hp,
          "level": self.level,
          "xp": self.xp
     }

    @classmethod
    def from_dict(cls, d): #här from dictar vi spelaren, asså vi går från datatypen dictionary till class
        p = cls(
            d["name"],
            d["power"],
            d["max_hp"],
            d["max_inventory"],
            d["role"],
        )
        p.alive = d.get("alive", True)
        p.hp = d.get("hp", p.max_hp)
        p.level = d.get("level", 0)
        p.xp = d.get("xp", 0)

        p.inventory = [Loot.from_dict(item) for item in d.get("inventory", [])]

        if p.hp > p.max_hp:
            p.hp = p.max_hp

        return p
    
def gain_xp(player, xp):    # ger xp och levlar upp spelaren efter ett visst antal xp, efter fighten.
    player.xp += xp                   
    print(f"Du får {xp} xp efter fighten! Du har nu {player.xp} xp!")
    if player.xp >= 10 * player.level:                                       # varje level blir svårare att komma till, 10 xp mer per level.
        player.level += 1
        player.xp = 0                                                                   # xp nollställs efter level up
        print(f"Grattis, Du har nått nästa level. Du är nu level {player.level}!")
        if player.level == 5:                                                        # när du när level 5 så vimnner man spelet.
           print("Grattis, du klarade spelet!!")
           exit(0)                                           # exit av spelet när man vinner spelet.
    return player

def take_damage(Target, damage):           # tar skada från antingen spelaren eller mantisen under fighten.   
    Target.hp -= damage
    if Target.hp <= 0:
        Target.hp = 0                       # Target kan inte ha mindre än 0 i hp.
        Target.alive = False               # Target dör när hp är 0.
    return Target

def fight(player):                                                                               # en fight mellan spelaren och en mantis.
    mantis = Mantisar(rand.choice(mantis_namn), rand.randint(1,5), rand.randint(1,3),"")       # här skapas en mantis med ett random namn från mantis_namn, den får också ett random hp och skada.
    total_damage = mantis.hp                      # total skada används senare, så att man inte kan få mer xp än mantisens hp.
    while player.alive and mantis.alive:      
        mantis = take_damage(mantis, player.power)
        print(f"Du slog {mantis.name} och gjorde {player.power} skada. {mantis.name} har nu {mantis.hp:.1f} hp kvar.")
        klockan_tickar.sleep(2)    # kul med lite paus!            
        if mantis.alive:
            player = take_damage(player, mantis.power)
            print(f"{mantis.name} slog dig och gjorde {mantis.power} skada. Du har nu {player.hp} hp kvar.")
            klockan_tickar.sleep(2)
        elif not mantis.alive: 
            print(f"Du har besegrat {mantis.name}!")
            gain_xp(player, total_damage)    
        else:
            pass
                          #om spelaren dör skrivs detta ut, inte i loopen eftersom den avbryts när spelaren dör.    
    if not player.alive:
        print(f"Du dog av {mantis.name}")
    else:
        pass
    return player


def heal(player):       # vila för att få 1 hp
    player.hp += 1
    if player.hp >= player.max_hp:         # kan inte få mer hp än max_hp
        player.hp = player.max_hp   # kan inte få mer hp än max_hp
        print("Du har redan fullt hp!")
    return player


def playerlootadd(player,loot): 
    player.inventory.append(loot) #lägger till loot i spelarens inventory
    player.power += loot.powerboost #lägger till powerbosten från looten till spelaren
    player.max_hp += loot.hpboost #lägger till hpboosten från looten till spelaren
    if len(player.inventory)-1 >= player.max_inventory: #kollar om spelarns inventory är fuult om det är det så skickar den en till playerlootremove
        playerlootremove(player)
    else:
        pass
    
    return player


 

def playerlootremove(player): 
    print(f"På de {len(player.inventory)-1} raderna under finns de föremål du har i ditt inventory")# här printar vi ut hur många rader med text som handlar om looten i inventoryt, anledningen till att vi kör -1 är för att vi har även lagt till skattskite itemet och de vill vi inte visa, eftersom de inte ska ligga där igentligen
    for i in range (len(player.inventory)-1): #samma procedur med -1 som innan fast här så printar den faktiskt ut allt i inventoryt
        item = player.inventory[i]
        if item.itemtype == "Weapond": #detta görs enbart för att det ska stå skade boost och som vi ser i elif så blir det hp boost istället
            print(f"{item.itemname}et som har en skade boost på {item.powerboost},")#här gör vi det lite fancy och skriver ut lootens namn och boost detta görs genom att vi satte item till player.inventory i och då vet den att den ska ta och skriva ut fakta från just de itemet
        elif item.itemtype == "Armour":
            print (f"{item.itemname}n som har en hp boost på {item.hpboost},")
    x = input("Ditt inventory är tyvärr fullt, välj ett av alternativen nedan för att utföra en handling\n(1) kasta bort föremålet som hittades i kistan\n(2) Byta ut föremålet mot något annat i inventoryt och kasta bort den saken")#här frågar vi spelaren om den vill kasta ut saken den hittade i kistan eller något i inventoryt och det sparas i x variebeln
    while True: #vi kör loopen för att hantera fel som användaren skriver in, så nu kan användaren skriva exempelvis 
        if x == "1":
            player.inventory.pop(player.max_inventory) #här popar vi sista objektet i listan, som är det spelaren nyss hittade i kistan, detta vet vi eftersom listan börjar på noll och max_inventory räknar från ett, så säg att 3 saker är max då kommer de objekten ha platsen 0,1,2 och ingen tre, vilket betyder att om vi lägger till en fjärde så får de plats 4 och vi kan poppa fyran för den är ändå utanför den tillåtna längden på listan
            break #vi breakar för att avsluta loopen,
        elif x == "2":
            print("\n"*20)#här byter vi rad 20 gånger för jag tyckte att det var snyggt att få lite mindre information på skärmen
            for i in range (len(player.inventory)-1):#här printar vi inventoryt, nästan exakt samma som förut fast nu har vi lagt till siffror innan så man senare ska kunna välja vilken man vill ta bort
                item = player.inventory[i]
                if item.itemtype == "Weapond":
                    print(f"({i}) {item.itemname}et som har en skade boost på {item.powerboost}")
                elif item.itemtype == "Armour":
                    print (f"({i}) din {item.itemname}an som har en hp boost på {item.hpboost}")
            while True:#en till while true för att ta hand om felhantering så ingen skriver skit
                val = input("vilken av sakerna i ditt inventory vill du kasta ut?\n")#här tar vi in vad användaren vill kasta ut och sparar det i variabeln val
                if val.isdigit() == False: #kollar så det är en siffra för vi vill inte ha bokstäver eftersom vi senare gör om det till en integer
                    #isdigit hittas på formelbladet, så ingen ai här johannes🤗
                    print("Snälladu skriv en av siffrorna bredvid dina items!!")
                elif int(val) < 0:#här görs val om till integer och sen kollar vi om den är mindre en noll och om den är det får användaren skriva in rätt siffra
                    print("Snälladu skriv en av siffrorna bredvid dina items!!")
                elif int(val) > len(player.inventory):#här kollar vi så inten inte är längre än listanslängd för annars betyder det att den vill kasta ut något som inte finns och då måste den ange ett nytt nummer 
                    print("Snälladu skriv en av siffrorna bredvid dina items!!") 
                else:
                    print(f"Du kastade ut ett/en {player.inventory[int(val)].itemname}")#om man har lyckats skriva in en siffra som man får skriva så printar programet namnet på itemet och att det kommer kastas ut
                    player.power -= (player.inventory[int(val)]).powerboost# här tar vi bort power boosten looten har gett oss så inte boosten finns kvar när spelaren inte innehaver saken
                    player.max_hp -= (player.inventory[int(val)]).hpboost#samma som den innan fast med hg
                    player.inventory.pop(int(val))#här tar vi bort saken från inventoryt genom att poppa den från listan
                    break # här breakar vi loppen som raderar looten
            break#här breakas den stora loopen där man får välja om man vill kasta ut från inventoryt eller de man just tog upp
        else:
            print("Skriv ett av nummrena 1-2")#här påminner den att man ska skriva ett eller två, asså om man vill kasta ut från inventoryt eller de man just tog upp

    return player #och sedan så retunerar vi player som vanligt
 
def playerlootcheck(player): #denna används när spelaren vill kolla vad som finns i inventoryt
    if len(player.inventory) <= 0: #vi börjar med att kolla om spelaren har något i inventoryt eller om det räcker med att printa att inventoryt är tomt
        print("Det verkar som du inte har något i din pung")
    else: # här skriver den ut inventoryt om det finns saker i det
        print(f"Du har {len(player.inventory)} st saker utav {player.max_inventory} i ditt inventory och de sakerna är:")
   
        for i in range (len(player.inventory)):  #här loopar den igenom allt i inventoryt och skriver yt det, texten varierar lite beroende om det är av loottypen vapen eller rustning och det kollas med en if sats   
            lootitem = player.inventory[i]
            if lootitem. itemtype == "Weapond":
                print(f"{i}  ditt {lootitem.itemname} som har en skade boost på {lootitem.powerboost}")
            elif lootitem.itemtype == "Armour":
                print(f"{i}  din {lootitem.itemname} som har en hp boost på {lootitem.hpboost}")

    return player
                
def lootchest (player): #här finns funktionen som öppnar en kista
    x = rand.choice(lootlist) #plockar random från lootlistan, som innehåller olika loot med olika chans att få
    print(f"Wow, du hittade en skattkista och i skattkistan låg en/ett {x.itemname}!!\n")#printar vad mann hittat i skattkistan
    playerlootadd(player,x)#kallar på lootadd funktionen och tar in x och player x är slumpmässiga looten och player är det som användern skriver in när den kallar på funktionen
    return player

def randportal(player):       # slumpmässigt val mellan skattkista eller fightas en mantis.
    x = rand.randint(0,11)
    if x <= 8:
        fight(player)        # större chans att man får fightas mot mantis.
    else:
        lootchest(player)

    return player

def new_game():
    print("Välkommen till äventyrsspelet👍😢😃😎. Du kommer att navigera i en grotta, slåss" \
        " mot mantisar och samla skatter. \nMen se upp för satanisterna!")
    
    player_name = input("Nu får du skapa en karaktär. vad heter du?\n")      # här skriver spelaren in sitt namn. detta sparas i Player1_name och inte player.name för vi har inte skapat ännu playern men under så används variabeln för att skapa playern
    
    print("Nu får du välja vilken klass du ska vara resten av spelet, du kan välja mellan pungråtta 1, Lennart Bladh 2 och fritidschefen 3!\n(skriv siffran efter för att välja roll.)\n")
    
    while True: # felhantering
        role_choice = input()                 # här väljer spelaren sin roll.

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
    return Player1

def load_game(player):
    x = load_save_file(player)
    return x

def game_start():
    print("Hej och välkommen till äventyrsspelet!!!  \n\nOm du är ny till detta spel så klicka (1) \n\nOm du har en sparfil klicka (2)")
    while True:
        Player1 = Player("player_name", 1, 5, 2, "Fritidschefen")
        game_choice = input()
        if game_choice == "1":
            x = new_game()
            break
        elif game_choice == "2":
            x = load_game(Player1)
            print(f"Välkommen tillbaka {x.name}")
            break
        else:
            print("snälla skriv en av siffrorna som står ovan🥺🥺🥺")
    return x

def main(): 
    Player1 = game_start()
    while Player1.alive:
            print("\nVad vill du göra?")

            val = input(""" 
                        1. Gå genom portal  2. Kolla stats
                        3. Öppna Pungsäcken 4. vila
                        5. Spara spelet     q. Avsluta spelet
                    """)
        
            if val == "1":
                Player1 = randportal(Player1)

            elif val == "2":
                print(f"""
                    


                        Halloj {Player1.name}.\n   Just nu har du {Player1.hp} liv och din styrka är {Player1.power}.\n   Du har {Player1.xp} xp och är i level {Player1.level}.
                        
                """)
                
            elif val == "3":
                Player1 = playerlootcheck(Player1)

            elif val == "4":
                Player1 = heal(Player1)
                print(f"Du chillade galet och fick 1 hp {Player1.hp}") 

            elif val == "5":
                save_game(Player1)

            elif val == "q":
                exit(0)
            else:
                print("Du måste välja något av valen i menyn")
            

if __name__ == "__main__":
    main()
print("Better luck next time BUDDY!")
