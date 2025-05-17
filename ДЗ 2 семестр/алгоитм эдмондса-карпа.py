edges = [
    (0, 1, 3),
    (0, 2, 2),
    (1, 2, 5),
    (1, 3, 2),
    (2, 3, 3)}

def max_flow(n, s, t, edges):
    g = [[] for i in range(n)]
    for u, v, c in edges:
        g[u].append([v, len(g[v]), c])
        g[v].append([u, len(g[u])-1, 0])
    f = 0
    while 1:
        q = [s]
        p = [-1]*n
        p[s] = -2
        while q:
            u = q.pop(0)
            for v, rev, c in g[u]:
                if p[v] == -1 and c > 0:
                    p[v] = u
                    if v == t:
                        q = []
                        break
                    q.append(v)
        if p[t] == -1:
            return f
        mf = 1e18
        v = t
        while v != s:
            u = p[v]
            for i, (neigh, rev, c) in enumerate(g[u]):
                if neigh == v:
                    mf = min(mf, c)
                    break
            v = u
        v = t
        while v != s:
            u = p[v]
            for i, (neigh, rev, c) in enumerate(g[u]):
                if neigh == v:
                    g[u][i][2] -= mf
                    g[v][rev][2] += mf
                    break
            v = u
        f += mf

print(max_flow(4, 0, 3, edges))