'''''
"Никогда не говорите мне "в среднем".
Корова утонула в реке, где ей в среднем было по колено."
'''
normis = 0
ya_sprashivayu_skolko = int(input())
spisok = list(map(int, input().split()))
res = 0
for i in range(ya_sprashivayu_skolko):
        if res == (ya_sprashivayu_skolko-1)/2:
            break
        res = 0
        for j in range(ya_sprashivayu_skolko):
            if spisok[i] > spisok[j]:
                res += 1
        normis = spisok[i]
print(normis)


