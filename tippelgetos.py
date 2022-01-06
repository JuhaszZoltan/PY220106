import random

szam = random.randint(1, 100)
tipp = -1
probalkozasok = 0
print('gondoltam egy számra')
while tipp != szam:
    tipp = int(input('mi a tipped?: '))
    if tipp < szam:
        print('nem, nagyobbra gondoltam!')
    if tipp > szam:
        print('nem, kisebbre gondoltam!')
    probalkozasok += 1

print(f"grat nyetél! valóban a {szam}-ra gondoltam!")
print(f"{probalkozasok} tippből sikerült kitalálnod")

i = 0
while i < 10:
    print('jz')
    i += 1

for i in range(10):
    print('jz')
