import time, random


print('loading ls4 (love scrpit 4):')
value = 0
time.sleep(2)
for i in range(5):
    value = int(random.randint(value+10, value+20))
    print('loading:',value,'%')
    time.sleep(random.randint(1,5)/10)
print('loading: 100%')
time.sleep(0.2)
print('finalized: ls4: a little rpg for you!')

time.sleep(0.5)


def loadsave(location):
    f = open(location,'r')
    for i in f.readlines():
        if 'hp' in i:
            global hp
            hp = int(i[i.find('=')+1:])
            print('hp =',hp)
        elif 'bossKilled' in i:
            global bossKilled
            bossKilled = int(i[i.find('=')+1])
            print('bosses killed =',bossKilled)
        elif 'gold' in i:
            global gold
            gold = i.split('=')
            gold = int(gold[1])
            print('gold =',gold)
        elif 'level' in i:
            global level
            level = int(i[i.find('=')+1])
            print('level =',level)

def newsave(location):
    f = open(location,'w+')
    f.write('bossKilled=0\n')
    f.write('hp=100\n')
    f.write('gold=0\n')
    f.write('level=1\n')
    f.close()

def savegame(location):
    f = open(location,'w+')
    write=('bossKilled='+str(bossKilled)+'\n')
    f.write(write)
    write=('hp='+str(hp)+'\n')
    f.write(write)
    write=('gold='+str(gold)+'\n')
    f.write(write)
    write=('level='+str(level)+'\n')
    f.write(write)
    f.close()

while True:
    loadOrNew = input('load game or new game? ')
    if loadOrNew == 'load':
        location = input('save location? (give a file name .save): ')
        loadsave(location)

        break
    elif loadOrNew == 'new':
        location = input('file name to save too (must end in .save) ')
        newsave(location)
        loadsave(location)
        break
    else:
        print('invalid option')

while True:
    print('kill boss, heal, upgrade sword, print stats, save')
    query = input('what would you like to do: ')

    if query == 'save':
        location = input('where to save to? ')
        savegame(location)
        break

    elif query == 'kill boss':
        chance = random.randint(0,2)
        if chance == 0 or chance == 1:
            print('you have won the battle')
            foundGold = random.randint(50,100)*level
            gold = gold + foundGold
            print('you found',foundGold,'gold')
            print('you have',gold,'gold')
            hplost = random.randint(0,30)
            hp = hp - hplost
            bossKilled = bossKilled + 1
            if hp < 0:
                print('sorry you died deleating save')
                newsave(location)
                break
            else:
                print('you survived the battle and have',hp,'hp left')
        else:
            print('you didnt find a boss to kill')

    elif query == 'heal':
        if gold >= 50:
            print('you spend 50 gold and return to full health')
            gold = gold-50
            hp = 100
        else:
            print('you dont have enough gold to heal (50 needed)')


    
    elif query == 'upgrade sword':
        if gold >= 100:
            print('you spend 100 gold to upgrade your sword')
            gold = gold-100
            level = level + 1
        else:
            print('you dont have enough gold for that (100 needed)')
    
    elif query == 'print stats':
        print('hp =',hp)
        print('gold =',gold)
        print('level =',level)
        print('bosses killed =',bossKilled)
    else:
        print('invalid response')

    if bossKilled == 10:
        print('hey there baby its me, your boyfriend\nif your reading this you found the easteregg i left for you\ni love you more than you will ever know and i will always be here for you\n i hope you like this little game i made for you\n you love, lucas')

