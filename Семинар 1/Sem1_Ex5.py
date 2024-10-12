N = int(input())    # число на входе
b = int(input())    # системка счисления исходная
c = int(input())   # системка счисления конечная (понапридумывают билят)
s = ""
if  b != 10 and c == 10:
    N_1 = str(N)
    answer = 0
    power = 0
    N_2 = N_1[::-1]
    for i in N_2:
        answer += int(i)*(b**power)
        power += 1
    print(answer)

elif b == 10:
    while N > 0:
        s = str(N % c) + s
        N //= c
    print(s)

elif b != 10 and c != 10:
    N_1 = str(N)
    number = 0
    power2 = 0
    N_2 = N_1[N::-1]
    for i in N_2:
        number += int(i)*(b**power2)
        power2 += 1
    while number > 0:
        s = str(number % c) + s
        number //= c
    print(s)
    






    