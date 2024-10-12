'''''
Многоточие...
'''
textik = open ("input.txt", 'r')
lines = textik.readlines()
a = list(map(str, lines[0].split()))
skolko = 0
for i in range(len(lines)):
    if '.' in lines[i] or '!' in lines[i] or '?' in lines[i] or '*/&*^%$#@' in lines[i]:
        skolko += 1
print(skolko)
textik.close()