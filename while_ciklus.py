# n = 2
# db = 0
# while n < 100000000:
#     n *= 2
#     print(n)
#     db += 1

# print(f"a ciklus {db}-szer futott le")
# print(f"és  a 2 27. hatánya az {pow(2, 27)}")

# i = 0
# while True:
#     print('Zolik' + i * 'a')
#     i += 1
#     if i == 10: break

jelszo = 'pwd'
probalkozas = 0
bekert = ''

while jelszo != bekert and probalkozas < 3:
    bekert = input('írd be a jelszavad: ')
    probalkozas += 1

if jelszo == 'pwd': print('siker')
else: print('majd máskor :(')

# x = 0
# while x < 10:
#     print('JZ')