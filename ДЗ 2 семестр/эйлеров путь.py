def eulerway(g):
    n = len(g)
    deg = [0] * n
    for u in range(n):
        for v in g[u]:
            deg[v] += 1
        deg[u] += len(g[u])
    start = [u for u in range(n) if deg[u] % 2 == 1]
    if len(start) not in (0, 2):
        return []
    if not start:
        start = [0]
    st, res = [start[0]], []
    while st:
        u = st[-1]
        if g[u]:
            v = g[u].pop()
            st.append(v)
        else:
            res.append(st.pop())
    return res[::-1] if all(not e for e in g) else []