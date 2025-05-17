def johnson(g):
    n = len(g)
    g.append([(i, 0) for i in range(n)])
    h = [0] * (n + 1)
    for _ in range(n):
        f = False
        for u in range(n + 1):
            for v, w in g[u]:
                if h[v] > h[u] + w:
                    h[v] = h[u] + w
                    f = True
        if not f:
            break
    else:
        return None
    g.pop()
    for u in range(n):
        for i in range(len(g[u])):
            v, w = g[u][i]
            g[u][i] = (v, w + h[u] - h[v])
    d = [[float('inf')] * n for _ in range(n)]
    for u in range(n):
        q = []
        q.append((0, u))
        d[u][u] = 0
        while q:
            c, x = q.pop(0)
            if c > d[u][x]:
                continue
            for v, w in g[x]:
                if d[u][v] > c + w:
                    d[u][v] = c + w
                    q.append((d[u][v], v))
        q.sort()
    for u in range(n):
        for v in range(n):
            if d[u][v] != float('inf'):
                d[u][v] += h[v] - h[u]
    return d