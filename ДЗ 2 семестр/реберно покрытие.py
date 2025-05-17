n = 3
m = 3
edges = [
    [3, 4],
    [3, 5],
    [4]]

def min_edge_cover(n, m, edges):
    match_to = [-1] * (n + m)
    res = []

    def bpm(u, seen):
        for v in edges[u]:
            if not seen[v]:
                seen[v] = True
                if match_to[v] == -1 or bpm(match_to[v], seen):
                    match_to[v] = u
                    return True
        return False

    for u in range(n):
        seen = [False] * (n + m)
        bpm(u, seen)

    used = [False] * (n + m)
    for v in range(n, n + m):
        if match_to[v] != -1:
            res.append((match_to[v], v))
            used[match_to[v]] = True
            used[v] = True

    for u in range(n):
        if not used[u] and edges[u]:
            res.append((u, edges[u][0]))
            used[edges[u][0]] = True

    for v in range(n, n + m):
        if not used[v] and match_to[v] != -1:
            res.append((match_to[v], v))

    return res

print(min_edge_cover(n, m, edges))