def so_bro_lemme_build_thatshit(pi):
    if not pi:
        return ""
    if pi[0] != 0:
        return ""

    n = len(pi)
    s = ['a'] * n
    for i in range(1, n):
        if pi[i] > 0:
            s[i] = s[pi[i] - 1]
        else:
            used = set()
            k = pi[i - 1]
            while k > 0:
                used.add(s[k])
                k = pi[k - 1]
            used.add(s[0])
            for c in 'abcdefghijklmnopqrstuvwxyz':
                if c not in used:
                    s[i] = c
                    break
    return ''.join(s)

pi = [0, 0, 1, 0, 1, 2, 3]
print(so_bro_lemme_build_thatshit(pi))