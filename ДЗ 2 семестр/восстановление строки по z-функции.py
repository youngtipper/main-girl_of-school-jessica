def zzzzzz(z):
    if not z:
        return ""
    if z[0] != 0:
        return ""

    n = len(z)
    s = ['a'] * n
    for i in range(1, n):
        if z[i] > 0:
            for j in range(z[i]):
                if i + j >= n:
                    break
                s[i + j] = s[j]
        else:
            used = set()
            j = 0
            while j < i and i + j < n and z[j] >= i - j:
                used.add(s[j])
                j += 1
            for c in 'abcdefghijklmnopqrstuvwxyz':
                if c not in used:
                    s[i] = c
                    break
    return ''.join(s)

z = [0, 0, 2, 0, 3, 0, 1]
print(zzzzzz(z))

#хорошая функция православные названия