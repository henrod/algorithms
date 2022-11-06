from collections import deque


def build_graph(n: int, edges: list[tuple[int, int]]) -> dict[int, list[int]]:
    graph: dict[int, list[int]] = {v: [] for v in range(n)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    return graph


def _bfs(graph: dict[int, list[int]], source: int, r: list[int], visited: set[int]) -> None:
    queue = deque([source])

    while queue:
        vertex = queue.popleft()
        r.append(vertex)

        for adj in graph[vertex]:
            if adj not in visited:
                visited.add(adj)
                queue.append(adj)


def bfs(n: int, edges: list[tuple[int, int]]) -> list[int]:
    graph = build_graph(n, edges)
    visited: set[int] = set()
    r: list[int] = []

    for vertex in range(n):
        if vertex not in visited:
            visited.add(vertex)
            _bfs(graph, vertex, r, visited)

    return r


if __name__ == '__main__':
    tests = [
        (
            6,
            [(0, 1), (1, 2), (1, 3), (2, 4), (3, 4), (4, 5)],
            [0, 1, 2, 3, 4, 5]
        ),
        (
            4,
            [(0, 1), (0, 2), (1, 3)],
            [0, 1, 2, 3]
        ),
    ]

    for n_test, (n, edges, expected) in enumerate(tests):
        result = bfs(n, edges)
        if result != expected:
            raise Exception(f'Test {n_test} failed:'
                            f'result={result}, expected={expected}')
    print('Success!')
