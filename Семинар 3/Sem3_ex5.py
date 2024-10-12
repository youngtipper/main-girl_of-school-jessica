import numpy as np

a = input ('Введите размеры вашей шоколадки с числами:')
size = a.split()
n = a[0]
m = a[1]

matrix = np.zeros(n,m)

verh = 0
niz = n - 1
levo = 0
pravo = m - 1

n = 1

while levo <= pravo:
    for i in range(levo, pravo + 1):
        matrix[verh][i] = n
        n += 1
    verh += 1

    for i in range (verh, niz + 1):
        matrix[i][pravo] = n
        n += 1
    pravo -= 1

    if verh <= niz:

        