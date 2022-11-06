from __future__ import annotations
import sys
from heapq import heappop, heapify

inf = sys.maxsize


class Dijkstra:
    class _Node:
        def __init__(self, vertex: int, distance: int = inf) -> None:
            self.distance = distance
            self.vertex = vertex

        def __lt__(self, other: Dijkstra._Node) -> bool:
            return self.distance < other.distance

    def __init__(self, n: int, edges: list[tuple[int, int, int]]) -> None:
        self._graph = Dijkstra.build_graph(n, edges)

    @staticmethod
    def build_graph(n: int, edges: list[tuple[int, int, int]]) -> dict[int, list[tuple[int, int]]]:
        graph: dict[int, list[tuple[int, int]]] = {v: [] for v in range(n)}

        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        return graph

    def distances(self, source: int) -> list[int]:
        nodes: list[Dijkstra._Node] = [self._Node(v) for v in range(len(self._graph))]
        nodes[source].distance = 0

        min_heap: list[Dijkstra._Node] = nodes.copy()
        heapify(min_heap)

        distances: list[int] = [inf] * len(nodes)

        while min_heap:
            node = heappop(min_heap)
            distances[node.vertex] = node.distance

            for adj_vertex, w in self._graph[node.vertex]:
                adj = nodes[adj_vertex]
                adj.distance = min(adj.distance, node.distance + w)

            heapify(min_heap)

        return distances


if __name__ == '__main__':
    tests = [
        (
            5, 0,
            [(0, 1, 1), (0, 2, 5), (1, 3, 10), (2, 3, 2)],
            [0, 1, 5, 7, inf]
        ),
        (
            5, 1,
            [(0, 1, 1), (0, 2, 5), (1, 3, 10), (2, 3, 2)],
            [1, 0, 6, 8, inf]
        ),
        (
            5, 4,
            [(0, 1, 1), (0, 2, 5), (1, 3, 10), (2, 3, 2)],
            [inf, inf, inf, inf, 0]
        ),
        (
            4, 0,
            [(0, 1, 1), (1, 2, 1), (2, 3, 1), (0, 3, 100)],
            [0, 1, 2, 3]
        ),
    ]

    for n_test, (n, source, edges, expected) in enumerate(tests):
        dijkstra = Dijkstra(n, edges)
        result = dijkstra.distances(source)
        if result != expected:
            raise Exception(f'Test {n_test} failed:'
                            f'result={result}, expected={expected}')
    print('Success!')
