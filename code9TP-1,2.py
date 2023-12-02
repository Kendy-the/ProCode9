from random import randrange

#tèt affichaj
print('=====Hé, Byenvini !!!=====')
print('===== jwèt lawoulèt ======')
print('Mwen gen yon nonb sekrè ou')
print('pral devine ki nonb li ye ')
print('--Ou genyen jiska 5 chans-')
print(' -pou Jwenn ki nonb li ye ')
print('=======Bon chans !!!=======')

#inisyalizasyon
chans = 5
lansePati = 1
nonb_òdinatè = randrange (0,100)

print(nonb_òdinatè)
#antre itilizatè
nonbChwazi = int (input ('\nantre yon nonb antye : '))

#lansman jwèt
while lansePati :
    
    while chans :
        
        #chache genyen AK pèdi
        if(nonb_òdinatè < nonbChwazi):
            if nonbChwazi > 100 :
                print('\nli pa pi gwo ke 100\n')
            if chans < 5 :
                print('\nou rete ',chans,' chans')
            nonbChwazi = int (input ('\nantre yon pi piti nonb : '))
            
        elif (nonb_òdinatè > nonbChwazi) :
            if nonbChwazi < 0 :
                print('\nli pa pi piti ke zero (0)\n')
            if chans < 5 :
                print('\nou rete ',chans,' chans')
            nonbChwazi = int (input ('\nantre yon pi gwo nonb : '))
        if(nonb_òdinatè == nonbChwazi) :
            print('\nFelisitasyon ou genyen !!!')
            print('peze (1 : rejwe) ou (0 : bay vag) ')
            lansePati = int (input())
            break
        chans-=1
        
        #si chans fini
        if not chans :
            print('\nOu pèdi !')
            print ('Nonb lan se te : ',nonb_òdinatè,'\n')
            print('peze (1 : rejwe) ou (0 : bay vag) ')
            lansePati = int (input())
            
    #pou relanse jwèt    
    if lansePati :
       nonb_òdinatè = randrange (0,100)
       nonbChwazi = int (input ('\nantre yon nonb antye : '))
       chans = 5

#Mesaj final       
print('\nMèsi, fen program !')            