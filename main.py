#from Szemely import Szemely #innen vedd ki a kommentet!
# mindig bekell importálnunk az osztályunkat  a fenti módszerrel
#így már elfogjuk érni a main.py-ból


"""Ez a fájl  Cséfalvy Tanárnő videója alapján készült ,
szerzői jog fenntartva!,"
"""
"""
Régen az alábbi módon csináltuk összekapcsolódó adatok kezelését
ez nem jó mert macerás és sok figyelmet igényel
"""
nev=["Zoli","Éva"]
nem=["férfi","nő"]
szul_ev=[1969,2001]
"""
alább a már elkészült Személy osztályból fogunk létrehozni 1 példányt
ami használja majd a Személy osztály minden általunk létrehozott adattagjait
(vagyis belső változóit) 
"""
"""
1.első személyünk létrehozása 1db sorban a 3 különböző lista helyett
2.sokkal kezelhetőbb ,csak úgy mint egy függvényt paraméterrekkel 
úgy hivjuk meg/adjuk meg neki az adattagokat
3.a Személy osztály konstruktora(init) 3 paramétert várt név,nem,év
ezeket megis adtuk neki innentől kezdve példány.adattag(jelen esetben szemely1.nev)
hivatkozunk egy adott tagjára
"""
#szemely1= Szemely("Zoli","férfi",1969) #innen vedd ki a kommentet!
#szemely2=Szemely("Jolán","nő",2001) #innen vedd ki a kommentet!
#a fent létrehozott példány nevét kitudjuk így printelni:
""" 
megtudjuk változtatni az adott példányunk adatait,
ha azok publikusak(később ezt kikell küszöbölni
nem szerencsés h bárki csak úgy belepiszkáljon
"""
"""print(szemely1.__nev)"""
"""A név privát adatagunkat csak így érjük el az általunk kreált
 getter függvényünkel(ez azért fontos ,hogy egyáltalán elérjük
 tehát "példány.get_privatadattag()" 
"""
#print(szemely1.get_nev()) #innen vedd ki a kommentet!
#print(szemely1.nem) #innen vedd ki a kommentet!
"""print(szemely1)"""
#azonban ha a konkrét ez csak az objektum példány memóricímét fogja kiprintelni
#nekünk ez nem beszédes ezért kell a to string metódus!( Személy.pyban leírás.)
#kommenteld ki a to string metódust a Szemely.pyban! így látod majd a különbséget.

#setter:
#ez az ellenőrzött változtatás így tudjuk
#szemely1.set_nev("Zoltán") #innen vedd ki a kommentet!
#különböző printelések ezeket változtassátok bátran(persze ésszel :D)
#print(szemely1) #innen vedd ki a kommentet!
#print(szemely2) #innen vedd ki a kommentet!
#print(f"Jolán kora: {szemely2.kor()}") #innen vedd ki a kommentet!
#print(f"Zoltán kora: {szemely1.kor()}") #innen vedd ki a kommentet!
#vagy az alábbi módszer ha jobban tetszik.
#print(f"{szemely2.get_nev()} kora: {szemely2.kor()} ") #innen vedd ki a kommentet!
#print(f"{szemely1.get_nev()} kora: {szemely1.kor()} ") #innen vedd ki a kommentet!
