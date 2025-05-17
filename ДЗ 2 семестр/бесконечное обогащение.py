n = int(input())
m = int(input())
e = []
for i in range(m):
    u, v, r = map(float, input().split())
    e.append((int(u), int(v), r))

def solve(n, e):
    d = [0]*n
    d[0] = 1
    for j in range(n):
        f = False
        for u,v,r in e:
            if d[v] < d[u]*r:
                d[v] = d[u]*r
                f = True
        if not f:
            break
    for u,v,r in e:
        if d[v] < d[u]*r:
            return True
    return False

print("YES" if solve(n, e) else "NO")