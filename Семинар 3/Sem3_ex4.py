razmery = input()
treugolnik = razmery.split()
dlina = int(treugolnik[0])
simvol = treugolnik[1]

for i in range (dlina):
    print (simvol * (i + 1))
for i in range (dlina):
    print (simvol * (dlina - i - 1))

