givemeyournumbers = input()
jeskie_chisla = givemeyournumbers.split()

a  = int(jeskie_chisla[0])
b =  int(jeskie_chisla[1])
gcd = 0
x = 0
y = 0
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y
print (gcd, x, y)