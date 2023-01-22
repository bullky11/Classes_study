from Szemely import Szemely
""" Adott személyekről tároljuk a nevüket, a nemüket és a születési évüket,végezzük el az alábbi feladatokat"""
"""
1.Mekkora az átlag életkor?
2.Hány férfi és hány nő van a listában?
3.van-e 30 év alatti nő?
"""

szemely1=Szemely("Zoli","férfi",1969)
szemely2=Szemely("Jenő","férfi",1999)
szemely3=Szemely("Jolán","nő",2000)
szemely4=Szemely("Jézus","férfi",0)
#belaraktuk egy listába az osztály példaányaink(objektumok)
szemely=[szemely1,szemely2,szemely3,szemely4]
print(szemely[1].szul_ev) #pl így hivatkozol a lista első elemének(szemely1)születési évére
print(szemely)
"""memóriacímeket éred el(nem annyira beszédes) 
de debuggerbe futtasd add meg figyeltnek a szemely- töréspontoknak a printeket
 szépen látni fogod az elemeit és védett attribútumait is"""
#1 feladat
def atlageletkor():
    i=0
    ossz_eletkor=0
    while i<len(szemely):
        ossz_eletkor+=szemely[i].kor()
        i+=1
    #kiirhatjuk i vel osztva vagy listahosszal osztva, a .2f a két tizedezjegyet jelenti
    print(f"az össz kor= {ossz_eletkor}")
    print(f"az korok átlaga: {ossz_eletkor/i}")
    print(f"az korok átlaga: {ossz_eletkor / len(szemely):.2f}")

#2.feladat
#a lenti nőkszáma az alapfüggvényt , a férfi és nőfüggvényt összeisvonhatjuk az alábbi módon

def ferfi_noszama(felt):
    i=0
    db=0
    while i<len(szemely):
        if szemely[i].nem==felt:
            db+=1
        i+=1
    return  db
"""def nokszama():
    i=0
    nodarab=0
    while i<len(szemely):
        if szemely[i].nem=="nő":
            nodarab+=1
        i+=1
    return  nodarab"""

#3.feladat itt több megoldást is láthatsz ami nincs kikommentelve az a tanárnő videója alapján van
def vane_30_ev_alatti_no():
   i=0
   while i<len(szemely) and not(szemely[i].nem=='nő' and szemely[i].kor()<30):
       i+=1
   return i < len(szemely)
#3.2férfi verzio
def vane_30_ev_alatti_ferfi():
   i=0
   while i<len(szemely) and not(szemely[i].nem=='férfi' and szemely[i].kor()<30):
       i+=1
   return i < len(szemely)

atlageletkor() #videóban eltér majd mert  tavalyi videó így a mai dátumból von ki nekünk tanárnőnek meg 2022 es dátum szerepel
print(f"A férfiak száma:{ferfi_noszama('férfi')}")#férfi feltétel
print(f"a Nők száma: {ferfi_noszama('nő')}")#nő feltétel
print("30 alattiak:")
vanen=vane_30_ev_alatti_no()
if vanen:
    print("Van 30 év alatti nő a listában")
else:
    print("nincs 30 év alatti nő a listában")

vanef=vane_30_ev_alatti_ferfi()
if vanef:
    print("Van 30 év alatti férfi a listában")
else:
    print("nincs 30 év alatti férfi a listában")