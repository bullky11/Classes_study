"""
az osztály gyakorlatilag egy sablon amit elég egyszer létrehoznunk nem kell 156713 személt begépelni
és kezelni egyesével.
mi a szemely1 példányunk/változónkal létrehoztunk 1 példányt(példányosítás!)
meghívjuk a Szemely osztály konttruktorát olyan paraméterekkel amit vár tőlünk a sablon
a példányosított osztály az OBJEKTUM!!!!!(ismerős?:P)
a self szócska jelentése:mindig a konkrét egyedre fog mutatni(önmagára a példányban)
pl a szemely1 csakis magára a szemely2 meg megint csak magára(nem önre!) mutat
így nem lesz közöttük kavarodás

"""

import datetime
#beimportáltuk ezt a datetimeotezzel a pontos időt tudjuk lekérni(pl kiszámolni valakinek a korát)

class Szemely:

    def __init__(self,nev,nem,szul_ev):# osztály konstruktor
        #ebben a fügvényben  fogunk létrehozni a változóinkat
        #vagyis adattagjaink(publikusak megtudjuk változtatni őket kívülről)
        self.__nev=nev #privát adattag(nem változtatható)
        self.nem=nem #publikus adattag(elérjük kintről változtatható)
        self.szul_ev=int(szul_ev)
    #a to string metódos

    # az osztály saját függvénye getter:
    #privátadattagok értékeit tudjuk lekérdezni
    def get_nev(self):
        return self.__nev
    #setter - olyan osztály függvények,amelyekkel beállíthatjuk a privát adattagok értékeit
    #ellenőrzött körülmények közt lehet variálni
    def set_nev(self,adat):
        self.__nev=adat

    #tagfüggvények- az osztály adattagjain végeznek műveleteket
    """
    itt pl. a kort akarjuk kiszámolni a kor tagfüggyvénnyel, létrehozunk egy változót x-néven
    ebbet a "datetime.datetime.now()"ot mentjük el(ne foglalkozz vele neten fenn van ,sok egyéb ilyen mellett) ,
    gyakorlatilag a pontos időt mondja meg(hozzá kell importálni a "datetime"-ot !
    ezután "return"-t használva a pontos idő évéből="xyear" kivonjuk a saját példány 
    születési évét="self.szul_ev (így megkapjuk ezzel a függvénnyel h ki hány éves)
    """
    def kor(self):
        x=datetime.datetime.now()
        return x.year - self.szul_ev

    def __str__(self):
        return f"{self.__nev}, {self.nem} , {self.szul_ev}"