'''
Implement Dijkstra with a class.
Because of that, it's possible to reference the node, update its distance and heapify.
'''

from __future__ import annotations
import sys
import heapq

inf = sys.maxsize


def build_graph(n: int, edges: list[tuple[int, int, int]]) -> dict[int, list[tuple[int, int]]]:
    graph: dict[int, list[tuple[int, int]]] = {v: [] for v in range(n)}

    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))

    return graph


def dijkstra(
    n: int,
    start: int,
    edges: list[tuple[int, int, int]],
) -> tuple[list[int], list[int | None]]:
    graph = build_graph(n, edges)
    min_heap: list[tuple[int, int | None, int]] = [(0, None, start)]
    visited: set[int] = set()

    distances: list[int] = [inf] * n
    parents: list[int | None] = [None] * n

    while min_heap:
        distance, parent, node = heapq.heappop(min_heap)
        if node in visited:
            continue

        distances[node] = distance
        parents[node] = parent
        visited.add(node)

        for adj, w in graph[node]:
            heapq.heappush(min_heap, (distance + w, node, adj))

    return distances, parents


def run_tests() -> None:
    tests = [
        (
            5, 0,
            [(0, 1, 1), (0, 2, 5), (1, 3, 10), (2, 3, 2)],
            [0, 1, 5, 7, inf],
            [None, 0, 0, 2, None],
        ),
        (
            5, 1,
            [(0, 1, 1), (0, 2, 5), (1, 3, 10), (2, 3, 2)],
            [1, 0, 6, 8, inf],
            [1, None, 0, 2, None],
        ),
        (
            5, 4,
            [(0, 1, 1), (0, 2, 5), (1, 3, 10), (2, 3, 2)],
            [inf, inf, inf, inf, 0],
            [None, None, None, None, None],
        ),
        (
            4, 0,
            [(0, 1, 1), (1, 2, 1), (2, 3, 1), (0, 3, 100)],
            [0, 1, 2, 3],
            [None, 0, 1, 2],
        ),
    ]

    for n_test, (n, start, edges, expected_distances, expected_parents) in enumerate(tests):
        result_distances, result_parents = dijkstra(n, start, edges)
        if result_distances != expected_distances:
            raise Exception(f'Distances test #{n_test} failed:'
                            f'result={result_distances}, expected={expected_distances}')
        if result_parents != expected_parents:
            raise Exception(f'Distances test #{n_test} failed:'
                            f'result={result_parents}, expected={expected_parents}')
    print('Success!')


if __name__ == '__main__':
    run_tests()
