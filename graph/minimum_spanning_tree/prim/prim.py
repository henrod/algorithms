from __future__ import annotations
import sys
import heapq

inf = sys.maxsize


class _Node:
    def __init__(self, vertex: int, key: int) -> None:
        self.vertex = vertex
        self.key = key
        self.parent: int | None = None

    def __lt__(self, other: _Node) -> bool:
        return self.key < other.key

    def __repr__(self) -> str:
        return f'{self.vertex}[{self.key}]-->{self.parent}'


def prim(n: int, edges: list[tuple[int, int, int]]) -> list[tuple[int, int]]:
    graph: dict[int, list[tuple[int, int]]] = {v: [] for v in range(n)}
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))

    nodes: list[_Node] = [_Node(v, inf) for v in range(n)]
    min_heap = [node for node in nodes]
    min_heap[0].key = 0
    heap_cache = {node.vertex for node in nodes}

    while min_heap:
        node = heapq.heappop(min_heap)
        heap_cache.remove(node.vertex)

        for adj_vertex, w in graph[node.vertex]:
            adj = nodes[adj_vertex]
            if adj.key > w and adj.vertex in heap_cache:
                adj.key = w
                adj.parent = node.vertex

        heapq.heapify(min_heap)

    mst: list[tuple[int, int]] = [
        (node.parent, node.vertex)
        for node in nodes
        if node.parent is not None
    ]

    return mst


def run_tests() -> None:
    tests = [
        (
            4,
            [(0, 1, 1), (0, 2, 5), (1, 3, 10), (2, 3, 2)],
            [(0, 1), (0, 2), (2, 3)],
        ),
        (
            4,
            [(0, 1, 1), (1, 2, 1), (2, 3, 1), (0, 3, -10)],
            [(0, 1), (3, 2), (0, 3)],
        ),
        (
            4,
            [(0, 2, -30), (0, 3, -10), (1, 2, -5), (1, 3, -10), (2, 3, 10)],
            [(3, 1), (0, 2), (0, 3)],
        )
    ]

    for n_test, (n, edges, expected) in enumerate(tests):
        result = prim(n, edges)
        if result != expected:
            raise Exception(f'Test #{n_test} failed:'
                            f'\nresult={result}\nexpected={expected}')

    print('Success!')


if __name__ == '__main__':
    run_tests()
