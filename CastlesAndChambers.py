#UNS studios
#name: Ronan Underwood
#date: ///
#description: text-based adventure game

import time
import random
from sys import exit

def clear():

    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")

def displayIntroText():

    print("  _____         __  __       ")                                     
    print(" / ___/__ ____ / /_/ /__ ___ ")
    print("/ /__/ _ `(_-</ __/ / -_|_-< ")                                
    print("\___/\_,_/___/\__/_/\__/___/              __              ")
    print("  / _ | ___  ___/ / / ___/ /  ___ ___ _  / /  ___ _______ ")
    print(" / __ |/ _ \/ _  / / /__/ _ \/ _ `/  ' \/ _ \/ -_) __(_-< ")
    print("/_/ |_/_//_/\_,_/  \___/_//_/\_,_/_/_/_/_.__/\__/_/ /___/ ")

    time.sleep(4.5)
    clear()

def die():
    clear()
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('GAME OVER')
    time.sleep(5)
    quit()
    
def end():
    clear()
    print('YOU WIN!')
    time.sleep(1)
    print('')
    time.sleep(1)
    print('')
    time.sleep(1)
    print('')
    time.sleep(1)
    print('')
    time.sleep(1)
    print('')
    time.sleep(1)
    print('')
    time.sleep(1)
    print('CASTLES AND CHAMBERS - SUPPORT AND ASSISTANCE')
    time.sleep(1)
    print('')
    time.sleep(1)
    print('PROGRAMMING ASSISTANCE')
    time.sleep(1)
    print('GENTRY UNDERWOOD')
    time.sleep(1)
    print('LEXI ROSS')
    time.sleep(1)
    print('GEVER TULLEY')
    time.sleep(1)
    print('')
    time.sleep(1)
    print('MANAGEMENT')
    time.sleep(1)
    print('JUSTINE MACAULEY')
    time.sleep(1)
    print('MELISSA NOCERO')
    time.sleep(1)
    print('')
    time.sleep(1)
    print('AND SPECIAL THANKS')
    time.sleep(1)
    print('TO COUNTLESS TESTERS')
    time.sleep(1)
    print('')
    time.sleep(1)
    print('')
    time.sleep(1)
    print('')
    time.sleep(1)
    print('CREATED BY RONAN UNDERWOOOD')
    time.sleep(1)
    print('')
    time.sleep(1)
    print('')
    time.sleep(1)
    print('')
    time.sleep(1)
    print('')
    time.sleep(1)
    print('')
    time.sleep(1)                       
    print(' _____ _____ _____ ')
    time.sleep(1)
    print('|  |  |   | |   __|')
    time.sleep(1)
    print('|  |  | | | |__   |')
    time.sleep(1)
    print('|_____|_|___|_____|')
    time.sleep(1)
    print('                   ')
    time.sleep(1)
    print('')
    time.sleep(1)
    print('')
    time.sleep(1)
    print('')
    time.sleep(1)
    print('')
    time.sleep(1)
    print('')
    time.sleep(1)
    print('')
    time.sleep(1)
    print('')
    time.sleep(1)
    quit()

def help():
    print('')
    print(' HELP MENU - CASTLES AND CHAMBERS')
    print(' Castles and Chambers is an text-based adventure game. That means that there are no graphics.')
    print(' Instead, you control the game with simple text-based commands. Some examples include:')
    print('')
    print(' go west')
    print(' take machete')
    print(' cut vines')
    print('')
    print(' The commands are relitively simple. The first word is always a verb (take, cut) and the second always the noun (machete, vines).')
    print('')
    print(''' Please note: 'go to' commands such as 'go to castle' are not valid and should be replaced by directional commands (such as 'go east')''')
    print(" Also note: the commands 'go north', 'go east', 'go south' and 'go west' can be abbriviated to 'n', 'e', 's' and 'w', respectively.")

def msg(area):
        return area['name']

