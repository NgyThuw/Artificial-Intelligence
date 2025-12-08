import math

def tsp_held_karp(cost, start=0):
    n = len(cost)
    dp = [[math.inf] * n for _ in range(1 << n)]
    parent = [[-1] * n for _ in range(1 << n)]
    dp[1 << start][start] = 0

    for mask in range(1 << n):
        if not (mask & (1 << start)):
            continue
        for u in range(n):
            if not (mask & (1 << u)):
                continue
            prev_cost = dp[mask][u]
            if prev_cost == math.inf:
                continue
            for v in range(n):
                if mask & (1 << v):
                    continue
                new_mask = mask | (1 << v)
                cand = prev_cost + cost[u][v]
                if cand < dp[new_mask][v]:
                    dp[new_mask][v] = cand
                    parent[new_mask][v] = u

    full_mask = (1 << n) - 1
    best_cost = math.inf
    last = -1
    for u in range(n):
        if u == start:
            continue
        cand = dp[full_mask][u] + cost[u][start]
        if cand < best_cost:
            best_cost = cand
            last = u

    route = [start]
    mask = full_mask
    u = last
    stack = []
    while u != -1:
        stack.append(u)
        pu = parent[mask][u]
        mask ^= 1 << u
        u = pu
    stack.reverse()
    route += stack
    route.append(start)

    return route, best_cost
