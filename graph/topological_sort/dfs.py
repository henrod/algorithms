def build_graph(n: int, edges: list[tuple[int, int]]) -> dict[int, list[int]]:
    graph: dict[int, list[int]] = {v: [] for v in range(n)}
    for u, v in edges:
        graph[u].append(v)
    return graph


def _dfs(graph: dict[int, list[int]], r: list[int], visited: set[int], vertex: int) -> None:
    for adj in graph[vertex]:
        if adj not in visited:
            visited.add(adj)
            _dfs(graph, r, visited, adj)

    r.append(vertex)


def topological_sort(n: int, edges: list[tuple[int, int]]) -> list[int]:
    graph = build_graph(n, edges)
    visited: set[int] = set()
    r: list[int] = []

    for vertex in range(n):
        if vertex not in visited:
            visited.add(vertex)
            _dfs(graph, r, visited, vertex)

    r.reverse()

    return r


if __name__ == '__main__':
    tests = [
        (
            6,
            [(0, 1), (1, 2), (1, 3), (2, 4), (3, 4), (4, 5)],
            [0, 1, 3, 2, 4, 5]
        ),
        (
            6,
            [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4)],
            [5, 0, 2, 1, 3, 4]
        ),
    ]

    for n_test, (n, edges, expected) in enumerate(tests):
        result = topological_sort(n, edges)
        if result != expected:
            raise Exception(f'Test {n_test} failed:'
                            f'result={result}, expected={expected}')
    print('Success!')
