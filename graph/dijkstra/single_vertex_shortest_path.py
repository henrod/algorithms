'''
Implement Dijkstra without a class.

Because of that, it isn't possible to reference the node, update its distance and heapify.

So re-add the node with the new distance. When first popped from the min_heap (it's popped when
min_distance is reached), add it to visited set and stop visiting it.
'''

import heapq


def build_graph(n: int, edges: list[tuple[int, int, int]]) -> dict[int, list[tuple[int, int]]]:
    graph: dict[int, list[tuple[int, int]]] = {v: [] for v in range(n)}

    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))

    return graph


def dijkstra(n: int, edges: list[tuple[int, int, int]], start: int, end: int) -> int:
    graph = build_graph(n, edges)
    min_heap = [(0, start)]
    visited: set[int] = set()

    while min_heap:
        distance, vertex = heapq.heappop(min_heap)
        if vertex in visited:
            continue

        if vertex == end:
            return distance

        visited.add(vertex)

        for adj, w in graph[vertex]:
            if adj not in visited:
                heapq.heappush(min_heap, (distance + w, adj))

    return -1


if __name__ == '__main__':
    tests = [
        (
            5, 0, 3, [(0, 1, 1), (0, 2, 5), (1, 3, 10), (2, 3, 2)],
            7
        ),
        (
            5, 1, 3,
            [(0, 1, 1), (0, 2, 5), (1, 3, 10), (2, 3, 2)],
            8
        ),
    ]

    for n_test, (n, start, end, edges, expected) in enumerate(tests):
        result = dijkstra(n, edges, start, end)
        if result != expected:
            raise Exception(f'Test {n_test} failed:'
                            f'result={result}, expected={expected}')
    print('Success!')
