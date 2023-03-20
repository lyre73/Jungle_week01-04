# 최소비용 구하기
"""
function Dijkstra(Graph, source):
    dist[source] ← 0                                    // 초기화

    create vertex set Q

    for each vertex v in Graph:
        if v ≠ source
            dist[v] ← INFINITY                          // 소스에서 v까지의 아직 모르는 길이
        prev[v] ← UNDEFINED                             // v의 이전 노드

        Q.add_with_priority(v, dist[v])

    while Q is not empty:                          // 메인 루프
        u ← Q.extract_min()                         // 최고의 꼭짓점을 제거하고 반환한다
        for each neighbor v of u:              // Q에 여전히 남아 있는 v에 대해서만
            alt ← dist[u] + length(u, v)
            if alt < dist[v]
                dist[v] ← alt
                prev[v] ← u
                Q.decrease_priority(v, alt)
    return dist, prev
"""
import sys, heapq
input = sys.stdin.readline

N = int(input()) # 도시(정점) 개수
M = int(input()) # 버스(간선) 개수
G = [[] for _ in range(N + 1)]
total_fare = [float("inf")] * (N + 1) # 출발 도시부터 각 정점까지의 최소 비용(미방문 시 inf)

for _ in range(M):
    city1, city2, fare = map(int, input().split())
    G[city1].append((fare, city2))

start, end = map(int, input().split())
total_fare[start] = 0

Q = [(0, start)]

while Q:
    u = heapq.heappop(Q)
    _, u_city = u

    if u_city == end:
        print(total_fare[u_city])
        break

    for v in G[u_city]:
        v_fare, v_city = v
        v_fare += total_fare[u_city]
        if v_fare < total_fare[v_city]:
            total_fare[v_city] = v_fare
            heapq.heappush(Q, (total_fare[v_city], v_city))