import random
import os

szelveny = []
for n in range(1, 91):
    szelveny.append(n)

print('tippeld meg a nyeroszamakat!')
tippek = []

while len(tippek) < 5:
    tipp = int(input(f'{len(tippek) + 1}. tipped: '))
    if tipp in tippek:
        print('ez már volt -.-')
    else:
        tippek.append(tipp)

random.shuffle(szelveny)
nyeroszamok = szelveny[:5]

talalatok = 0

for n in tippek:
    if n in nyeroszamok: talalatok += 1

os.system('cls')

print(f'ezeket a számokat játszottad meg: {tippek}')
print(f'ezek a heti nyerőszámok: {nyeroszamok}')
print(f'ennyi találatod volt: {talalatok}')