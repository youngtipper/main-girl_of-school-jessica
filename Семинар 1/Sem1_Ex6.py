bebra_chisla = open ("input.txt", 'r')
lines = bebra_chisla.readlines()
a = list(map(int, lines[0].split()))
op = lines[1]
base = list(map(int, lines[2]))
a_2 = []
if base != 10:
    number = 0
    power = 0

    for i in a:
        k = str(i)
        k_1 = k[::-1]
        number = 0
        power = 0
        for m in k_1:
            number += int(m)*(base**power)
            power += 1
        a_2.append(number)

else:
    a_2 = a

print(a_2, "a_2")
            
if op == "+":
    res = sum(a_2)
elif op == "-":
    res = a_2[0]
    for i in a_2[1:]:
        res -= i 
else:
    res = 1
    for i in a_2:
        res *= i

print (res)
bebra_chisla.close()
bebra_otvet = open ("output.txt", "w")
bebra_otvet.write(str(res))
bebra_otvet.close()
