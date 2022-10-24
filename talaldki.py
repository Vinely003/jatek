import random
import time

rSzam = random.randint(1, 101)
print("Gondoltam egy számra 1 és 100 között. Találd ki.")
igazE = True
while igazE:
    szam = input("Adj meg egy számot: ")
    if szam.isnumeric():
        szam1 = int(szam)
        if szam1 >= 1 and szam1 <= 100:
            if szam1 < rSzam:
                print("A gondolt szám nagyobb")
            elif szam1 > rSzam:
                print("A gondolt szám kissebb")
            else:
                print("Kitalátad")
                igazE = False
        else:
            print("1 és 100 között add meg a számot")
    else:
        print("Nem számot adtál meg")
time.sleep(50000)