def get_choice(area,dir):
    #north
    if (dir=='go north' or dir=='north' or dir=='n') :
        return 0
    #east
    elif (dir=='go east' or dir=='east' or dir=='e') :
         return 1
    #south
    elif (dir=='go south' or dir=='south' or dir=='s'):
        return 2
    #west
    elif (dir=='go west' or dir=='west' or dir=='w'):
        return 3
    #quit
    elif dir=='quit':
        return -3
    #help
    elif (dir=='help' 
    or dir=='get help'):
        return -4
    #machete (get)
    elif (dir=='get machete' 
    or dir=='take machete' 
    or dir=='pick up machete' 
    or dir=='grab machete'
    or dir=='find machete'):
        return -5
    #machete (cut with)
    elif (dir=='use machete' 
    or dir=='cut vines' 
    or dir=='cut vines with machete' 
    or dir=='use machete on vines'
    or dir=='use machete to cut vines'):
        return -6
    #ticket (pick up)
    elif (dir=='pick up ticket' 
    or dir=='get ticket' 
    or dir=='take ticket' 
    or dir=='pick up small ticket' 
    or dir=='get small ticket' 
    or dir=='take small ticket' 
    or dir=='grab ticket'
    or dir=='grab small ticket'
    or dir=='find ticket'
    or dir=='find small ticket'):
        return -7
    #raft (pick up)
    elif (dir=='pick up raft' 
    or dir=='take raft' 
    or dir=='get raft' 
    or dir=='pick up the raft' 
    or dir=='grab raft'
    or dir=='find raft'):
        return -8
    #blank
    elif (dir=='ARPANET'):
        return -9
    #castle(enter)
    elif (dir=='enter castle'
    or dir=='go into castle'
    or dir=='enter old castle'
    or dir=='go into old castle'):
        return -10
    #enter(just)
    elif (dir=='enter'):
        return -11
    #oar(pick up)
    elif (dir=='get oar' 
    or dir=='take oar' 
    or dir=='pick up oar'
    or dir=='grab oar'):
        return -12
    #oar (use)
    elif (dir=='use oar'):
        return -13
    #oar and machete (get)
    elif (dir=='get oar and machete' 
    or dir=='get machete and oar' 
    or dir=='take oar and machete' 
    or dir=='take machete and oar' 
    or dir=='pick up oar and machete' 
    or dir=='pick up machete and oar' 
    or dir=='grab oar and machete' 
    or dir=='grab machete and oar'):
        return -14
    #error 2
    elif (dir=='use raft'
    or dir=='use raft to get to island'
    or dir=='go to castle'
    or dir=='go to island'
    or dir=='go to forest'
    or dir=='go into forest'
    or dir=='enter forest'
    or dir=='go on path'
    or dir=='keep walking'):
        return -15
    # Secrets must be upheald (EE)
    elif (dir=='where is machete'):
        return -16
    # Take key
    elif (dir=='pick up key' 
    or dir=='take key' 
    or dir=='get key' 
    or dir=='grab key'
    or dir=='find key'):
        return -17
    #look around
    elif (dir=='look around' or dir=='look'):
        return -18
    elif (dir=='exit' or dir=='leave'):
        return -19
    elif (dir=='exit castle'
    or dir=='leave castle'
    or dir=='exit old castle'
    or dir=='leave old castle'):
        return -20
    #use raft (3)
    elif (dir=='use raft'
    or dir=='go on raft'
    or dir=='go to raft'
    or dir=='use oar'):
        return -21
    #xyzzy
    elif (dir=='xyzzy'):
        return -22
    #cave (enter)
    elif (dir=='enter cave'):
        return -23
    #coin (take)
    elif (dir=='get coin' 
    or dir=='take coin' 
    or dir=='pick up coin'
    or dir=='grab coin'):
        return -24 
    #no (yes!)
    elif (dir=='no'):
        return -25
    # get ruby
    elif (dir=='get ruby' 
    or dir=='take ruby' 
    or dir=='pick up ruby'
    or dir=='grab ruby'):
        return -26
    # ticket on shelf
    elif (dir=='put ticket on shelf'
    or dir=='use ticket'
    or dir=='put small ticket on shelf'
    or dir=='use small ticket'):
        return -27
    # ruby on shelf
    elif (dir=='put ruby on shelf'
    or dir=='use ruby'):
        return -28
    # ruby on shelf
    elif (dir=='put coin on shelf'
    or dir=='use coin'):
        return -29
    # cheat codes
    elif (dir == 'PIXELS'):
        return -30
    elif (dir== 'MAC 128K'):
        return -31
    elif (dir == 'GRUE'):
        return -32
    elif (dir== 'COMMADORE 64'):
        return -33
    elif (dir== 'ZORKMID'):
        return -34
    elif (dir=='get egg'
    or dir=='take egg'
    or dir=='pick up egg'
    or dir=='grab egg'
    or dir=='get dragon egg'
    or dir=='take dragon egg' 
    or dir=='pick up dragon egg'
    or dir=='grab dragon egg'):
        return -36
    elif (dir=='put egg on shelf'
    or dir=='use egg'
    or dir=='put dragon egg on shelf'
    or dir=='use dragon egg'):
        return -35
    #potion (get)
    elif (dir=='get potion'
    or dir=='take potion'
    or dir=='pick up potion'
    or dir=='grab potion'):
        return -37
    #potion (put on shelf)
    elif (dir=='put potion on shelf'
    or dir=='use potion'):
        return -38
    #ring (get)
    elif (dir=='get ring'
    or dir=='take ring'
    or dir=='pick up ring'
    or dir=='grab ring'):
        return -39
    #ring (put on shelf)
    elif (dir=='put ring on shelf'
    or dir=='use ring'):
        return -40
    elif (dir=='open door'):
        return -41
    elif (dir=='enter door' 
    or dir=='enter doorway'):
        return -42
    elif (dir==''):
        return -43
    #the problem code (1)
    else:
        return -1    

