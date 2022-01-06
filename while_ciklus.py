n = 1
db = 0
while n < 100000000:
    n *= 2
    print(n)
    db += 1

print(f"a ciklus {db}-szer futott le")
print(f"tehát a 2^{db}. hatványa {pow(2, 27)}")

# i = 0
# while True:
#     print('Zolik' + i * 'a')
#     i += 1

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
