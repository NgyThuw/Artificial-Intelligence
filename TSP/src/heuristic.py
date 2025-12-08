import math

def tsp_nearest_neighbor(cost, start=0):
    n = len(cost)
    visited = [False] * n
    route = [start]
    visited[start] = True
    total_cost = 0
    current = start

    for _ in range(n - 1):
        next_city = None
        next_cost = math.inf
        for v in range(n):
            if not visited[v] and cost[current][v] < next_cost:
                next_city = v
                next_cost = cost[current][v]
        route.append(next_city)
        visited[next_city] = True
        total_cost += next_cost
        current = next_city

    total_cost += cost[current][start]
    route.append(start)
    return route, total_cost