def main():
    dirs = (0,0,0,0)

    #variables
    vinesHacked = False
    hasMachete = False

    hasTicket = False
    hasRaft = False 
    hasCoin = False
    hasRuby = False
    hasOar = False
    hasEgg = False
    hasRing = False
    hasPotion = False

    ticketShelf = False
    rubyShelf = False
    coinShelf = False
    eggShelf = False
    ringShelf = False
    potionShelf = False

    castleDoor = False
    otherCastleDoor = False

    westOfCastle = {'name':'-WEST OF CASTLE- You are in a clearing. To the west is a dirt path leading into the forest. To the east is an old castle entrance overgrown with vines. On the ground is a small ticket.','directions':dirs}
    path = {'name':'-PATH- You are on a small dirt path winding west into the dark forest.','directions':dirs}
    beach = {'name':'-BEACH- You are standing on a small beach. There is a large island to your west. There is a machete and an oar here.', 'directions':dirs}
    castleEntrance = {'name':'-CASTLE ENTRANCE- The castle entrance is covered with vines. You would need a machete to enter.','directions':dirs}
    desertPatchOne = {'name':'-DESERT- There is a massive desert to your north. The dessert is impassable.','directions':dirs}
    desertPatchTwo = {'name':'-DESERT- There is a massive desert to your north. The dessert is impassable.','directions':dirs}
    desertPatchFour = {'name':'-DESERT- There is a massive desert to your north. The dessert is impassable.','directions':dirs}
    cliffs = {'name':'-CLIFFS- You are standing at the edge of a cliff. There are some mountains to the east. The cliff is at least 50 feet high and streches as far as you can see. The lake beneath it would not make for a pleasant fall. You can not go further south.','directions':dirs}
    centerOfCastle = {'name':'-CENTER OF CASTLE- You are standing at the center of an old castle. The walls are crumbling around you and are covered in vines. There is a raft on the ground and a tower to your north. There is a door to your south.','directions':dirs}
    ocean = {'name':'You hop on your raft and paddle out into the ocean. To the west is a small island and to the east the beach.','directions':dirs}
    islandLanding = {'name':'-ISLAND- You are standing on a small tropical island with paths leading in every direction. There is a shelf here with six compartments. The shelf is empty.', 'directions':dirs}
    castleTower = {'name':'-CASTLE TOWER- You are in a tall tower overlooking the castle. From here you can see everything. The massive desert to your north, the cliffs to your south, the mountains to your east and the ocean to your west.','directions':dirs}
    southPath = {'name':'-SOUTH PATH- You are on a small dirt path winding south. At the end of the path is an massive pulsating blob. You are unable to make out its shape or form.','directions':dirs}
    westPath = {'name':'-WEST PATH- You are walking on a thin path. There is a cave in front of you.','directions':dirs}
    northPath = {'name':'-NORTH PATH- You are at the other side of the island. There is a beach here. Half buried in the sand is a small vile of potion.','directions':dirs}
    deathByEvilBlob = {'name':"You feel terrible pain, pain like you have never felt before. DEATH BY EVIL BLOB",'directions':dirs}
    cave = {'name':'-CAVE- You are in a cave. The cave goes on west for seemingly forever. ','directions':dirs}
    caveWestTwo = {'name':"-CAVE- You are in a cave. You can't see much but you notice the south side opens up.",'directions':dirs}
    deathBySpikeTrap = {'name':"Your stomach lurches as you fall into a deep hole. DEATH BY SPIKE TRAP",'directions':dirs}
    caveWestThree = {'name':"-CAVE- You can't see much more.",'directions':dirs}
    caveWestFour = {'name':"-CAVE- You can't see anything",'directions':dirs}
    caveSouthTwo = {'name':"-CAVE- You are in a cave.",'directions':dirs}
    caveSouthThree = {'name':"-ROOM- You are in a small room. There is light, although you can not tell its source. The room is made of marble and appears very majestic. There is a coin on the ground. The southern wall is glowing blue. The word 'xyzzy' is etched into the wall. You do not recognize that word.",'directions':dirs}
    deathByLargePit = {'name':"You walk along. Suddenly, a hole in the ground opens up. DEATH BY LARGE PIT",'directions':dirs}
    swampOne = {'name':"-SWAMP- You are in a swamp. The swamp reeks strongly of rotten eggs.",'directions':dirs}
    quicksand = {'name':"You step in somthing yellow. You struggle, but you are slowly forced down. DEATH BY QUICKSAND",'directions':dirs}
    swampTwo = {'name':"-SWAMP- You continue walking down the swamp. There is what looks like a beehive in front of you. There are some old ruins to your east.",'directions':dirs}
    thoseArentBees = {'name':"Those aren't bees. DEATH BY BEE-LIKE CREATURES.",'directions':dirs}
    nearRuby = {'name':"-ENTRANCE TO RUINS- You are in an entrance to what appears to be an old crumbling building.",'directions':dirs}
    ruby = {'name':"-RUINS- You are standing in the middle of beautiful ruins of greek style. There is a shimmering ruby floating in midair here.",'directions':dirs}
    cliffsToMountains = {'name':"-CLIFFS- The cliffs end and massive mountains appear to your east.",'directions':dirs}
    mountains = {'name':"-MOUNTAINS- The mountains are too large to scale. However, there is a path that leads north.",'directions':dirs}
    fallOffCliffs = {'name':"You are freefalling for roughly 1.8 seconds. Then you hit the water. DEATH BY FALLING OFF CLIFFS.",'directions':dirs}
    pathLeadingNorth = {'name':"-MOUNTAIN PATH- You reach a fork. You can go either east or west.",'directions':dirs}
    deathByEvilBeans = {'name':"An inner voice yells at you.", 'directions':dirs}
    dragonEgg = {'name':"-ROCKY CLEARING- You are standing in a rocky clearing. There is a nest here. There is a dragon egg in the nest.", 'directions':dirs}
    insideCastle = {'name':"-CASTLE CHAMBERS-  Inside is a staircase leading down to a long hallway. You walk down for seemingly forever. Finally, you reach the bottom and discover a long hallway lit by torches. At the end of the hallway is another door.", 'directions':dirs}
    insideCastleTwo = {'name':"-CASTLE CHAMBERS-  You are in another hallway lit by torches. To your south is a wall glowing blue.", 'directions':dirs}
    weirdRoom = {'name':"-ROOM- You are in a small room. There is a glass display case in the middle of the room. There is a ring in the case.", 'directions':dirs}

    desertPatchTwo['directions'] = (0,0,westOfCastle,0)
    westOfCastle['directions'] = (desertPatchTwo,castleEntrance,cliffs,path)
    path['directions'] = (0,westOfCastle,swampOne,beach)
    beach['directions'] = (desertPatchOne,path,0,0)
    castleEntrance['directions'] = (desertPatchFour,0,cliffs,westOfCastle)
    desertPatchOne['directions'] = (0,0,beach,0)
    desertPatchFour['directions'] = (0,0,castleEntrance,0)
    cliffs['directions'] = (westOfCastle,cliffsToMountains,fallOffCliffs,0)
    centerOfCastle['directions'] = (castleTower,0,0,castleEntrance)
    ocean['directions'] = (0,beach,0,islandLanding)
    islandLanding['directions'] = (northPath,ocean,southPath,westPath)
    northPath['directions'] = (0,0,islandLanding,0)
    westPath['directions'] = (0,islandLanding,0,cave)
    southPath['directions'] = (islandLanding,0,deathByEvilBlob,0)
    deathByEvilBlob['directions'] = (0,0,0,0)
    islandLanding['directions'] = (northPath,ocean,southPath,westPath)
    cave['directions'] = (0,westPath,0,caveWestTwo)
    caveWestTwo['directions'] = (0,cave,deathBySpikeTrap,caveWestThree)
    caveWestThree['directions'] = (0,caveWestTwo,0,caveWestFour)
    caveWestFour['directions'] = (0,caveWestThree,caveSouthTwo,deathByLargePit)
    caveSouthTwo['directions'] = (caveWestFour,0,caveSouthThree,0)
    caveSouthThree['directions'] = (caveSouthTwo,0,islandLanding,0)
    castleTower['directions'] = (0,0,centerOfCastle,0)
    swampOne['directions'] = (path,thoseArentBees,swampTwo,quicksand)
    quicksand['directions'] = (0,0,0,0)
    cliffsToMountains['directions'] = (0,mountains,fallOffCliffs,cliffs)
    mountains['directions'] = (pathLeadingNorth,0,0,cliffsToMountains)
    swampTwo['directions'] = (swampOne,nearRuby,thoseArentBees,0)
    thoseArentBees['directions'] = (0,0,0,0)
    nearRuby['directions'] = (0,ruby,0,swampTwo)
    ruby['directions'] = (0,0,0,nearRuby)
    fallOffCliffs['directions'] = (0,0,0,0)    
    pathLeadingNorth['directions'] = (0,dragonEgg,mountains,deathByEvilBeans)
    deathByEvilBeans['directions'] = (0,0,0,0)
    dragonEgg['directions'] = (0,0,0,pathLeadingNorth)
    insideCastle['directions'] = (centerOfCastle,0,0,0)
    insideCastleTwo['directions'] = (insideCastle,0,weirdRoom,0)
    weirdRoom['directions'] = (0,0,0,0)
    
    area = westOfCastle

    print("For help type 'get help'")
    stuck = True
    while True:
        
        print(area['name'])
        stuck = True
        while stuck :
            if (ticketShelf == True
            and coinShelf == True
            and rubyShelf == True
            and eggShelf == True
            and ringShelf == True
            and potionShelf == True):
                end()
            if (area == deathByEvilBlob 
            or area == deathByLargePit 
            or area == deathBySpikeTrap 
            or area == quicksand
            or area == thoseArentBees
            or area == fallOffCliffs):
                quit()
            if area == deathByEvilBeans:
                area = pathLeadingNorth
                print(area['name'])
            dir = input("> ").strip().replace(' the ', ' ').replace('i ', '')
            choice = get_choice(area,dir)
            if choice == -1:
                #don't know word
                print("I don't know the phrase '" + dir + "'")
                continue
            elif choice == -3:
                #quit
                quit()
            elif choice == -4:
                #help
                help()
            elif choice == -5:
                if area == beach:
                    #pick up machete
                    if hasMachete == False:
                        print('You pick up the machete. The blade looks old but plenty sharp.')
                        hasMachete = True
                        if hasOar == True:
                            beach['name'] = '-BEACH- You are standing on a small beach. There is a large island to your west.'
                        else:
                            beach['name'] = '-BEACH- You are standing on a small beach. There is a large island to your west. There is an oar here.'
                    else:
                        print('You already have the machete.')
                else:
                    print('''I don't see a machete here.''')
            elif choice == -6:
                if area == castleEntrance:
                    #cut vines
                    if hasMachete == True:
                        print('You cut the vines. You can now enter.')
                        vinesHacked = True
                        castleEntrance['name'] = '-CASTLE ENTRANCE- You are standing at the entrance to an old castle. You have hacked the vines.'
                        castleEntrance['directions'] = (desertPatchFour,centerOfCastle,0,westOfCastle)
                    else:
                        print('''You don't have a machete.''')
                else:
                    print('''I don't see anything to cut here.''')
            elif choice == -7:
                if area == westOfCastle:
                    #pick up ticket
                    if hasTicket == True:
                        print('You already have the ticket.')
                    else:
                        print('You pick up the ticket. It reads: ADMIT ONE to CASTLES and CHAMBERS. SINGLE USE ONLY!')
                        hasTicket = True
                        westOfCastle['name'] = '-WEST OF CASTLE- You are in a clearing. To the west is a dirt path leading into the forest. To the east is an old castle entrance overgrown with vines.'
                else:
                    print('''I don't see a ticket here.''')
            elif choice == -8:
                if area == centerOfCastle:
                    #pick up raft
                    if hasRaft == True:
                        print('You already have the raft.')
                    else:
                        print('With massive effort, you manage to lift up the raft and put it on your back.')
                        hasRaft = True
                        centerOfCastle['name'] = '-CENTER OF CASTLE- You are standing at the center of an old castle. The walls are crumbling around you and are covered in vines. There is a tower to your north and a door to your south.'
                        if hasOar == True:
                            beach['directions'] = (desertPatchOne,path,0,ocean)
                else:
                    print('''I don't see a raft here''') 
            elif choice == -10:
                if area == castleEntrance:
                    #enter castle
                    if vinesHacked == True:
                        area = centerOfCastle
                        print(centerOfCastle['name'])
                    else:
                        print('''The vines aren't cut!''')
                else:
                    print('''There's no castle here.''')
            elif choice == -11:
                print("Enter where? Did you mean 'enter castle' or 'enter doorway' ?")
            elif choice == -12:
                if area == beach:
                    #pick up oar
                    if hasOar == False:
                        print('''You pick up the oar. It's heavy. Solid oak.''')
                        hasOar = True
                        if hasRaft == True and hasOar == True:
                            beach['directions'] = (desertPatchOne,path,0,ocean)
                        elif hasMachete == True:
                            beach['name'] = '-BEACH- You are standing on a small beach. There is a large island to your west.'
                        else:
                            beach['name'] = '-BEACH- You are standing on a small beach. There is a large island to your west. There is a machete here.'
                    else:
                        print('You already have the oar.')
                else:
                    print('''I don't see an oar here.''')
            elif choice == -13:
                if area == ocean:
                    #use oar
                    print('in what direction do you want to go?')
                else:
                    print('''I don't know that word''')
            elif choice == -14:
                if area == beach:
                    #pick up machete and oar
                    if hasMachete == False and hasOar == False:
                        print("You pick up the machete and the oar.")
                        hasOar = True
                        hasMachete = True
                        beach['name'] = '-BEACH- You are standing on a small beach. There is a large island to your west.'
                    elif hasOar == True and hasMachete == False:
                        print('You take the machete. You already have the oar.')
                        hasMachete = True
                    elif hasOar == False and hasMachete == True:
                        print('You take the oar. You already have the machete.')
                        hasOar = True
                    else:
                        print("You already have both the oar and the machete.")
                else:
                    print("I don't see an machete or an oar here.")
            elif choice == -15:
                #directional reccomendation
                print('''I don't know that word. But a directional command (such as 'go east') might help.''')
            elif choice == -16:
                #easter egg
                if hasMachete == True:
                    print('In your hands.')
                else:
                    print('Secrets must be upheld')
            elif choice == -18:
                print(area['name'])
            elif choice == -19:
                print('Exit from where?')
            elif choice == -20:
                if area == centerOfCastle:
                    area = castleEntrance
                    print(area['name'])
                else:
                    print('''You aren't in a castle.''')
            elif choice == -21:
                if area == centerOfCastle:
                    #Error 3 (Raft)
                    if hasRaft == True:
                        print('You already have the raft')
                    else:
                        print("I don't understand that, but you might want to try 'get raft'.")
                else:
                    print('''I don't see a raft here.''')
            elif choice == -22:
                if area == caveSouthThree:
                    xyzzy = random.randint(1,5)
                    if xyzzy == 1:
                        area = westOfCastle
                        print(area['name'])
                    elif xyzzy == 2:
                        area = dragonEgg
                        print(area['name'])
                    elif xyzzy == 3:
                        area = weirdRoom
                        print(area['name'])
                    elif xyzzy == 4:
                        area = northPath
                        print(area['name'])
                    else:
                        area = ruby
                        print(area['name'])
                else:
                    print('DEATH BY IMPROPER USE OF XYZZY')
                    print('(just kidding)')
            elif choice == -23:
                if area == westPath:
                    area = cave
                    print(area['name'])
                else:
                    print("I don't see a cave here")
            elif choice == -24:
                if area == caveSouthThree:
                    #take coin
                    if hasCoin == False:
                        print('You pick up the coin. It feels smooth in your hand.')
                        hasCoin = True
                        caveSouthThree['name'] = "-ROOM- You are in a small room. There is light, although you can not tell its source. The room is made of marble and appears very majestic. The southern wall is glowing blue. The word 'xyzzy' is etched into the wall. You do not recognize that word."
                    else:
                        print('You already have the coin.')
                else:
                    print("I don't see a coin here.")
            elif choice == -25:
                print('Yes!')
            elif choice == -26:
                if area == ruby:
                    #take ruby
                    if hasRuby == False:
                        print('You pick up the ruby. The warmth of the jewel spreads up your arm and through your body.')
                        hasRuby = True
                        ruby['name'] = '-RUINS- You are standing in the middle of beautiful ruins of greek style.'
                    else:
                        print('You already have the ruby.')
                else:
                    print("I don't see a ruby here.")
            elif choice == -27:
                if area == islandLanding:
                    #ticket on shelf
                    if ticketShelf == True:
                        print('The ticket is already on the shelf.')
                    else:
                        print('You put the ticket on the shelf. The shelf makes a loud clicking noise and the ticket dissapears.')
                        ticketShelf = True
                else:
                    print("Use ticket how?")
            elif choice == -28:
                if area == islandLanding:
                    #ruby on shelf
                    if rubyShelf == True:
                        print('The ruby is already on the shelf.')
                    else:
                        print('You put the ruby on the shelf. The shelf makes a loud clicking noise and the ruby dissappears.')
                        rubyShelf = True
                else:
                    print("Use ruby how?")
            elif choice == -29:
                if area == islandLanding:
                    #coin on shelf
                    if hasCoin == True:
                        if coinShelf == True:
                            print('The coin is already on the shelf.')
                        else:
                            print('You put the coin on the shelf. The shelf makes a loud clicking noise and the coin dissappears.')
                            coinShelf = True
                    else:
                        print("You don't have a coin")
                else:
                    print("Use coin how?")
            elif choice == -30:
                area = islandLanding
                print(area['name'])
            elif choice == -31:
                area = westOfCastle
                print(area['name'])
            elif choice == -32:
                area = caveSouthThree
                print(area['name'])
            elif choice == -33:
                area = ruby
                print(area['name'])
            elif choice == -34:
                area = dragonEgg
                print(area['name'])
            elif choice == -9:
                area = weirdRoom
                print(area['name'])
            elif choice == -35:
                if area == islandLanding:
                    #egg on shelf
                    if hasEgg == True:
                        if eggShelf == True:
                            print('The egg is already on the shelf.')
                        else:
                            print('You put the dragon egg on the shelf. The shelf makes a loud clicking noise and the egg dissappears.')
                            eggShelf = True
                    else:
                        print("I don't have an egg.")
                else:
                    print("Use the egg how?")
            elif choice == -36:
                if area == dragonEgg:
                    #take egg
                    if hasEgg == False:
                        print('You pick up the egg. the egg is suprisingly heavy, and it takes effort to lift up.')
                        hasEgg = True
                        dragonEgg['name'] = "-ROCKY CLEARING- You are standing in a rocky clearing. There is a nest here."
                    else:
                        print('You already have the egg.')
                else:
                    print("I don't see an egg here.")
            elif choice == -37:
                if area == northPath:
                    #take potion
                    if hasPotion == False:
                        print('You pick up the potion. The red liquid sloshes around in the small crystal bottle.')
                        northPath['name'] = '-NORTH PATH- You are at the other side of the island. There is a beach here.'
                        hasPotion = True
                    else:
                        print('You already have the potion.')
                else:
                    print("I don't see any potion here.")
            elif choice == -38:
                if area == islandLanding:
                    #potion on shelf
                    if hasPotion == True:
                        if potionShelf == True:
                            print('The potion is already on the shelf.')
                        else:
                            print('You put the bottle of potion on the shelf. The shelf makes a loud clicking noise and the potion dissappears.')
                            potionShelf = True
                    else:
                        print("I don't have a potion.")
                else:
                    print("The bottle is sealed shut. There is no way to open it.")
            elif choice == -39:
                if area == weirdRoom:
                    #take ring
                    if hasRing == False:
                        weirdRoom['name'] = "You hear a deep voice yell 'Leave now!' (press enter)"
                        print('')
                        print('You pick up the ring and put it on your finger. The ring is a perfect fit.')
                        print('')
                        hasRing = True
                        print('Suddenly, you hear a loud rumbling noise.')
                        print('')
                        area = westOfCastle
                        print(area['name'])
                    else:
                        print('You already have the ring.')
                else:
                    print("I don't see a ring here.")
            elif choice == -40:
                if area == islandLanding:
                    #potion on shelf
                    if hasRing == True:
                        if ringShelf == True:
                            print('The ring is already on the shelf.')
                        else:
                            print('You put the ring on the shelf. The shelf makes a loud clicking noise and the ring dissappears.')
                            ringShelf = True
                    else:
                        print("I don't have a ring.")
                else:
                    print("Use the ring how?")
            elif choice == -41:
                if area == centerOfCastle:
                    if castleDoor == False:
                        print('Open.')
                        castleDoor = True
                        centerOfCastle['directions'] = (castleTower,0,insideCastle,castleEntrance)
                    else:
                        print('The door is already open.')
                elif area == insideCastle:
                    if otherCastleDoor == False:
                        print('Open.')
                        otherCastleDoor = True
                        insideCastle['directions'] = (centerOfCastle,0,insideCastleTwo,0)
                    else:
                        print('The door is already open.')
                else:
                    print("I don't see a door here.")
            elif choice == -42:
                if area == centerOfCastle:
                    if castleDoor == True:
                        area = insideCastle
                        print(area['name'])
                    else:
                        print('The door is closed.')
                if area == insideCastle:
                    if otherCastleDoor == True:
                        area = insideCastleTwo
                        print(area['name'])
                    else:
                        print('The door is closed.')
                else:
                    print("I don't see a door here.")
            elif choice == -43:
                if area == weirdRoom and weirdRoom['name'] == "You hear a deep voice yell 'Leave now!' (press enter)":
                    area = centerOfCastle
                    print(area['name'])
                else:
                    print("I don't know the phrase ''")
            else:
                #can't go that way
                if area['directions'][choice] == 0:
                    print('''I can't go any further that way.''')
                else:
                    area = area['directions'][choice]
                    print(area['name'])

#where it runs
displayIntroText()
main()
end()
