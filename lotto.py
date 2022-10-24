import random

szelveny = list(list(map(int, input("Add meg az 5 NYERŐszámot vesszővel elválasztva: ").split(","))))
print("Húzott számok: ", szelveny)
rSzam = random.sample(range(1, 100), 5)
print("Lottószámok: ", rSzam)
talalat = 0
for i in rSzam:
    for j in szelveny:
        if j == i:
            talalat = talalat + 1

print("Talált számok: ", talalat)