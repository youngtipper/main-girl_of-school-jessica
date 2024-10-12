bebra_chisla = open ("input.txt", 'r')
lines = bebra_chisla.readlines()
a = list(map(int, lines[0].split()))
op = lines[1]
if op == "+":
    res = sum(a)
elif op == "-":
    res = a[0]
    for i in a[1:]:
        res -= i 
else:
    res = 1
    for i in a:
        res *= i
bebra_chisla.close()
bebra_otvet = open ("output.txt", "w")
bebra_otvet.write(str(res))
bebra_otvet.close()