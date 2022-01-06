import random
# 0 és 9 közötti véletlen számokkal, 10 elemű listát úgy, hogy ne legyen ismétlődés

print('---------------------')
lista = []
for n in range(10):
    lista.append(n)
print(lista)
for n in range(len(lista)):
    x = random.randrange(len(lista))
    y = random.randrange(len(lista))
    s = lista[x]
    lista[x] = lista[y]
    lista[y] = s
print(lista)



print('---------------------')
lista = []
futasok_szama = 0
while len(lista) < 10:
    n = random.randrange(10)
    if n not in lista:
        lista.append(n)
    futasok_szama += 1
print(lista)
print(f'lefutások száma: {futasok_szama}')



print('---------------------')
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(lista)
print(lista)


lista.sort()
print(lista)
