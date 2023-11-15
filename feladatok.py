import random
import math


"""
Írj eljárást, mely a paraméterként kap két egész számot
ezen két egész szám közötti
páros számok összegét számolja ki az eljárás
"""
def feladat1(a:int,b:int):
    i:int=a
    osszeg:int=0
    while i<=b:
        if i%2==0:
            osszeg+=i
        i+=1
    print(f"A páros számok összege:{osszeg}")
    return osszeg


"""
Írj függvényt, amely  generál 20 db véletlen számot 
-10 és 20 között
számold meg hány negatív szám van közötte a visszatérési érték a negatív számok száma
"""
def negativ():
    i:int=0
    db:int=0
    for i in range (0,20,1):
        szam:int=math.floor(random.random()*21-10)
        if szam<0:
            db+=1
        #i+=1
    return db
def paros2(a:int,b:int):
    osszeg:int=0
    for i in range(a,b,1):
        if i%2==0:
            osszeg+=i
        return osszeg
""" 
Irj függvényt amely generál 10 véletlen számot {12,33}között és visszatér ezek öszzegével.
"""
def veletlen():
    osszeg:int=0
    for i in range(0,10,1):
        szam:int=math.floor(random.random()*(34-12)+12)
        osszeg+=1
    return osszeg

"""
Írj függvényt amely genreál 8 db véletlen számot számot,{20,50) intervallumban,
 és visszatér ezek közül a legnagyobb számmal
"""
def veletlen2():
    i=1
    for i in range(0,8,1):
        szam:int=math.floor(random.random()*(50-20)+20)
        if szam>i:
            i=szam
    return i


"""
Kérjünk be 3 db egész számot a felhasználótol
mekkora a számok átlaga?
"""

def egesz_bekert():
    osszeg=0
    for i in range(0,3,1):
        szam: int = int(input(f"Kérem az{i+1},egész számot"))
        osszeg+=szam
    return osszeg/3

"""
Kérjük be egész számokat a felh-től
amíg 0-t nem ad!
írjuk ki a számok átlagát
"""

def nulla_szam():
    i=0
    db:int=1
    osszeg=0
    szam:int=int(input(f"Kérem az {i+1}. egész számot"))
    while szam!=0:
        osszeg+=szam
        db+=1
        i+=1
        szam:int=int(input(f"Kérem az {i+1}. számot"))
    return osszeg / (db-1)




