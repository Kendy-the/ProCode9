#ex-1 mete karaktè miniskil
chèn = 'MWEN SE PRESUME'
chèn_1 = str.lower(chèn)
print('Ex-1')
print('Ansyen chèn : ',chèn)
print('Nouvo chèn : ',chèn_1,'\n')

#ex-2 koupe yon chèn nan espas li yo
nouvoChèn = chèn.split()
print('Exo-2')
print('Ansyen chèn : ',chèn)
print('lis : ',nouvoChèn,'\n')

#ex-3 mete premye lèt chak mo an majiskil
#defini yon chèn vid
chèn_2 = ''
print('Exo-3')
print('Ansyen chèn : ',chèn)
#mete Chak mo(aprè separasyon) an majiskil
for mo in chèn.split() :
    mo = mo.capitalize()
    chèn_2 = chèn_2+' '+mo
#remete chèn nan nan plas li    
chèn = chèn_2
print('Nouvo chèn : ',chèn,'\n')

#ex-4 rekipere premye lèt chak mo
#defini yon chèn vid
chèn_2 = ''
#dekoupe chèn an mo épi pran premye lèt chak mo
for mo in chèn.split() :
    chèn_2 = chèn_2+mo[0]
print('Exo-4')
print('Ansyen chèn : ',chèn)    
print('Nouvo chèn : ',chèn_2,'\n')

#ex-5 ranplase tout "a" pa "@"
chèn_2 = "Manman m ap aprann programe nan langaj python"
print('Exo-5')
print('Ansyen chèn : ',chèn)
chèn_2 = chèn.replace("a","@")
print('Nouvo chèn : ',chèn_2,'\n')

#ex-6 envèse yon chèn e mete li an majiskil
print('Exo-6')
#defini chèn vid
chèn_3 = ''
print('Ansyen chèn : ',chèn)
#envèse chèn 
for el in chèn :
    chèn_3 = el + chèn_3
chèn_3 = chèn_3.upper()    
print('Nouvo chèn : ',chèn_3,'\n')  

#exo-7 affiche endèks premye karaktè "a" nan yon chèn
print('Exo-7')
chèn_2 = "manmAn m AP aprAnn programe nan lAngaj python "
print('chèn : ',chèn_2)
endèks = chèn_2.find('a')
print('endèks : ',endèks,'\n')

#exo-8 afiche total tout endèks karaktè a
print('Exo-8')
print ('chèn : ',chèn_2)
#chache endèks Chak karaktè 'a'
i = 0 # kontè Pou Jwenn endèks 'a'
total = 0 # pou kalkile total endèks
while i < len(chèn_2) :
    if ((chèn_2[i] == 'a') or (chèn_2[i] == 'A')) :
        total += i
    i+=1    
print('total : ',total,'\n')

#exo-9 lis endèks karaktè 'a'
i = 0
endèks = 0
lis = []
while i < len(chèn_2) :
    if (chèn_2[i] == 'a') :
        lis.append(i)
    i+=1
print('Exo-9')
print('chèn : ',chèn_2)    
print('lis : ',lis,'\n')

#exo-10 wete espas nan chenn, ranplasel pa nb karaktè chenn
print('Exo-10')
print('Ansyen chèn : ',chèn_2,'\n')
#chache plasman espas yo
i = 0
k = 0 # kontè Pou denyè endis lis
lisEspas = []
while i < len(chèn_2) :
    if chèn_2[i] == ' ' :
        lisEspas.append(i)
        k+=1
    i+=1

#retire espas ki nan chèn nan
chèn_2 = chèn_2.split()

#chèn tanporè San espas
chènTanporè = ''
i = 0
while i < k :
    chènTanporè = chènTanporè+chèn_2[i]
    i+=1
    
#longè chèn San espas
longèChèn = str(len(chènTanporè))

#arnjman chèn separe Avèk longè chèn San espas
chèn_4 = ''
i = 0
while i < k :
    chèn_4 = chèn_4+chèn_2[i]+longèChèn
    i+=1
#retire dénye longèChèn nan nan chèn nan
i = 0
chèn_5 =''
while i < len(chèn_4) :
    if(i < (len(chèn_4))-2) :
        chèn_5 = chèn_5+chèn_4[i]
    i+=1
#remete chèn nan nan plas li
chèn_2 = chèn_5       
print('Nouvo chèn : ',chèn_2,'\n')    
