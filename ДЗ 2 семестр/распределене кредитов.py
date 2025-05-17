n = 2
a = [100, 200]
b = [150, 150]
edges = [
    [0, 1],
    [1]      ]

def sharethatbitch(n, a, b, edges):
    sa = sum(a)
    sb = sum(b)
    if sa != sb:
        return False

    cap = [[0] * (2 * n + 2) for _ in range(2 * n + 2)]
    for i in range(n):
        cap[0][i + 1] = a[i]
        for j in edges[i]:
            cap[i + 1][n + 1 + j] = float('inf')
    for j in range(n):
        cap[n + 1 + j][2 * n + 1] = b[j]

    flow = 0
    while True:
        q = [0]
        p = [-1] * (2 * n + 2)
        p[0] = -2
        while q:
            u = q.pop(0)
            for v in range(2 * n + 2):
                if p[v] == -1 and cap[u][v] > 0:
                    p[v] = u
                    if v == 2 * n + 1:
                        break
                    q.append(v)
        if p[2 * n + 1] == -1:
            return flow == sa
        mf = float('inf')
        v = 2 * n + 1
        while v != 0:
            u = p[v]
            mf = min(mf, cap[u][v])
            v = u
        v = 2 * n + 1
        while v != 0:
            u = p[v]
            cap[u][v] -= mf
            cap[v][u] += mf
            v = u
        flow += mf

print(sharethatbitch(n, a, b, edges))