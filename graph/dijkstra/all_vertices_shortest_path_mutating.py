'''
Implement Dijkstra with a class.
Because of that, it's possible to reference the node, update its distance and heapify.
'''

from __future__ import annotations
import sys
from heapq import heappop, heapify

inf = sys.maxsize


class Dijkstra:
    class _Node:
        def __init__(self, vertex: int, distance: int = inf) -> None:
            self.distance = distance
            self.vertex = vertex
            self.parent: int = -1

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

    def _dijkstra(self, source: int) -> list[Dijkstra._Node]:
        nodes: list[Dijkstra._Node] = [self._Node(v) for v in range(len(self._graph))]
        nodes[source].distance = 0

        min_heap: list[Dijkstra._Node] = nodes.copy()
        heapify(min_heap)

        while min_heap:
            node = heappop(min_heap)

            for adj_vertex, w in self._graph[node.vertex]:
                adj = nodes[adj_vertex]
                if node.distance + w < adj.distance:
                    adj.distance = node.distance + w
                    adj.parent = node.vertex

            heapify(min_heap)

        return nodes

    def shortest_paths(self, source: int) -> list[int]:
        nodes = self._dijkstra(source)
        return [node.distance for node in nodes]

    def shortest_paths_topological_sort(self, source: int) -> list[int]:
        nodes = self._dijkstra(source)
        r: list[int] = []
        visited: set[int] = set()

        def dfs(vertex: int) -> None:
            parent = nodes[vertex].parent
            if parent >= 0 and parent not in visited:
                visited.add(parent)
                dfs(parent)

            r.append(vertex)

        for delta in range(len(nodes)):
            vertex = (source + delta) % len(nodes)
            if vertex not in visited:
                visited.add(vertex)
                dfs(vertex)

        return r


def run_distances_tests() -> None:
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
        result = dijkstra.shortest_paths(source)
        if result != expected:
            raise Exception(f'Distances test #{n_test} failed:'
                            f'result={result}, expected={expected}')
    print('Success!')


def run_topological_sort_tests() -> None:
    tests = [
        (
            5, 0,
            [(0, 1, 1), (0, 2, 5), (1, 3, 10), (2, 3, 2)],
            [0, 1, 2, 3, 4]
        ),
        (
            5, 1,
            [(0, 1, 1), (0, 2, 5), (1, 3, 10), (2, 3, 2)],
            [1, 0, 2, 3, 4]
        ),
        (
            5, 4,
            [(0, 1, 1), (0, 2, 5), (1, 3, 10), (2, 3, 2)],
            [4, 0, 1, 2, 3]
        ),
        (
            4, 0,
            [(0, 1, 1), (1, 2, 1), (2, 3, 1), (0, 3, 100)],
            [0, 1, 2, 3]
        ),
    ]

    for n_test, (n, source, edges, expected) in enumerate(tests):
        dijkstra = Dijkstra(n, edges)
        result = dijkstra.shortest_paths_topological_sort(source)
        if result != expected:
            raise Exception(f'Topological sort test #{n_test} failed:'
                            f'result={result}, expected={expected}')
    print('Success!')


if __name__ == '__main__':
    run_distances_tests()
    run_topological_sort_tests()
